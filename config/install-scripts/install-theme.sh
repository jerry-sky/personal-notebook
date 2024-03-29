#!/bin/bash

printf "\n\033[1mInterface theme\nInstalling Materia GTK Theme…\033[0m\n"

# install the base theme
sudo apt-get install materia-gtk-theme
# copy custom CSS into the installed GTK dark version of this theme suite
cur_dir="${BASH_SOURCE%/*}"
sudo cp "$cur_dir"/../../config-files/cinnamon/cinnamon.style -t "/usr/share/themes/Materia-dark/cinnamon/cinnamon.css"

printf "\n\033[1mInstalling icon theme…\033[0m\n"
# install icon theme
cd /usr/share/icons
sudo git clone --depth 1 'https://github.com/keeferrourke/la-capitaine-icon-theme'
cd "$cur_dir"

printf "\n\033[1mConfiguring Cinnamon…\033[0m\n"
# load appropriate Cinnamon interface settings
dconf load / < "$cur_dir/../../config-files/cinnamon/interface.conf"
