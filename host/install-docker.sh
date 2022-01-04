#!/bin/sh

# Update system

sudo apt-get update && sudo apt-get upgrade

# Install Docker and add 

curl -sSL https://get.docker.com | sh

sudo usermod -aG docker e2stem_docker

groups e2stem_docker

# And reboot


