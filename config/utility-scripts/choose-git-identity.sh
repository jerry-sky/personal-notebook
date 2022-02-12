#!/bin/bash

grep="egrep sec"

all_keys=$(LANG=C gpg --list-secret-keys --keyid-format=long)

keys_count=$(echo "$all_keys" | $grep -c)

# print a list of all keys
for i in $(seq 1 $keys_count); do
    printf "\n\033[1m$i.\033[0m\n"
    echo "$all_keys" | $grep -m$i -A2 | tail -n3
done

# prompt user to choose one from the list
read -n1 chosen_no
printf '\n'

# extract the chosen key from the list
chosen=$(echo "$all_keys" | $grep -m$chosen_no -A2 | tail -n3)

# extract the ID
key_id=$(echo "$chosen" | perl -lne 'print $2 if /(rsa[0-9]{4}\/)([A-Z0-9]+)/g')

# extract the username and the email
user_id=$(echo "$chosen" | perl -lne 'print "$2;$4" if /(uid\s*\[.*\]\s+)(.+)(\s+<)(.*)(>)/g')

username=$(echo "$user_id" | perl -lne 'print $1 if /(.*)(;)(.*)/g')
email=$(echo "$user_id" | perl -lne 'print $3 if /(.*)(;)(.*)/g')

# configure Git
git config --global user.signingKey "$key_id"
git config --global commit.gpgSign true
git config --global tag.gpgSign true
git config --global user.name "$username"
git config --global user.email "$email"

git config --global --list
