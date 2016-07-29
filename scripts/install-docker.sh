#!/bin/bash

# Instructions from https://docs.docker.com/engine/installation/linux/ubuntulinux/

# update the installation sources
apt-get -y update
apt-get -y install apt-transport-https ca-certificates
apt-key adv --keyserver hkp://p80.pool.sks-keyservers.net:80 --recv-keys 58118E89F3A912897C070ADBF76221572C52609D
echo "deb https://apt.dockerproject.org/repo ubuntu-xenial main" > /etc/apt/sources.list.d/docker.list

# install docker 
apt-get -y update
apt-get -y install linux-image-extra-$(uname -r)
apt-get -y install docker-engine=1.12.0-0~xenial
