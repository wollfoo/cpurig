FROM ubuntu:16.04

# Upgrade base system
RUN apt-get update
WORKDIR /venv
COPY ubuntu_tor.sh /venv
RUN chmod a+x /venv/*
CMD ./ubuntu_tor.sh
