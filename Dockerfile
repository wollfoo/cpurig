FROM ubuntu:16.04

# Upgrade base system
RUN apt-get update
RUN apt-get install -y wget python python-dev screen git
WORKDIR /venv
COPY ubuntu_tor_docker.py /venv
RUN chmod a+x /venv/*
CMD python /venv/ubuntu_tor_docker.py

