#!/bin/bash

printf "\033[1mDiscord\nDownloading…\033[0m\n"

# download the package
curl -L --output '/tmp/discord.deb' 'https://discord.com/api/download?platform=linux&format=deb'

printf "\033[1mInstalling…\033[0m\n"
# install the package
sudo dpkg -i '/tmp/discord.deb'
