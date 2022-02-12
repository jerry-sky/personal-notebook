#!/bin/bash

# toggle mute for the default source
pactl set-source-mute $(pacmd list-sources | grep '*' | awk -F ' ' '{print $3}') toggle
killall -SIGUSR1 i3status
