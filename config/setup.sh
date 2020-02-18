#!/bin/bash

_exit_message="bye"
_cleanup(){
  tput cup $(tput lines) 0
  printf "\n\n\033[1m$_exit_message\033[0m\n"
  tput cnorm
}
trap _cleanup EXIT

# all config entries
config_entries=(\
  "append a few entires to .bashrc"\
  "swap Control_R and Menu keys"\
  "bash aliases"\
  "copy Redshift config file"\
  "copy Vivaldi browser.html file"\
  "copy nvim init file"\
  "copy java formatter file"\
  "copy Menu icon file"
)

# default entires' values
config_entries_values=(\
  0\
  0\
  1\
  1\
  1\
  1\
  1\
  1\
)

_config_entries_length=${#config_entries[@]}

# current selection position
_cursor_position=0

# invert entries' values
_inverse_selection() {
  for ((i = 0; i < ${#config_entries_values[@]}; i++)); do
    if (( config_entries_values[$i] == 0 )); then
      config_entries_values[$i]=1
    else
      config_entries_values[$i]=0
    fi
  done
}

# clear selection
_clear_selection() {
  for ((i = 0; i < ${#config_entries_values[@]}; i++)); do
    config_entries_values[$i]=0
  done
}

# print commands
printf "\n"
printf " \033[38;5;135;1mw\033[0m       \033[38;5;247mmove up\033[0m\n"
printf " \033[38;5;135;1ms\033[0m       \033[38;5;247mmove down\033[0m\n"
printf " \033[38;5;135;1mSpace\033[0m   \033[38;5;247mtoggle selected item\033[0m\n"
printf " \033[38;5;135;1mi\033[0m       \033[38;5;247minverse selection\033[0m\n"
printf " \033[38;5;135;1mc\033[0m       \033[38;5;247mclear selection\033[0m\n"
printf " \033[38;5;135;1ma\033[0m       \033[38;5;247mapply\033[0m\n"
printf " \033[38;5;135;1mq\033[0m       \033[38;5;247mabort\033[0m\n"
printf "\n"

# apply selected config entries
_run_config_entries() {

  tput cup $(tput lines) 0

  for ((i = 0; i < ${#config_entries[@]}; i++)); do
    if (( config_entries_values[$i] == 1 )); then
      echo $([ "${config_entries[$i]}" = "${config_entries[0]}" ] && echo merdas)
      case "${config_entries[$i]}" in
        "${config_entries[0]}" ) bash "./scripts/bashrc.sh" ;;
        "${config_entries[1]}" ) bash "./scripts/key-remap.sh" ;;
        "${config_entries[2]}" ) bash "./scripts/bash-aliases.sh" ;;
        "${config_entries[3]}" ) bash "./scripts/redshift.sh" ;;
        "${config_entries[4]}" ) bash "./scripts/vivaldi.sh" ;;
        "${config_entries[5]}" ) bash "./scripts/nvim.sh" ;;
        "${config_entries[6]}" ) bash "./scripts/java-formatter.sh" ;;
        "${config_entries[7]}" ) bash "./scripts/menu-icon.sh" ;;
      esac
    fi
  done

}

tput civis
tput sc

while [[ 1 ]]; do

  tput sc
  case "$_input" in
    [wW] ) (( _cursor_position > 0 )) && (( _cursor_position-- )) ;;
    [sS] ) (( _cursor_position < _config_entries_length-1 )) && (( _cursor_position++ )) ;;
    [iI] ) _inverse_selection ;;
    [cC] ) _clear_selection ;;
    [aA] ) _run_config_entries && break ;;
    [qQ] ) _exit_message="abort" && break ;;
  esac

  for ((i = 0; i < ${#config_entries[@]}; i++)); do
    tput cuf 4
    if (( ${config_entries_values[$i]} == 1 )); then
      printf "\033[38;5;247m[\033[0m+\033[38;5;247m]\033[0m"
    else
      printf "\033[38;5;247m[\033[0m \033[38;5;247m]\033[0m"
    fi
    printf "\033[38;5;205m ${config_entries[$i]}\033[0m\n"
  done

  tput rc
  tput sc
  i=0
  while [[ $i < $_config_entries_length ]]; do
    if (( i == $_cursor_position )); then
      printf -- '->'
    else
      printf "  "
    fi
    tput cud1
    (( i++ ))
  done
  tput rc

  read -n 1 -s -d '' _input

  if [[ -z "${_input// }" ]]; then
    if (( config_entries_values[$_cursor_position] == 0 )); then
      config_entries_values[$_cursor_position]=1
    else
      config_entries_values[$_cursor_position]=0
    fi
  fi

done
