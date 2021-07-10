#!/bin/bash

printf "\033[1mAdding new Git identity\033[0m\n"

printf "Generating new GPG key set\033[1m\nImportant: generate key of size >=4096\033[0m\n"
gpg --full-generate-key

# get the generated key ID
id=$(LANG=C gpg --list-secret-keys --keyid-format=long | tail -n5 | perl -nle 'print $2 if /(sec\s*rsa[0-9]{4}\/)([A-Z0-9]+)/g')

printf "\033[1mKey generated.\nAfter you hit enter, you will be presented with the public key you can copy.\033[0m\n"
read -n1
gpg --armor --export $id
