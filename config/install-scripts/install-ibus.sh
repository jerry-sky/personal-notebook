#/bin/bash

printf "\n\033[1miBus, iBus-Anthy, iBus-Hangul\033[0m\n"

printf "\n\033[1mInstalling…\033[0m\n"
# install iBus and the Japanese and Korean iBus packages
sudo apt-get install -y ibus ibus-anthy ibus-hangul

# install the program that resolves necessary language packages and applies
# language settings system-wide
sudo apt-get install -y language-selector-gnome

# configure taskbar icon colour
/usr/bin/gsettings set org.freedesktop.ibus.panel xkb-icon-rgba "#c0c0c0"

# run the program
zenity --question --text "Do you want to run the language selector program now?"
if [ "$?" -eq "0" ]; then
    nohup gnome-language-selector &>/dev/null &
fi
