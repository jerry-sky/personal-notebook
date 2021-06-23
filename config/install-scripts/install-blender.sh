#!/bin/bash

printf "\n\033[1mBlender\033[0m\n"

ftp_url="https://ftp.nluug.nl/pub/graphics/blender/release/"

# get the remote directory of the latest Blender version
rem_dir="$(curl -s $ftp_url | perl -nle 'print $& if /Blender\d\.\d{2}/g' | tail -n 1)"

# get the name of the remote archive
rem_arc="$(curl -s -L $ftp_url$rem_dir | perl -nle 'print $& if /blender\-\d+\.\d+\.\d+\-linux64\.tar\.xz/g' | tail -n 1)"

printf "\n\033[1mDownloading…\033[0m\n"
echo "Archive: $rem_arc"

if [ -z "$rem_arc" ]; then
    echo 'error: couldn’t download Blender — extracted filename is empty'
    exit 1
fi

# download the archive
archive="/tmp/blender.tar.xz"
curl --output "$archive" "$ftp_url$rem_dir/$rem_arc"

printf "\n\033[1mInstalling…\033[0m\n"
# unpack the archive
cd "/tmp"
unpacked="/tmp/${rem_arc%\.tar\.xz}"
tar -xf "$archive"
# copy the program (application) metadata
sudo cp "$unpacked/blender.desktop" "/usr/share/applications/blender.desktop"
sudo update-desktop-database /usr/share/applications
# copy the program data
sudo mkdir -p "/opt/blender"
sudo cp -r -- $unpacked/* "/opt/blender/"
# link the executable
cd "/usr/bin"
sudo ln -fs "/opt/blender/blender" "blender"
