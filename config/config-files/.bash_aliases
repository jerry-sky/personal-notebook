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
function __git_remote() {
    # this function gets the default origin for the branch
    branch=$(git branch --show-current)
    remote=$(git config branch."$branch".remote)
    if [ -z "$remote" ]; then
        remote="origin"
    fi
    echo $remote
}
function __git_remote_parse() {
    # this function parses given remote and branch target
    dest="$1"
    # return status
    status=0
    if [ -z "$dest" ] || [[ "$dest" == -* ]]; then
        dest="$(__git_remote)"
        status=2
    fi
    if [[ "$dest" != */* ]]; then
        dest="$dest/$(git branch --show-current)"
    fi
    echo $dest | tr '/' ' '
    return $status
}
function gph() {
    dest=$(__git_remote_parse "$1")
    empty=$?
    printf "\033[1;7m pushing to $dest \033[0m\n"
    printf "\033[1;38;5;249m press RETURN to continue \033[0m"
    # give user chance to abort pushing
    read
    if [ "$empty" = "0" ]; then
        shift # remove the original argument
    fi
    git push $dest "$@"
}
function gpl() {
    dest=$(__git_remote_parse "$1")
    printf "\033[1;7m pulling from $dest \033[0m\n"
    printf "\033[1;38;5;249m press RETURN to continue \033[0m"
    # give user change to abort pulling
    read
    if [ "$empty" = "0" ]; then
        shift # remove the original argument
    fi
    git pull --rebase $dest "$@"
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
alias ccx="code-insiders . && exit"
alias c="code-insiders"
alias ch="code-insiders ."
function cx() {
  code-insiders $@ && exit
}

# Google Chrome browser
alias gc="google-chrome-stable"

# from Markdown to PDF converter
alias mdpdf="pandoc \
    --from markdown-blank_before_header-implicit_figures+lists_without_preceding_blankline+gfm_auto_identifiers \
    --to pdf \
    -V geometry:margin=2cm \
    -H ~/notebooks/personal-notebook/config/config-files/head.tex \
    --number-sections \
    --toc-depth 4 \
    --shift-heading-level-by=-1"

# Quick local directory server (hsh stands for HTTP server here)
alias hsh="python3 -m http.server --bind localhost 4200"

# Nemo (file explorer) aliases
alias n="-- nemo"
alias n.="-- nemo ."
alias nh="-- nemo ."

# opening another terminal from terminal (in the same directory)
alias t="gnome-terminal"

# leave the last viewed page in the terminal after exit
alias lx="less -Xr"

function lxp() {
    $@ | less -Xr
}

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
