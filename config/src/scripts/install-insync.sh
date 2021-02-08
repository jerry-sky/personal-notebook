#!/bin/bash

printf "\n\033[1mInsync\nInstalling…\033[0m\n"
# add the Insync repository
sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys ACCAF35C

codename="$(cat /etc/os-release | perl -nle 'print $2 if /(VERSION_CODENAME\=)(.+)/g')"

sudo mkdir -p /etc/apt/sources.list.d/
cd /tmp
echo "deb http://apt.insync.io/mint $codename non-free contrib" > insync.list
sudo mv insync.list /etc/apt/sources.list.d/

printf "\n\033[1mInstalling…\033[0m\n"
sudo apt-get update
sudo apt-get install insync
