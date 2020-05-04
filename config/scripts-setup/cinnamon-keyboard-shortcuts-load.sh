#!/bin/bash

dconf load /org/cinnamon/desktop/keybindings/ < ./config-files/cinnamon-keyboard-shortcuts.conf

printf " + loaded Cinnamon keyboard shortcuts\n"
