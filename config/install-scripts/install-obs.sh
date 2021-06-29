#!/bin/bash

printf "\n\033[1mOBS\033[0m\n"

printf "\n\033[1mInstalling necessary dependencies…\033[0m\n"
sudo apt-get install -y ffmpeg

printf "\n\033[1mInstalling OBS…\033[0m\n"
sudo add-apt-repository -y ppa:obsproject/obs-studio
sudo apt-get install -y obs-studio

printf "\n\033[1mInstalling OBS WebSockets plugin…\033[0m\n"
# find the link to the latest DEB installation package
link=$(curl -sL https://github.com/Palakis/obs-websocket/releases/latest \
    | perl -nle 'print $& if /\/Palakis\/.+\/download\/.+\.deb/g' \
    | head -n1)
# download the DEB package
wget -q https://github.com$link -O /tmp/obs-websocket.deb
# install
sudo dpkg -i /tmp/obs-websocket.deb
# install Python3 dependency
sudo python3 -m pip install simpleobsws

printf "\n\033[1mInstalling OBS StreamFX plugin…\033[0m\n"
# find the link to the latest version
# (currently stuck with 0.10.0, because 0.10.1 makes OBS not openable //TODO upgrade)
link=$(curl -sL https://github.com/Xaymar/obs-StreamFX/releases/tag/0.10.0 \
    | perl -nle 'print $& if /\/Xaymar\/.+\/download\/.+ubuntu.+\.zip/gi' \
    | head -n1)
echo $link
# download
wget -q https://github.com$link -O /tmp/obs-streamfx.zip
# install
unzip -qo /tmp/obs-streamfx.zip -d ~/.config/obs-studio/
