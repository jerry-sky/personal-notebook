#!/usr/bin/env python3
from sys import stdin, exit, argv
from config_entries.config_entries import config_entries
from config_entries.config_entry import Status, ConfigEntry
import pathlib
import os

EXIT_MESSAGE = '\033[3mbye\033[0m'

INSTALLED_CHARACTER = '\033[38;2;95;217;97m✓'
NOT_INSTALLED_CHARACTER = '\033[38;2;200;40;24m×'
UNKNOWN_STATUS_CHARACTER = '\033[38;2;242;234;78m?'

INSTALLED = '\033[1minstalled\033[0m'
ABORTED = '\033[1maborted\033[0m'
UNINSTALLED = '\033[1muninstalled\033[0m'
REINSTALLED = '\033[1m(re)installed\033[0m'

# first see which command is the longest to adjust the space padding for the other commands
COMMAND_LENGTH = max([len(ce.shorthand) for ce in config_entries])


def print_available_options():

    # print available config entries
    print('\n\033[1mAvailable configs:\033[0m')
    for ce in config_entries:
        print_entry(ce)

    print(
        '\nType the [ commands in brackets ] you want to execute splitted with whitespace or type `quit` to terminate this program.\n'
        + 'Type `l`, or `list` to view all available commands.\n'
    )
    print(
        'Is installed status:\n',
        '  ' + INSTALLED_CHARACTER + ' — installed\n',
        '  ' + NOT_INSTALLED_CHARACTER + ' — not installed\n',
        '  ' + UNKNOWN_STATUS_CHARACTER + ' — unknown status\n'
        '\033[0m'
    )


def print_entry(ce: ConfigEntry) -> None:
    # check if the entry has been installed
    is_installed = NOT_INSTALLED_CHARACTER
    if ce.is_installed() == Status.Installed:
        is_installed = INSTALLED_CHARACTER
    elif ce.is_installed() == Status.Unknown:
        is_installed = UNKNOWN_STATUS_CHARACTER
    # print its command, install status and short description
    print('  \033[38;5;244m•\033[0m \033[38;5;248m[\033[0m \033[38;5;135;1m' + ce.shorthand + (' ' * (COMMAND_LENGTH - len(ce.shorthand)))
          + '\033[0m \033[38;5;248m] '
            + is_installed
            + '\033[0m \033[38;5;244m→\033[0m \033[38;5;205m' + ce.description + '\033[0m')


def entry_execute(ce: ConfigEntry) -> bool:
    try:
        ce.execute()
        return True
    except Exception as e:
        print(command + ': ' + str(e))
        return False


def ask_for_input() -> str:
    i = ''
    try:
        i = input()
    except EOFError:
        print(EXIT_MESSAGE)
        exit(0)
    return i

if __name__ == '__main__':

    config_entries_shorthands = list(
        map(lambda x: x.shorthand, config_entries))

    _exit = False

    if '-i' in argv:
        # interactive mode
        print('\033[1mInteractive mode')

        for ce in config_entries:

            print_entry(ce)
            if ce.is_installed() == Status.NotInstalled:
                # entry is not installed
                print('press RETURN to install')
                line = ask_for_input()
                if line == '':
                    print(INSTALLED)
                    entry_execute(ce)
                else:
                    print(ABORTED)
            elif ce.is_installed() == Status.Installed:
                # entry is installed
                print('type u and press RETURN to uninstall')
                line = ask_for_input()
                if line == 'u':
                    print(UNINSTALLED)
                    entry_execute(ce)
                else:
                    print(ABORTED)
            else: # Status.Unknown
                print('type i and press RETURN to (re)install')
                line = ask_for_input()
                if line == 'i':
                    print(REINSTALLED)
                    entry_execute(ce)
                else:
                    print(ABORTED)

    else:
        print_available_options()

        for line in stdin:
            commands = line.split()

            count = 0
            for command in commands:

                if command in config_entries_shorthands:
                    index = config_entries_shorthands.index(command)
                    count += entry_execute(config_entries[index])

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

    print(EXIT_MESSAGE)
    exit(0)
