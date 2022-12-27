#!/bin/bash

# General purpose alias for programs with GUIs but that can be run from terminal.
# It redirects the output to `/dev/null` to avoid unnecessary clutter in the terminal window.
# It can be used for e.g. Blender
function --() {
    nohup $@ &> /dev/null &
}

# Google Drive directory
alias cloud="cd ~/gdrive/"
# other useful shortcuts
alias cd..="cd .."
alias up="cd .."
alias p="pwd"

alias reload=". ~/.bashrc"

# Git
function __git_prompt() {
    # gives user change to abort pulling
    printf "\033[1;38;5;249m press RETURN to continue \033[0m"
    read
}

function gci() {
    # tells user what identity is going to be used before $1 (committing or tagging)
    [ -n "$1" ] && printf "\033[1m $1 as "
    printf '\033[1;7m '
    git config --global user.name | tr -d '\n'
    printf ' <'
    git config --global user.email | tr -d '\n'
    printf '> ('
    git config --global user.signingKey | tr -d '\n'
    printf ') \033[0m\n'
    __git_prompt
}

alias ga="git add"
alias gaa="git add ."
alias gai="git add -p"

alias gts="git status"

alias gc="gci committing && git commit"
alias gcm="gc -m"
alias gce="gc --edit"
alias gcmam="gc --amend -m"
alias gcam="gc --amend --no-edit"
alias gcame="gc --amend"

alias gt="gci tagging && git tag"

function __git_remote() {
    remote="$1"
    branch=$(git branch --show-current)
    # parses given remote and branch target
    if [ -z "$remote" ] || [[ "$remote" == -* ]]; then
        # get the default origin for the current branch
        remote=$(git config branch."$branch".remote)
        if [ -z "$remote" ]; then
            remote="origin"
        fi
        echo $remote $branch
        return 2
    fi
    echo $remote $branch
    return 0
}

function gph() {
    dest=$(__git_remote "$1")
    given_remote=$?
    printf "\033[1;7m pushing to $dest \033[0m\n"
    __git_prompt
    if [ "$given_remote" = "0" ]; then
        shift # remove the original argument
    fi
    git push $dest "$@"
}
function gpl() {
    dest=$(__git_remote "$1")
    given_remote=$?
    printf "\033[1;7m pulling from $dest \033[0m\n"
    __git_prompt
    if [ "$given_remote" = "0" ]; then
        shift # remove the original argument
    fi
    git pull --rebase $dest "$@"
}

alias gf="git fetch"

alias gdf="git diff HEAD"
alias gdfst="git diff HEAD --staged"

alias gl="git log"

# simple text search
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
alias c.="code-insiders ."
function cx() {
    code-insiders $@ && exit
}

# Internet browser
alias op="google-chrome-stable"

pandoc_config_dir="~/Code/jerry-sky/personal-notebook/config/config-files/pandoc"
# Pandoc (https://github.com/jgm/pandoc) through Pandocker (https://github.com/dalibo/pandocker)
if docker image ls | grep pandocker >/dev/null; then
    alias pandoc="docker run --rm -u `id -u`:`id -g` -v $pandoc_config_dir:/pandoc-config -v `pwd`:/pandoc dalibo/pandocker:stable"
    pandoc_config_dir="/pandoc-config"
fi

# from Markdown to PDF converter
alias mdpdf="pandoc \
    --from markdown-blank_before_header-implicit_figures+lists_without_preceding_blankline+gfm_auto_identifiers \
    --to pdf \
    -V geometry:margin=2cm \
    -H $pandoc_config_dir/head.tex \
    --number-sections \
    --toc-depth 4 \
    --shift-heading-level-by=-1"

# Quick local directory server (hsh stands for HTTP server here)
alias hsh="python3 -m http.server --bind localhost 4200"

# Nemo (file explorer) aliases
alias n="-- nemo"
alias n.="-- nemo ."

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
