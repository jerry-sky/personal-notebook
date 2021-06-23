#!/bin/bash

printf "\033[1mUnity\n\nInstalling Unity Hub…\033[0m\n\n"

# download Unity Hub AppImage
sudo curl -L --output '/opt/UnityHub.AppImage' 'https://public-cdn.cloud.unity3d.com/hub/prod/UnityHub.AppImage'
sudo chmod +x /opt/UnityHub.AppImage

# create a link to the executable
sudo ln -fs /opt/UnityHub.AppImage /usr/bin/unity-hub

# create a desktop entry
sudo bash -c 'cat > /usr/share/applications/unity-hub.desktop <<EOF
[Desktop Entry]
Type=Application
Exec=/usr/bin/unity-hub
Icon=/usr/bin/unity-hub
NoDisplay=false
Terminal=false
Hidden=false
Name=Unity Hub
EOF'

sudo update-desktop-database /usr/share/applications

# install .NET
printf '\n\033[1mInstalling .NET SDK and runtime…\033[0m\n'

wget https://packages.microsoft.com/config/ubuntu/20.10/packages-microsoft-prod.deb -O /tmp/packages-microsoft-prod.deb
sudo dpkg -i /tmp/packages-microsoft-prod.deb

sudo apt-get update; \
    sudo apt-get install -y apt-transport-https && \
    sudo apt-get update && \
    sudo apt-get install -y dotnet-sdk-5.0

# install Mono
printf '\n\033[1mInstalling Mono…\033[0m\n'
sudo apt-get install -y gnupg ca-certificates
sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys 3FA7E0328081BFF6A14DA29AA6A19B38D3D831EF
echo "deb https://download.mono-project.com/repo/ubuntu stable-focal main" | sudo tee /etc/apt/sources.list.d/mono-official-stable.list
sudo apt-get update

sudo apt-get install -y mono-complete
