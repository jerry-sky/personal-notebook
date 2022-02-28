#/bin/bash

printf "\n\033[1mi3-gaps\033[0m\n"

printf "\n\033[1mInstalling…\033[0m\n"
# add the PPA
sudo add-apt-repository -y ppa:regolith-linux/stable
sudo apt-get update
# install the WM
sudo apt-get install i3-gaps
