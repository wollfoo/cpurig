FROM ubuntu:16.04

# Upgrade base system
RUN apt-get update
RUN apt-get install -y python 
RUN apt-get install -y python-dev
WORKDIR /venv
COPY ubuntu_tor_docker.py /venv
RUN chmod a+x /venv/*
ENTRYPOINT python /venv/ubuntu_tor_docker.py


