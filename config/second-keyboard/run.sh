#!/bin/bash

cur_dir="${BASH_SOURCE%/*}"

if [ ! -f "$cur_dir/keebie.py"]; then
    notify-send 'Second keyboard: no executable found!'
    exit 1
fi

pkexec chmod a+r /dev/input/by-id/usb-SEM_USB_Keyboard-event-kbd

test -r /dev/input/by-id/usb-SEM_USB_Keyboard-event-kbd
if [ "$?" = "1" ]; then
    notify-send 'Second keyboard: permission denied!'
    exit 1
fi

"$cur_dir/keebie.py"
