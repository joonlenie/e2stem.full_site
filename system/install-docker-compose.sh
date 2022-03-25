#!/bin/sh

# Install Python dependencies

sudo apt-get install libffi-dev libssl-dev
sudo apt install python3-dev
sudo apt-get install -y python3 python3-pip

# Install Docker-Compose

sudo pip3 install docker-compose

sudo systemctl enable docker

