FROM alpine:3.7

ARG tf_version="0.12.9"

RUN apk update && \
    apk upgrade && \
    apk add ca-certificates && update-ca-certificates
RUN apk add --no-cache --update \
    bash \
    curl \
    git \
    jq \
    lftp \
    libffi-dev \
    make \
    openssh \
    py-pip \
    python3 \
    unzip
RUN apk add dos2unix --update-cache --repository http://dl-3.alpinelinux.org/alpine/edge/community/ --allow-untrusted
RUN apk add --update tzdata