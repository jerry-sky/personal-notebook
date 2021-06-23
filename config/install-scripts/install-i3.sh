#/bin/bash

printf "\n\033[1mi3-gaps\033[0m\n"

printf "\n\033[1mInstalling…\033[0m\n"
# add the PPA
sudo add-apt-repository -y ppa:regolith-linux/stable
sudo apt-get update
# install the WM
sudo apt-get install i3-gaps

# install some utilities needed for making i3 more towards an actual DE
printf "\n\033[1mInstalling utilities…\033[0m\n"
# dex is needed for the GUI authentication prompt program (see the i3 config)
sudo apt-get install -y dex
# window compositor and background viewer
sudo apt-get install -y compton feh
# YAD — yet another dialog program
sudo apt-get install -y yad
