#!/bin/bash

CD="$1"

HD="/home/jerry-sky"

read -s -p 'OBS WS password: ' OBS_password
printf '\n'

if [ -z "$CD" ]; then
    echo 'provide the second-keyboard config directory path'
    exit 1
fi

if [ -z "$OBS_password" ]; then
    echo 'provide the OBS WS password'
    exit 1
fi

# download the script
cd second-keyboard
git clone --depth 1 'https://github.com/robinuniverse/Keebie' tmp
mv tmp/keebie.py ./
sed -i '1s/.*/#!\/usr\/bin\/env python3/' keebie.py
rm -rf tmp

# install necessary packages
sudo apt-get install -y xdotool x11-utils
python3 -m pip install evdev

# copy the script that gains read+write access to the keyboard device file
mkdir -p $HD/second-keyboard
sudo cp "$CD"/second-keyboard/gain-access.sh $HD/second-keyboard/gain-access.sh

# copy the sudoers file
# that enables the aforementioned ‘gain access’ script to be run with root
# privileges without providing a password
sudo cp "$CD"/second-keyboard/sudoers /etc/sudoers.d/second-keyboard
sudo chown root:root /etc/sudoers.d/second-keyboard

# change ownership to root
sudo chown root:root $HD/second-keyboard/gain-access.sh
sudo chmod 4755 $HD/second-keyboard/gain-access.sh

# ---

# OBS-related settings

# OBS WebSockets password
printf "$OBS_password" > "$CD"/second-keyboard/scripts/.ws
