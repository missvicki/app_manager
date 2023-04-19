FROM node:latest

WORKDIR /app/frontend

COPY package.json package-lock.json ./

RUN npm install --silent

COPY . ./

# start app
CMD ["npm", "start"]
