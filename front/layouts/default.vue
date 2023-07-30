<template>
  <div id="main">

    <div id="center-block">
      <slot/>
    </div>

  </div>
</template>


<style scoped>
* {
  box-sizing: border-box;
}

#main {
  min-width: 100vw;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
}


</style>