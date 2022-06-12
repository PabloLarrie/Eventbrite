FROM node:16.15.1-slim

WORKDIR /app

ENV PATH /app/node_modules/.bin:$PATH

COPY package*.json ./
RUN npm install
RUN npm install @vue/cli@3.7.0 -g

CMD ["npm", "run", "serve"]
