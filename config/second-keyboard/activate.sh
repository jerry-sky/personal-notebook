#!/bin/bash

git clone --depth 1 'https://github.com/robinuniverse/Keebie' tmp
mv tmp/keebie.py ./
sed -i '1s/.*/#!\/usr\/bin\/env python3/' keebie.py

rm -rf tmp

sudo apt-get install xdotool x11-utils
