#!/bin/sh

# Update system

sudo apt-get update && sudo apt-get upgrade

# Install Docker and add the users

curl -sSL https://get.docker.com | sh

sudo usermod -aG docker Pi


# And reboot.



