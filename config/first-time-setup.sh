#!/bin/bash

# the installation commands
APT="sudo apt-get -y"
APTI="$APT install"
DPKG="sudo dpkg -i"

###

# don’t keep any of the temporary files
cd "/tmp"
cur_dir="__first-time-setup"
mkdir -p "$cur_dir"
cd "$cur_dir"
cur_dir="/tmp/$cur_dir"

### Install programs

printf "\033[1mPrograms\n\nGit\nInstalling…\033[0m\n"

# install Git
$APTI "git"
# configure git
printf "\n\033[1mConfiguring…\033[0m\n"
printf "\033[1mProvide your GitHub username:\033[0m\n"
read username
git config --global user.name "$username"
printf "\033[1mProvide your GitHub email:\033[0m\n"
read email
git config --global user.email "$email"
## install password manager
$APTI "libsecret-1-0" "libsecret-1-dev"
cd /usr/share/doc/git/contrib/credential/libsecret
sudo make
if [ $? != "0" ]; then
    exit 1
fi
cd "$cur_dir"
## configure git to use the password manager
git config --global credential.helper /usr/share/doc/git/contrib/credential/libsecret/git-credential-libsecret
## try to download a private repository
## this is needed to invoke password input so a newly generated access token can be used and remembered
printf "\nNow, we can download a private repository so Git can ask you for your password. However, instead of your password provide a newly generated GitHub access token that you can attain here: https://github.com/settings/tokens/new\n"
git clone 'https://github.com/jerry-sky/personal-notebook-private'
printf "\n\033[1mRemember to add commit and tag signing after you regain access to your GPG keys.\n"

# download Chrome
printf "\n\033[1mGoogle Chrome Stable\nDownloading…\033[0m\n"
wget "https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb"
# install Chrome
printf "\033[1mInstalling…\033[0m\n"
$DPKG "google-chrome-stable_current_amd64.deb"

# install VS Code (Insiders version)
printf "\n\033[1mVS Code Insiders\nInstalling…\033[0m\n"
## add the apt repository
wget -qO- https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > packages.microsoft.gpg
sudo install -o root -g root -m 644 packages.microsoft.gpg /etc/apt/trusted.gpg.d/
sudo sh -c 'echo "deb [arch=amd64,arm64,armhf signed-by=/etc/apt/trusted.gpg.d/packages.microsoft.gpg] https://packages.microsoft.com/repos/code stable main" > /etc/apt/sources.list.d/vscode.list'
$APT update
## install the program
$APTI code-insiders

### Make some directories

mkdir ~/code
mkdir ~/notebooks

# download the notebook repositories
printf "\n\033[1mDownloading the notebook repositories…\033[0m\n"
cd ~/notebooks
git clone "https://github.com/jerry-sky/personal-notebook"
git clone "https://github.com/jerry-sky/academic-notebook"
