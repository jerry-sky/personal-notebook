#!/bin/bash

function get_device_id {
    device_name="$1"
    xinput list | egrep "$device_name" | awk -F'=' '{print $2}' | awk '{print $1}'
}

function alter_prop {
    # Changes given prop’s value of the preselected Xinput device.
    device_id="$1"
    prop_name="$2"
    prop_value="$3"
    prop_id=`xinput list-props $device_id | grep "$prop_name" | head -n1 | head -n1 | awk -F'(' '{print $2}' | awk -F')' '{print $1}'`
    xinput set-prop "$device_id" "$prop_id" "$prop_value"
}


device_id=`get_device_id 'UNIW0001.*Touchpad'`

alter_prop "$device_id" 'Tapping Enabled' '1'
alter_prop "$device_id" 'Natural Scrolling Enabled' '1'
alter_prop "$device_id" 'Disable While Typing Enabled' '0'
alter_prop "$device_id" 'Middle Emulation Enabled' '1'
