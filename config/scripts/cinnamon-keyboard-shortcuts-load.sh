#!/bin/bash

dconf load /org/cinnamon/desktop/keybindings/ < cinnamon-keyboard-shortcuts.conf

printf " + loaded Cinnamon keyboard shortcuts\n"
