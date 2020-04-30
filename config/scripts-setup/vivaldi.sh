#!/bin/bash

if [ -d /opt/vivaldi ] ; then
  sudo cp ./vivaldi/browser.html /opt/vivaldi/resources/vivaldi/
else
  _print_error "No /opt/vivaldi folder"
fi

printf " + copied Vivaldi browser.html file\n"
