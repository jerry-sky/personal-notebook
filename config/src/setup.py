#!/usr/bin/env python3
from sys import stdin, exit
from config_entries.config_entries import config_entries
import pathlib
import os

EXIT_MESSAGE = '\033[3mbye\033[0m'


def print_available_options():

    print('\n\033[1mAvailable configs:\033[0m')
    for ce in config_entries:
        print('  \033[38;5;244m×\033[0m \033[38;5;248m[\033[0m \033[38;5;135;1m' + ce.shorthand +
              '\033[0m \033[38;5;248m] \033[38;5;244m→\033[0m \033[38;5;205m' + ce.description + '\033[0m')

    print()
    print(
        'Type the [ commands in brackets ] you want to execute splitted with whitespace or type `quit` to terminate this program.\n')


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
