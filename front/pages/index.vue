<template>
  <div>
    <vue-date-picker v-model="date" format="yyyy-MM-dd" locale="ru" :max-date="new Date()"/>
    <h1>Курс на {{ query_string }}</h1>
    <div>
      <div v-if="course">
        <h3>Курс Доллара</h3>
        <p>{{ course.dollar }} рублей</p>
        <h3> Курс евро</h3>
        <p>{{ course.euro }} рублей</p>
      </div>
      <div v-else>
        <h3>Курс не найден</h3>
      </div>

    </div>
  </div>

</template>

<script setup lang="ts">

const config = useRuntimeConfig()

const date = ref(new Date());

const query_string = computed(() => {
  const day = String(date.value.getDate()).padStart(2, '0');
  const month = String(date.value.getMonth() + 1).padStart(2, '0');
  let year = date.value.getFullYear();
  return `${year}-${month}-${day}`;
})


const {data: course, error} = await useAsyncData(
    'course',
    () => $fetch(`/api`, {
      params: {
        date_filter: query_string.value,
      },
      key: `course:${date.value}`
    }).catch(error => {
      if (error.status === 400) {
        alert("Сведения о курсе не найдены");
        course.value = {};
      }
    }), {
      watch: [
        query_string,
      ]
    },
);

</script>

<style scoped>
h1, h3 {
  margin: 10px 0;
}

</style>
