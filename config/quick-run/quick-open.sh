#!/bin/bash -i

source ~/.bash_aliases

# the default programs to execute…
DEFAULT_IDE="code-insiders"
DEFAULT_TERMINAL="i3-sensible-terminal"
DEFAULT_FILE_VIEWER="nemo"

# …and their display names
display_ide="Code"
display_terminal="Terminal"
display_files="Dateien"

# prompt the user
output=$(yad --class=pop-up --form \
    --field=Öffnen '' \
    --field=mit:CB $display_ide'!'$display_terminal'!'$display_files)

# abort if user closed the prompt
if [ "$?" != 0 ]; then
    exit 2
fi

# populate all necessary variables
i=0
while read -d '|' val; do
    if [ $i -eq 0 ]; then
        directory="$val"
    elif [ $i -eq 1 ]; then
        program="$val"
        break
    fi
    ((i++))
done <<< $(echo "$output")

# abort if user gave empty directory/ command
if [ -z "$directory" ]; then
    exit 3
fi

# opens given directory or lets the use choose when provided path is empty
function open_dir() {
    dir="$1"
    if [ -z "$dir" ]; then
        # let the user decide
        dir=$(zenity --file-selection --directory)
    fi
    if [ -z "$dir" ]; then
        # cancelled
        exit 4
    fi
    cd -- "$dir"
}

# extract the value of the command
inherent="${directory:1}"

# evaluate command (the first character)
case "${directory:0:1}" in

    # evaluate (e.g. an alias)
    'e')
        if [ -z "$inherent" ]; then
            exit 4
        fi
        eval -- "$inherent"
    ;;

    # open a directory in the home directory
    'h')
        cd ~
        open_dir "$inherent"
    ;;

    # open a directory in the code directory
    'c')
        cd ~/code
        open_dir "$inherent"
    ;;

    # open given directory
    '/')
        cd -- "$directory"
    ;;

    *)
        notify-send -u critical "provide a valid command or path"
        exit 1
    ;;

esac

# execute
case "$program" in

    $display_ide)
        $DEFAULT_IDE .
    ;;

    $display_terminal)
        $DEFAULT_TERMINAL .
    ;;

    $display_files)
        $DEFAULT_FILE_VIEWER .
    ;;

esac
