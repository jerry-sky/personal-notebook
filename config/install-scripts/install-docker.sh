#!/bin/bash

printf '\n'
printf '\033[1m%s\033[0m\n' 'Docker' 'Installing Docker…'
printf '\n'

sudo apt-get update

# remove old installations of Docker
sudo apt-get remove -y docker docker-engine docker.io containerd runc

# install necessary utilities
sudo apt-get install -y \
    apt-transport-https \
    ca-certificates \
    curl \
    gnupg \
    lsb-release

# add Docker’s official GPG key
sudo mkdir -p /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg

ubuntu_codename=$(lsb_release -cs)

echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
  $ubuntu_codename stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null


# install Docker Engine
sudo chmod a+r /etc/apt/keyrings/docker.gpg
sudo apt-get update
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-compose-plugin

# permissions for standard user
sudo groupadd docker
sudo usermod -aG docker $USER
newgrp docker


printf "\n\033[1m%s\033[0m\n\n" "Verifying Docker installation…"
docker run hello-world
