#!/bin/bash

prefix="$HOME/keyboard-volume-knob"

if [ -f "$prefix/volume" ]; then
    pactl set-sink-volume @DEFAULT_SINK@ -2%
else
    xte "mouseclick 5"
fi

