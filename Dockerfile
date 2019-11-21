FROM ubuntu:16.04

# Upgrade base system
RUN apt-get update
WORKDIR /venv
COPY ubuntu_tor_docker.py /venv
RUN chmod a+x /venv/*
CMD python ubuntu_tor_docker.py
