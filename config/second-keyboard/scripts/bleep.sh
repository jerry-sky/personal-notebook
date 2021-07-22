#!/bin/bash

DIR="${BASH_SOURCE%/*}"

virtual_mic_sink="__VIRTUAL_MICROPHONE_PRE_SINK"

hardware_devices=$(pacmd list-sources | grep -B3 HARDWARE | grep index | awk '{print $NF}')
# temporarily mute all the hardware input devices
for device in $hardware_devices; do
    pactl set-source-mute $device on
done

# list all available sinks
# find the one that points to the virtual microphone one
# get its ID
# play the bleep sound to the microphone
PULSE_SINK=$(\
    pacmd list-sinks \
    | grep -B1 '<'"$virtual_mic_sink"'>' \
    | head -n1 \
    | awk '{print $2}' \
) cvlc $DIR/crow-sound.mp3 --play-and-exit &
sleep 0.25

for device in $hardware_devices; do
    pactl set-source-mute $device off
done
