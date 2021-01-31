FROM node:14.15.4-alpine3.12

WORKDIR /app

COPY package*.json ./
RUN npm install --production

COPY ./src ./src

EXPOSE 4000

CMD ["npm","start"]