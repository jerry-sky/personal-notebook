#!/bin/bash

echo "Writing additional entries to .bashrc..."
cat ./.bashrc.part >> ~/.bashrc

echo "Attaching aliases..."
cp ./.bash_aliases ~/

echo "Attaching Redshift config file..."
if [ ! ( -d ~/.config ) ] ; then
  mkdir ~/.config
fi
cp ./redshift.conf ~/.config/

echo "Done."
