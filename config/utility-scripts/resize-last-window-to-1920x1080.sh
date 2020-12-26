#!/bin/bash

# check if the `wmctrl` program is installed
if [ ! "$(command -v wmctrl)" ]; then
    echo "wmctrl is not installed"
    exit
fi

# ask the user if the last window is actually
# the one they want to resize
## print the last opened window
wmctrl -l | tail -n 1

echo "resize this window? (type anything to cancel or leave the line empty to resize)"

read tmp
if [ ! "$tmp" ]; then
    ## get the id of the window (substitution)
    ## resize the window by using the id (-i option)
    wmctrl -i -r "$(wmctrl -l | tail -n 1 | cut -d' ' -f1)" -e "0,-1,-1,1920,1080"
    echo "resized"
else
    echo "cancelled"
fi
