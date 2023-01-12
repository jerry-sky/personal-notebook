#!/bin/bash

sudo mkdir -p /opt/utility-scripts
cd /opt/utility-scripts

sudo git clone https://github.com/PRATAP-KUMAR/ubuntu-gdm-set-background --depth 1 TMP
sudo cp TMP/ubuntu-gdm-set-background ./ubuntu-gdm-set-background.sh
sudo rm -r TMP
sudo chmod +x ubuntu-gdm-set-background.sh
