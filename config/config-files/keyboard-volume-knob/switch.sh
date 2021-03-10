#!/bin/bash

# this script allows switching between two modes of the keyboard volume knob
# this is done via creating and deleting two files simply named `scroll` and `volume`

prefix="$HOME/keyboard-volume-knob"

if [ -f "$prefix/scroll" ]; then
  rm -f "$prefix/scroll"
  touch "$prefix/volume"
else
  rm -f "$prefix/volume"
  touch "$prefix/scroll"
fi

