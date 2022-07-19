FROM alpine as base
RUN mkdir /app
COPY ./** /app
WORKDIR /app
RUN sh ./install_docker.sh
CMD ["yarn", "start"]
