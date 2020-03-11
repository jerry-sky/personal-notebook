#!/bin/bash

# Git
alias ga="git add"
alias gaa="git add ."
alias gts="git status"
alias gcm="git commit -m"
alias gph="git push"
alias gpl="git pull"
alias gplr="git pull --rebase"
alias gf="git fetch"
alias gdf="git diff HEAD"

# VS Code shortcuts
# alias cx="code && exit"
alias ccx="code . && exit"
alias c="code"
alias ccc="code ."

function cx() {
  code $1 && exit
}


# General alias for programs with GUIs but that can be run from bash
# redirects the output to /dev/null to avoid unnecessary clutter
# in the terminal window
# it can be used for e.g. Blender
function --() {
  # first parameter is the program to run
  # second parameter is the file to open with that program
  $1 $2 &> /dev/null &
}

# a use-case for the -- function for Blender
# adds .blend at the end of the provided filename
function b() {
  if [ $(echo $1 | grep .blend) ]; then
    -- blender $1
  else
    -- blender $1.blend
  fi
}
