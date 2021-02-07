#!/bin/bash

# download the archive
cd '/tmp'
curl -L --output telegram.tar.xz 'https://telegram.org/dl/desktop/linux'

# unpack the archive
tar -xf telegram.tar.xz

# run the program in the background
Telegram/Telegram &>/dev/null &
