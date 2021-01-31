FROM node:14.15.4-alpine3.12
WORKDIR /app
COPY package*.json ./
RUN npm ci --production
COPY ./src ./src

EXPOSE 5000

CMD ["npm","start"]