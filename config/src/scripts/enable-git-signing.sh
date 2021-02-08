#!/bin/bash

printf "\033[1mGit GPG signing\nImporting the key from `key.gpg`…\033[0m\n"

gpg --import key.gpg

if [ "$?" != "0" ]; then
    echo "put the private GPG signing key in a file called `key.gpg`"
    exit 1
fi

key_id="$(LANG=C gpg --import key.gpg 2>&1 | head -n 1 | perl -nle 'print /(?<=key\s)[A-z0-9]{16}/g')"

if [ -z "$key_id" ]; then
    echo "error occurred — could not extract the key id; you may configure Git manually if the key itself has been imported successfully"
    exit 1
fi

printf "\033[1mConfiguring Git…\033[0m\n"
# configure Git
git config --global user.signingkey "$key_id"
git config --global commit.gpgSign true
git config --global tag.gpgSign true
