#!/bin/bash
# changes viewport scale of the currently running virtual machine

function get_running_vm_name() {
    VBoxManage list runningvms | cut -d'"' -f2
}

function main() {
    local scale_factor="$1"
    VBoxManage setextradata "$(get_running_vm_name)" GUI/ScaleFactor "$scale_factor"
}

main "$@"
