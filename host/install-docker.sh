#!/bin/sh

# Update system

sudo apt-get update && sudo apt-get upgrade

# Install Docker and add the 

curl -sSL https://get.docker.com | sh

sudo usermod -aG docker Pi

groups Pi

# And reboot...



