#!/bin/bash

printf "\n\033[1mKBCT\033[0m\n"

printf "\n\033[1mInstalling…\033[0m\n"

cd /tmp
wget https://github.com/samvel1024/kbct/releases/download/v0.1.0/kbct-x86_64.AppImage

# install it system-wide
chmod +x kbct-x86_64.AppImage
sudo mv kbct-x86_64.AppImage /opt/kbct
sudo ln -s /opt/kbct /usr/bin/kbct

sudo mkdir /etc/kbct
sudo ln -s /home/$USER/notebooks/personal-notebook/config/config-files/kbct/config.yml /etc/kbct/config.yml

# configure it to run on startup, reboot, and after coming back from suspending
sudo cp /home/$USER/notebooks/personal-notebook/config/config-files/kbct/kbct.service /usr/lib/systemd/system/kbct.service
sudo systemctl enable kbct.service
