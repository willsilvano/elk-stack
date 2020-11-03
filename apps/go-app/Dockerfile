FROM golang:1.15
ENV ELASTIC_APM_SERVICE_NAME='Go App'
ENV ELASTIC_APM_SERVER_URL='http://apm-server:8200'
ENV ELASTIC_APM_SECRET_TOKEN='changeme'
WORKDIR /go/src/app
RUN go get go.elastic.co/apm
COPY . .
RUN GOOS=linux go build -ldflags="-s -w"
CMD ["./app"]