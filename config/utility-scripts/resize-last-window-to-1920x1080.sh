#!/bin/bash

# check if the `wmctrl` program is installed
if [ ! "$(command -v wmctrl)" ]; then
    echo "wmctrl is not installed"
    exit
fi

# get the list of open windows
wins_list="$(wmctrl -l -G)"
# calc number of open windows
num_wins="$(printf "$wins_list\n" | wc -l)"
# also calc the width of the max number
num_wins_width="${#num_wins}"

# print all available options
for i in $(seq 1 $num_wins); do
    printf "\033[1m$i.\033[0m"
    # adjust the whitespace accordingly
    cur_width="${#i}"
    ((offset=num_wins_width-cur_width+1))
    printf "%0.s " $(seq 1 $offset)
    printf "$wins_list" | head -n"$i" | tail -n1
done

printf "\n\033[1mType the number of the window to resize\033[0m\n"

read tmp
if [ "1" -le "$tmp" -a "$tmp" -le "$num_wins" ] 2>/dev/null; then
    # get the id of the window (substitution)
    # resize the window by using the id (-i option)
    wmctrl -i -r "$(printf "$wins_list" | head -n"$tmp" | tail -n1 | cut -d' ' -f1)" -e "0,-1,-1,1920,1080"
    echo "resized"
else
    echo "cancelled"
fi