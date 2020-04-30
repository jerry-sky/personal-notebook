#!/bin/bash

if [ ! -d ~/.config ]; then
  mkdir ~/.config
fi
cp ./redshift.conf ~/.config/

printf " + copied Redshift config file\n"
