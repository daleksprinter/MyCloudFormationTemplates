FROM golang:latest as builder

RUN mkdir /go/src/work
WORKDIR /go/src/work

COPY main.go .

ENV CGO_ENABLED=0
ENV GOOS=linux
ENV GOARCH=amd64

RUN go build -o main

FROM alpine:latest
RUN apk --no-cache add ca-certificates
COPY --from=builder /go/src/work/main /main
ENTRYPOINT ["/main"]
