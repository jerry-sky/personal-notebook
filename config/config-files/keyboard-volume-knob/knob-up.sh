#!/bin/bash

prefix="$HOME/keyboard-volume-knob"

step=${1:-5}

if [ -f "$prefix/volume" ]; then
    pactl set-sink-volume @DEFAULT_SINK@ +$step%
else
    xte "mouseclick 4"
fi

