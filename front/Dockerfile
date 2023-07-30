FROM node:17-alpine
ENV \
  TZ=Europe/Moscow \
  NUXT_HOST=0.0.0.0 \
  NUXT_PORT=3000


RUN mkdir -p /usr/src/nuxt-app
WORKDIR /usr/src/nuxt-app
COPY . .

RUN npm ci && npm cache clean --force
RUN npm run build



EXPOSE 3000

ENTRYPOINT ["node", ".output/server/index.mjs"]