#!/bin/bash

# pretty printing
function PRINT {
    echo
    printf "\033[1m%s\033[0m\n" "$@"
    echo
}


# don’t keep any of the temporary files
cd "/tmp"


PRINT "PROGRAMS"


PRINT "Basic utilities"
sudo apt install -y wget gpg apt-transport-https curl


PRINT "Google Chrome Stable"
wget "https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb"
sudo dpkg -i "google-chrome-stable_current_amd64.deb"


PRINT "Neovim"
sudo apt install -y neovim


PRINT "Git"
sudo apt install -y git


PRINT "GitHub CLI"
curl -fsSL https://cli.github.com/packages/githubcli-archive-keyring.gpg | sudo dd of=/usr/share/keyrings/githubcli-archive-keyring.gpg \
    && sudo chmod go+r /usr/share/keyrings/githubcli-archive-keyring.gpg \
    && echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/githubcli-archive-keyring.gpg] https://cli.github.com/packages stable main" | sudo tee /etc/apt/sources.list.d/github-cli.list > /dev/null \
    && sudo apt update \
    && sudo apt install gh -y

PRINT "Git and GitHub setup"
gh auth login



PRINT "Make some default directories"
mkdir -p ~/Code


PRINT "Download this notebook"
cd ~/Code
mkdir -p jerry-sky
cd jerry-sky
git clone "https://github.com/jerry-sky/personal-notebook"
