#!/bin/bash

printf '\n'
printf '\033[1m%s\033[0m\n' 'Docker' 'Installing Docker…'
printf '\n'

sudo apt-get update
sudo apt-get install -y \
    apt-transport-https \
    ca-certificates \
    curl \
    gnupg \
    lsb-release

curl -fsSL https://download.docker.com/linux/ubuntu/gpg \
    | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg

ubuntu_codename=$(lsb_release -cs)

echo \
  "deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu \
  $ubuntu_codename stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

sudo apt-get update
sudo apt-get install docker-ce docker-ce-cli containerd.io

egrep '^docker:' /etc/group >/dev/null
if [ $? -eq 1 ]; then
    sudo groupadd docker
    sudo usermod -aG docker $USER
    newgrp docker
fi


printf "\n\033[1m%s\033[0m\n\n" "Verifying Docker installation…"
docker run hello-world


printf "\n\033[1m%s\033[0m\n\n" "Installing Docker-Compose…"

sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" \
    -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
