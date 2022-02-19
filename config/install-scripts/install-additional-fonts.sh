#!/bin/bash

GOOGLE_FONTS="https://fonts.google.com/download?family="


function download_font_family {
    address="$1"
    name="$2"

    cd /tmp
    printf "\n\033[1mDownloading and installing $name…\033[0m\n"
    curl -L --output "$name".zip "$address"
    unzip "$name".zip -d "$name"
    rm "$name".zip
    sudo mv "$name" /usr/share/fonts/truetype/
}


printf "\n\033[1mAdditional font packs\033[0m\n"

download_font_family "${GOOGLE_FONTS}Fira%20Code" "Fira Code"
download_font_family "${GOOGLE_FONTS}Fira%20Sans" "Fira Sans"
download_font_family "${GOOGLE_FONTS}Merriweather" "Merriweather"
download_font_family "${GOOGLE_FONTS}Merriweather%20Sans" "Merriweather Sans"
download_font_family "https://use.fontawesome.com/releases/v6.0.0/fontawesome-free-6.0.0-desktop.zip" "Font Awesome"
