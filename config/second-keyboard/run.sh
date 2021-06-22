#!/bin/bash

cur_dir="${BASH_SOURCE%/*}"

if [ ! -f "$cur_dir/keebie.py" ]; then
    notify-send -u low 'Second keyboard: no executable found!'
    exit 1
fi

if [ ! -f ~/second-keyboard/gain-access.sh ]; then
    notify-send -u critical 'Second keyboard: no ‘gain access’ script!'
    exit 1
fi
# gain privileges to that device
# this script needs to be marked as `NOPASSWD` in the `sudoers.d` file
sudo ~/second-keyboard/gain-access.sh

# get the path of the device
device="$(cat $cur_dir/config | head -n1)"

# check if read-write access is granted
test -rw "$device"
if [ "$?" = "1" ]; then
    notify-send -u critical 'Second keyboard: permission denied!'
    exit 1
fi

printf -- "\n\n---\nNew Run on $(date)\n---\n\n"
"$cur_dir/keebie.py"
