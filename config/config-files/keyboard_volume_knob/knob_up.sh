#!/bin/bash

prefix="$HOME/keyboard_volume_knob"

if [ -f "$prefix/volume" ]; then
    pactl set-sink-volume @DEFAULT_SINK@ +2%
else
    xte "mouseclick 4"
fi

