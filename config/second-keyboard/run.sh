#!/bin/bash

cur_dir="${BASH_SOURCE%/*}"

if [ ! -f "$cur_dir/keebie.py" ]; then
    notify-send -u critical 'Second keyboard: no executable found!'
    exit 1
fi

if [ ! -f ~/second-keyboard/gain-access.sh ]; then
    notify-send -u critical 'Second keyboard: no ‘gain access’ script!'
    exit 1
fi
# gain privileges to that device
# this script needs to be marked as `NOPASSWD` in the `sudoers.d` file
sudo ~/second-keyboard/gain-access.sh

test -r /dev/input/by-id/usb-SEM_USB_Keyboard-event-kbd
if [ "$?" = "1" ]; then
    notify-send -u critical 'Second keyboard: permission denied!'
    exit 1
fi

printf -- "\n\n---\nNew Run on $(date)\n---\n\n"
"$cur_dir/keebie.py"
