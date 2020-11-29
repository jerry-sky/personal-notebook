#!/usr/bin/env python3
from sys import stdin, exit
from config_entries.config_entries import config_entries
from config_entries.config_entry import Status
import pathlib
import os

EXIT_MESSAGE = '\033[3mbye\033[0m'

INSTALLED_CHARACTER = '\033[38;2;95;217;97m✓'
NOT_INSTALLED_CHARACTER = '\033[38;2;200;40;24m×'
UNKNOWN_STATUS_CHARACTER = '\033[38;2;242;234;78m?'


def print_available_options():

    command_length = 0
    for ce in config_entries:
        t = len(ce.shorthand)
        if t > command_length:
            command_length = len(ce.shorthand)

    print(command_length)

    print('\n\033[1mAvailable configs:\033[0m')
    for ce in config_entries:

        is_installed = NOT_INSTALLED_CHARACTER
        if ce.is_installed() == Status.Installed:
            is_installed = INSTALLED_CHARACTER
        elif ce.is_installed() == Status.Unknown:
            is_installed = UNKNOWN_STATUS_CHARACTER

        print('  \033[38;5;244m•\033[0m \033[38;5;248m[\033[0m \033[38;5;135;1m' + ce.shorthand + (' ' * (command_length - len(ce.shorthand)))\
            + '\033[0m \033[38;5;248m] '\
            + is_installed\
            + '\033[0m \033[38;5;244m→\033[0m \033[38;5;205m' + ce.description + '\033[0m')

    print()
    print(
        'Type the [ commands in brackets ] you want to execute splitted with whitespace or type `quit` to terminate this program.\n'\
        + 'Type `l`, or `list` to view all available commands.\n'
    )
    print(
        'Is installed status:\n',
        '  ' + INSTALLED_CHARACTER + ' — installed\n',
        '  ' + NOT_INSTALLED_CHARACTER + ' — not installed\n',
        '  ' + UNKNOWN_STATUS_CHARACTER + ' — unknown status\n'
        '\033[0m'
    )


if __name__ == "__main__":

    config_entries_shorthands = list(map(lambda x: x.shorthand, config_entries))

    _exit = False

    print_available_options()
    for line in stdin:

        commands = line.split()

        count = 0
        for command in commands:

            if command in config_entries_shorthands:
                index = config_entries_shorthands.index(command)
                try:
                    config_entries[index].execute()
                    count += 1
                except Exception as e:
                    print(command + ': ' + str(e))

            elif command in ['quit', 'q']:
                _exit = True
            elif command in ['list', 'l', 'a']:
                print_available_options()
            else:
                print(command + ': unknown command')

        if count > 0:
            print('\033[38;5;41m' + str(count)
                  + '\033[38;5;248m operation' + ('s' if count != 1 else '') + ' performed successfully\033[0m')
        if _exit:
            break

    exit(EXIT_MESSAGE)
