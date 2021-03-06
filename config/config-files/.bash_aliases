#!/bin/bash

# General purpose alias for programs with GUIs but that can be run from terminal.
# It redirects the output to `/dev/null` to avoid unnecessary clutter in the terminal window.
# It can be used for e.g. Blender
function --() {
    $@ &> /dev/null &
}

# directory shortcuts
alias an="cd ~/notebooks/academic-notebook/"
alias pn="cd ~/notebooks/personal-notebook/"
# projects directory
alias cdd="cd ~/code/"
# other useful shortcuts
alias cd..="cd .."
alias cdu="cd .."
alias p="pwd"

alias reload=". ~/.bashrc"

alias audloop="pacmd load-module module-loopback latency_msec=5"

# Git
alias ga="git add"
alias gaa="git add ."
alias gai="git add -p"
alias gts="git status"
alias gcm="git commit -m"
alias gcmam="git commit --amend -m"
alias gcam="git commit --amend --no-edit"
function gph() {
    printf "\033[1;7m pushing to $(git remote)/$(git branch --show-current) \033[0m\n"
    printf "\033[1;38;5;249m press RETURN to continue \033[0m"
    # give user chance to abort pushing
    read
    git push "$@" "$(git remote)" "$(git branch --show-current)"
}
function gpl() {
    printf "\033[1;7m pulling from $(git remote)/$(git branch --show-current) \033[0m\n"
    printf "\033[1;38;5;249m press RETURN to continue \033[0m"
    # give user change to abort pulling
    read
    git pull --rebase "$@" "$(git remote)" "$(git branch --show-current)"
}
alias gf="git fetch"
alias gdf="git diff HEAD"
alias gdfst="git diff HEAD --staged"
alias gl="git log"
alias gg="git grep -n -I"
alias ggi="git grep -n -I -i"
# discarding changes
alias gd="git checkout --"
alias gdi="git checkout -p"
# unstaging changes
alias gu="git reset --"
alias gui="git reset -p"
# stashing
alias gsth="git stash"
# stashing only staged files
alias gsthst="git diff --staged --name-only | git stash"
# other stash commands
alias gsthp="git stash pop"
alias gstha="git stash apply"
alias gsthl="git stash list"

# VS Code shortcuts
alias ccx="code . && exit"
alias c="code"
alias ch="code ."
function cx() {
  code $@ && exit
}

# Nemo (file explorer) aliases
alias n="-- nemo"
alias n.="-- nemo ."
alias nh="-- nemo ."

# opening another terminal from terminal (in the same directory)
alias t="gnome-terminal"

# adds `.blend` if not present in the filename provided when launching a file using blender
function b() {
    if [ $(echo $1 | grep .blend) ]; then
        -- blender $@
    else
        -- blender $1.blend "${@:2}"
    fi
}

# adds `.pur` if not present in the filename provided when launching a file using PureRef
function puref() {
    if [ $(echo $1 | grep .pur) ]; then
        -- PureRef $@
    else
        -- PureRef $1.pur "${@:2}"
    fi
}

# converts a SVG file to a format that is digestible by LaTeX
function inktex() {
    bn="$1"
    bn="${bn%.*}"
    inkscape -D -z --file="$bn.svg" --export-pdf="$bn.pdf" --export-latex
}
