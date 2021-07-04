#!/bin/bash

archive=tex.tar.gz

printf '\033[1mTeX Live\nInstalling…\033[0m\n'
cd /tmp
mkdir __texlive
cd __texlive
# download
wget https://mirror.ctan.org/systems/texlive/tlnet/install-tl-unx.tar.gz -O $archive
# extract
tar -zxvf $archive --strip-components=1
# run the script
sudo ./install-tl

# get version
version=$(head -n1 release-texlive.txt | perl -ne 'print $& if /[0-9]{4}/g')

# add to PATH
printf '\n# TeX Live\nPATH="/usr/local/texlive/'$version'/bin/x86_64-linux:$PATH"\n' >> ~/.bashrc
