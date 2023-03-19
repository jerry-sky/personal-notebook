#!/bin/bash

PS1="\[\033[38;2;72;209;217;7;1m\] \W \[\033[00m\033[38;2;72;209;217;240m\] \[\033[00m\]"

PATH="$PATH:/opt/utility-scripts/:/opt/jetbrains"

EDITOR="/usr/bin/vi"
set -o vi

git config --global core.editor /usr/bin/vi
git config --global core.quotepath false
