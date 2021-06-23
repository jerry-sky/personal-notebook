#!/bin/bash

cd /tmp
mkdir -p fira-code
cd fira-code
printf "\n\033[1mAdditional font packs\nDownloading and installing Fira Code…\033[0m\n"
curl -L --output fira-code.zip 'https://fonts.google.com/download?family=Fira%20Code'
unzip fira-code.zip
rm fira-code.zip
cd ..
sudo mv fira-code /usr/share/fonts/truetype/

mkdir -p fira-sans
cd fira-sans
printf "\n\033[1mDownloading and installing Fira Sans…\033[0m\n"
curl -L --output fira-sans.zip 'https://fonts.google.com/download?family=Fira%20Sans'
unzip fira-sans.zip
rm fira-sans.zip
cd ..
sudo mv fira-sans /usr/share/fonts/truetype/

mkdir -p merriweather
cd merriweather
printf "\n\033[1mDownloading and installing Merriweather…\033[0m\n"
curl -L --output merriweather.zip 'https://fonts.google.com/download?family=Merriweather'
unzip merriweather.zip
rm merriweather.zip
cd ..
sudo mv merriweather /usr/share/fonts/truetype
