#!/bin/bash

printf "\n\033[1m%s\033[0m\n" "Touchégg"

printf "\n\033[1m%s\033[0m\n" "Downloading…"

file="touchegg_2.0.14_amd64.deb"

cd /tmp
wget https://github.com/JoseExposito/touchegg/releases/download/2.0.14/"$file"

printf "\n\033[1m%s\033[0m\n" "Installing…"
sudo dpkg -i /tmp/"$file"
