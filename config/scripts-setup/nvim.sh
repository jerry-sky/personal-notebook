#!/bin/bash

if [ -d ~/.config/nvim ] ; then
    cp ./config-files/nvim/init.vim ~/.config/nvim/
  else
    printf "No ~/.config/nvim directory\n"
fi

printf " + copied NVim init file\n"
