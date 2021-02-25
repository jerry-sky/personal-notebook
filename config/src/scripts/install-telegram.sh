#!/bin/bash

# download the archive
cd '/opt'
sudo curl -L --output telegram.tar.xz 'https://telegram.org/dl/desktop/linux'

# unpack and remove the archive
sudo tar -xf telegram.tar.xz
sudo rm telegram.tar.xz

# run the program in the background
Telegram/Telegram &>/dev/null &
