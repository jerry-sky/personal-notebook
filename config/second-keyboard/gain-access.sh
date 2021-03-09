#!/bin/bash

# this script gains read access to the device file of the chosen keyboard

# first, get the path of the device file
device="$(cat /home/jerry-sky/notebooks/personal-notebook/config/second-keyboard/config | head -n1)"

# give read access to it
chmod a+r "$device"
