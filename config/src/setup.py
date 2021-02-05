#!/usr/bin/env python3
from sys import stdin, exit, argv
from config.config_entries import config_entries
from config.config_entry import Status, ConfigEntry
import os

EXIT_MESSAGE = '\033[3mbye\033[0m'

INSTALLED_CHARACTER = '\033[38;2;95;217;97m✓'
NOT_INSTALLED_CHARACTER = '\033[38;2;200;40;24m×'
UNKNOWN_STATUS_CHARACTER = '\033[38;2;242;234;78m?'

INSTALLED = '\033[1minstalled\033[0m'
ABORTED = '\033[1maborted\033[0m'
UNINSTALLED = '\033[1muninstalled\033[0m'
UNCHANGED = '\033[1munchanged\033[0m'

# first see which command is the longest to adjust the space padding for the other commands
COMMAND_LENGTH = max([len(ce.shorthand) for ce in config_entries])


def print_available_options():
    '''
    Prints all available entries as a list.
    '''

    # print available config entries
    print('\n\033[1mAvailable configs:\033[0m')
    for ce in config_entries:
        print_entry(ce)

    print(
        '\nType the [ commands in brackets ] you want to execute splitted with whitespace or input `^D` to terminate this program.\n'
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
    '''
    Prints all information about given entry.
    '''
    # check if the entry has been installed
    is_installed = NOT_INSTALLED_CHARACTER
    if ce.is_installed == Status.Installed:
        is_installed = INSTALLED_CHARACTER
    elif ce.is_installed == Status.Unknown:
        is_installed = UNKNOWN_STATUS_CHARACTER
    # print its command, install status and short description
    print('  \033[38;5;244m•\033[0m \033[38;5;248m[\033[0m \033[38;5;135;1m' + ce.shorthand + (' ' * (COMMAND_LENGTH - len(ce.shorthand)))
          + '\033[0m \033[38;5;248m] '
            + is_installed
            + '\033[0m \033[38;5;244m→\033[0m \033[38;5;205m' + ce.description + '\033[0m')


def execute_entry(ce: ConfigEntry) -> bool:
    '''
    Executes the function(s) provided by the given entry.
    '''
    try:
        ce.execute()
        return True

    except Exception as e:
        print(command + ': ' + str(e))
        return False


def ask_for_confirmation(msg: str) -> bool:
    '''
    Requires an explicit binary input from the user.

    The user needs to input either `y` or `n`.
    '''
    y = 'y'
    n = 'n'

    print(msg + ': y|n')

    i = ''
    while i not in [y, n]:
        try:
            i = input()  # [:-1] # remove the newline at the end
        except EOFError:
            print(EXIT_MESSAGE)
            exit(0)

    return i == y


if __name__ == '__main__':

    if '-i' in argv:
        # interactive mode
        print('\033[1mInteractive mode')

        for ce in config_entries:
            # for each entry:
            # print its information
            print_entry(ce)

            # give user a choice to install/uninstall/reinstall the entry
            if ce.is_installed == Status.NotInstalled:
                # entry is not installed
                if ask_for_confirmation('Install?'):
                    print(INSTALLED)
                    execute_entry(ce)
                else:
                    print(ABORTED)

            elif ce.is_installed == Status.Installed:
                # entry is installed
                if ask_for_confirmation('Keep installed?'):
                    print(UNINSTALLED)
                    execute_entry(ce)
                else:
                    print(ABORTED)

            else:  # Status.Unknown
                if ask_for_confirmation('Keep entry’s state?'):
                    print(UNCHANGED)
                    execute_entry(ce)
                else:
                    print(ABORTED)

    else:
        # list mode

        # premap all entries with their respective shorthands
        config_entries_shorthands = list(
            map(lambda x: x.shorthand, config_entries))

        print_available_options()

        for line in stdin:
            # analyze every line of the standard input

            commands = line.split()

            count = 0
            for command in commands:
                # for every command:

                if command in config_entries_shorthands:
                    # the command refers to one of the entries on the list
                    index = config_entries_shorthands.index(command)
                    count += execute_entry(config_entries[index])

                elif command in ['list', 'l', 'a']:
                    # user wants to see all available entries
                    print_available_options()

                else:
                    # unrecognized command given
                    print(command + ': unknown command')

            if count > 0:
                # indicate number of successfully ran operations
                print('\033[38;5;41m' + str(count)
                      + '\033[38;5;248m operation' + ('s' if count != 1 else '') + ' performed successfully\033[0m')

    # bye
    print(EXIT_MESSAGE)
    exit(0)
