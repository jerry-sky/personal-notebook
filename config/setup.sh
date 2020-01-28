#!/bin/bash

echo "Writing additional entries to .profile..."
cat ./.profile.part >> ~/.profile

echo "Attaching aliases..."
cp ./.aliases ~/

echo "Done. Apply changes by restarting or by executing `. ~/.profile` "
