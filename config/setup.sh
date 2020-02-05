#!/bin/bash

## Simple bash prompt functionality
# the function output
REPLY_=0
# the prompt message
PROMPT_MESSAGE_="Are you sure? "
# function body
_prompt() {
  read -p "$PROMPT_MESSAGE_" -n 1 -r
  if [[ $REPLY =~ ^[Yy]$ ]] ; then
    REPLY_=1
    printf " -> \033[32mYes\033[0m"
  else
    REPLY_=0
    printf " -> \033[31mNo\033[0m"
  fi
  printf '\n===\n'
}

## Add colour to default messages
_print_message() {
  printf "\033[36m$1\033[0m\n"
}

## Add colour to error messages
_print_error() {
  printf "\033[31m$1\033[0m\n"
}

echo '---'

## Config files to copy/setup

_print_message "Writing additional entries to .bashrc..."
_prompt
(( REPLY_ )) && \
  cat ./.bashrc.part >> ~/.bashrc

_print_message "Do you want to switch the Control_R and Menu keys?\nIt is advised to switch these keys when on a laptop without a dedicated Menu key."
_prompt
(( REPLY_ )) && \
  cat ./.key_remap >> ~/.bashrc

_print_message "Attaching aliases..."
_prompt
(( REPLY_ )) && \
  cp ./.bash_aliases ~/

_print_message "Attaching Redshift config file..."
_prompt
if (( REPLY_ )) ; then
  if [ ! -d ~/.config ] ; then
    mkdir ~/.config
  fi
  cp ./redshift.conf ~/.config/
fi

_print_message "Attaching Vivaldi browser.html file..."
_prompt
if (( REPLY_ )) ; then
  if [ -d /opt/vivaldi ] ; then
    sudo cp ./vivaldi/browser.html /opt/vivaldi/resources/vivaldi/
  else
    _print_error "No /opt/vivaldi folder"
  fi
fi

_print_message "Attaching NVim init file..."
_prompt
if (( REPLY_ )) ; then
  if [ -d ~/.config/nvim ] ; then
    cp ./nvim/init.vim ~/.config/nvim/
  else
    _print_error "No ~/.config/nvim directory"
  fi
fi

_print_message "Attaching Java Formatter config file..."
_prompt
if (( REPLY_ )) ; then
  cp ./java-formatter.xml ~/.config/
fi

_print_message "Attaching Menu icon file..."
_prompt
if (( REPLY_ )) ; then
  sudo cp ./menu-icon.png /usr/share/icons/
fi

printf "\nDone.\n"