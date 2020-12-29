#!/bin/bash

# default arguments
input_file="$1"
lang="en-GB"
author="Jerry Sky"

# read arguments
while [[ "$#" -gt 0 ]]; do
    case $1 in
        -l|--lang) lang="$2"; shift ;;
        -A|--author) author="$2"; shift ;;
        *) input_file="$1" ;;
    esac
    shift
done

# input file necessary
if [ -z "$input_file" ]; then
    echo "input file argument necessary"
    exit 1
fi

# get the title from the first line
title="$(head -n1 $input_file | tail -c+3)"

# look for the date and the description
# date and description can be between lines 2 and 5
date=""
description=""
lines_to_delete=1
for i in $(seq 2 5); do
    line=$(head -n"$i" "$input_file" | tail -n1)

    # read the date of the document
    if [ -z "$date" ]; then
        date=$(echo "$line" | grep -E -o '[0-9]{4}\-[0-9]{2}\-[0-9]{2}')
        if [ ! -z "$date" ]; then
            lines_to_delete="$i"
        fi
    fi

    # read the description of the document
    if [ -z "$description" ]; then
        description=$(echo "$line" | grep -E -o '\*(\w|\-|\s|\.|\,)+\*')
        # remove the wrapper characters
        description="${description:1}"
        description="${description%?}"
        if [ ! -z "$description" ]; then
            lines_to_delete="$i"
        fi
    fi
done

# n+1 lines to delete (`tail -n1` does nothing)
((lines_to_delete++))
# remove lines which we are going to generate the front matter from
echo "$(tail -n +$lines_to_delete $input_file)" > "$input_file"

# compose the metadata block
metadata="---
lang: '$lang'
title: '$title'
author: '$author'
"
if [ ! -z "$date" ]; then
    metadata="$metadata""date: '$date'
"
fi

if [ ! -z "$description" ]; then
    metadata="$metadata""description: '$description'
"
fi

# end the metadata block and add a horizontal line
metadata="$metadata---

---
"

# save changes
echo "$metadata""$(cat $input_file)" > "$input_file"
