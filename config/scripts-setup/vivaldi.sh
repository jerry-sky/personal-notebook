#!/bin/bash

if [ -d /opt/vivaldi ] ; then
  sudo cp ./config-files/vivaldi/browser.html /opt/vivaldi/resources/vivaldi/
else
  printf "No /opt/vivaldi folder\n"
fi

printf " + copied Vivaldi browser.html file\n"
