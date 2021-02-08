#!/bin/bash

source "dconf-prefix.sh"

dconf_prefix org/cinnamon/desktop/interface > interface.conf
dconf_prefix org/cinnamon/desktop/wm/preferences >> interface.conf
