FROM ghcr.io/security-onion-solutions/golang:1.22.6-alpine AS build
LABEL maintainer "Security Onion Solutions, LLC"
ARG STRELKA_RELEASE_VERSION=0.24.01.18

RUN CGO_ENABLED=0 go install github.com/target/strelka/src/go/cmd/strelka-manager@$STRELKA_RELEASE_VERSION

FROM ghcr.io/security-onion-solutions/alpine:3.20.2
COPY --from=build /go/bin/strelka-manager /usr/local/bin/
RUN addgroup -g 939 strelka && \
    adduser -u 939 -G strelka strelka --disabled-password \
    -h /etc/strelka --no-create-home strelka
USER strelka
