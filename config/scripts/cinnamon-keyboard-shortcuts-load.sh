#!/bin/bash

dconf load /org/cinnamon/desktop/keybindings/ < cinnamon-keyboard-shortcuts.conf

printf " + copied cinnamon keyboard shortcuts"
