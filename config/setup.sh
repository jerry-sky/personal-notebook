#!/bin/bash

echo "Writing additional entries to .bashrc..."
cat ./.bashrc.part >> ~/.bashrc

echo "Attaching aliases..."
cp ./.bash_aliases ~/

echo "Done."
