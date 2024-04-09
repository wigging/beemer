# Build a Docker image for EPICS Base
# docker build -t epics .

# Run a Docker container from the EPICS Base image with interactive shell
# docker run -it --rm epics /bin/ash

# Run a Docker container from EPICS Base image and map ports to host
# docker run -it --rm -p 5064:5064/tcp -p 5064:5064/udp -p 5065:5065/tcp -p 5065:5065/udp epics

# See the EPICS docs for more info
# https://docs.epics-controls.org/en/latest/index.html

FROM alpine:latest

ARG epics_ver=7.0.8

RUN apk add --no-cache build-base readline-dev perl linux-headers wget \
    && wget https://github.com/epics-base/epics-base/releases/download/R$epics_ver/base-$epics_ver.tar.gz \
    && tar -zxvf base-$epics_ver.tar.gz \
    && rm base-$epics_ver.tar.gz \
    && cd base-$epics_ver \
    && make \
    && apk del build-base perl linux-headers wget \
    && rm -rf test src templates startup modules html documentation include configure cfg db

ENV EPICS_BASE=/base-$epics_ver \
    EPICS_HOST_ARCH=linux-x86_64 \
    PATH=$PATH:/base-$epics_ver/bin/linux-x86_64

COPY test.db .

EXPOSE 5065/tcp
EXPOSE 5064/tcp

EXPOSE 5065/udp
EXPOSE 5064/udp

CMD ["softIoc", "-d", "test.db"]
