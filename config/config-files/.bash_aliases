#!/bin/bash


alias cd..="cd .."

alias reload=". ~/.bashrc"

# leave the last viewed page in the terminal after exit
alias lx="less -Xr"



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
    local remote="$1"
    local branch=$(git branch --show-current)
    # parses given remote and branch target
    if [ -z "$remote" ] || [[ "$remote" == -* ]]; then
        # get the default origin for the current branch
        remote=$(git config branch."$branch".remote)
        if [ -z "$remote" ]; then
            remote="origin"
        fi
        echo "$remote" "$branch"
        return 2
    fi
    echo "$remote" "$branch"
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
alias glg="git log --graph"

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
alias gsthst="git stash --staged"

# other stash commands
alias gsthp="git stash pop"
alias gstha="git stash apply"
alias gsthl="git stash list"



# editor shortcuts
alias c="code"
function cx() {
    code $@ && exit
}
alias idea="-- jetbrains-idea"
alias storm="-- jetbrains-phpstorm"



# Internet browser
alias op="x-www-browser"

# Quick local directory server (hsh stands for HTTP server here)
alias hsh="python3 -m http.server --bind localhost 4200"



pandoc_config_dir="$HOME/Code/jerry-sky/personal-notebook/config/config-files/pandoc"
alias pandocker="printf '\033[1m%s\033[0m\n' 'warning: Pandocker image not found, running Pandoc instead of Pandocker' && pandoc"
# Pandoc (https://github.com/jgm/pandoc) through Pandocker (https://github.com/dalibo/pandocker)
if docker image ls | grep pandocker >/dev/null; then
    alias pandocker="docker run --rm -u `id -u`:`id -g` -v $pandoc_config_dir:/pandoc-config -v $(pwd):/pandoc dalibo/pandocker:stable"
    pandoc_config_dir="/pandoc-config"
fi

# from Markdown to PDF converter
alias mdpdf="pandocker \
    --from markdown-blank_before_header-implicit_figures+lists_without_preceding_blankline+gfm_auto_identifiers \
    --to pdf \
    -V geometry:margin=2cm \
    -H $pandoc_config_dir/head.tex \
    --number-sections \
    --toc-depth 4 \
    --shift-heading-level-by=-1"



# General purpose alias for programs with GUIs but that can be run from terminal.
# It redirects the output to `/dev/null` to avoid unnecessary clutter in the terminal window.
# It can be used for e.g. Blender
function --() {
    nohup $@ &> /dev/null &
}

# adds `.blend` if not present in the filename provided when launching a file using blender
function b() {
    if [ "$(echo $1 | grep -q .blend)" ]; then
        -- blender $@
    else
        -- blender $1.blend "${@:2}"
    fi
}

# adds `.pur` if not present in the filename provided when launching a file using PureRef
function puref() {
    if [ "$(echo $1 | grep -q .pur)" ]; then
        -- PureRef $@
    else
        -- PureRef "$1.pur" "${@:2}"
    fi
}

