#!/usr/bin/env python3
from sys import stdin, exit, argv
from config_entries import config_entries, config_entries_flat
from model import Status, ConfigEntry
import os

EXIT_MESSAGE = '\033[3mbye\033[0m'

INSTALLED_COLOUR = '\033[38;2;95;217;97m'
INSTALLED_CHARACTER = INSTALLED_COLOUR + '✓'
NOT_INSTALLED_COLOUR = '\033[38;2;200;40;24m'
NOT_INSTALLED_CHARACTER = NOT_INSTALLED_COLOUR + '×'
UNKNOWN_STATUS_COLOUR = '\033[38;2;242;234;78m'
UNKNOWN_STATUS_CHARACTER = UNKNOWN_STATUS_COLOUR + '?'

INSTALLED = '\033[1minstalled\033[0m'
ABORTED = '\033[1maborted\033[0m'
UNINSTALLED = '\033[1muninstalled\033[0m'
UNCHANGED = '\033[1munchanged\033[0m'

# first see which command is the longest to adjust the space padding for the other commands
COMMAND_LENGTH = max([len(ce.shorthand) for ce in config_entries_flat])


def print_available_options():
    '''
    Prints all available entries as a list.
    '''

    # print available config entries
    print('\n\033[1mAvailable configs:\033[0m\n')
    for group in config_entries:
        print(group['name'])
        for ce in group['list']:
            print_entry(ce)

        print()

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


def print_entry(ce: ConfigEntry, single=False) -> None:
    '''
    Prints all information about given entry.
    '''
    # check if the entry has been installed
    is_installed = NOT_INSTALLED_CHARACTER
    if ce.is_installed == Status.Installed:
        is_installed = INSTALLED_CHARACTER
    elif ce.is_installed == Status.Unknown:
        is_installed = UNKNOWN_STATUS_CHARACTER

    if single:
        print(
            '\033[0;38;5;205m' + ce.description + '\033[0m'
        )
    else:
        # print its command, install status and short description
        print(
            '  \033[38;5;244m•\033[0m \033[38;5;248m[\033[0m \033[38;5;135;1m'
            + ce.shorthand
            + (' ' * (COMMAND_LENGTH - len(ce.shorthand)))
            + '\033[0m \033[38;5;248m] '
            + is_installed
            + '\033[0m \033[38;5;244m→\033[0m \033[38;5;205m'
            + ce.description + '\033[0m')


def execute_entry(ce: ConfigEntry) -> bool:
    '''
    Requires an explicit input from the user based on the current state
    of the given Config Entry.

    The user needs to choose between options to:
    - install,
    - uninstall,
    - reinstall,
    - do nothing
    with the given Config Entry.

    Availability of these options depends on each Config Entry.
    '''

    reinstall = 'reinstall'
    install = 'install'
    uninstall = 'uninstall'
    nothing = 'nothing'

    available_options = [nothing, install]

    if not ce.is_immutable:
        available_options += [reinstall, uninstall]

    # print the status of the config entry
    print_entry(ce, single=True)
    # ask the user what he wants to do with the entry
    print('\033[1mChoose between:')
    for o in available_options:
        print('  \033[4m' + o[:2] + '\033[0;1m' + o[2:])

    # take only first two letters from the names of the options
    # — user has to input these two letters of their chosen option
    available_options_cmds = [x[:2] for x in available_options]
    cmd_index = 0
    x = input()
    while x not in available_options_cmds:
        x = input('\033[0mplease choose one of the options listed above\033[1m\n')

    cmd_index = available_options_cmds.index(x)
    chosen_option = available_options[cmd_index]

    # clean up
    print('\033[0m', end='')

    if chosen_option == install:
        ce.install()
        return True
    elif chosen_option == reinstall:
        ce.uninstall()
        ce.install()
        return True
    elif chosen_option == uninstall:
        ce.uninstall()
        return True

    return False


if __name__ == '__main__':

    if '-i' in argv:
        # interactive mode
        print('\033[1mInteractive mode')

        for group in config_entries:
            print(group['name'])
            for ce in group:
                # for each entry give the user an option to do nothing,
                # uninstall, reinstall, or install
                execute_entry(ce)

    else:
        # list mode

        # premap all entries with their respective shorthands
        config_entries_shorthands = list(
            map(lambda x: x.shorthand, config_entries_flat))

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
                    count += execute_entry(config_entries_flat[index])

                elif command in ['list', 'l', 'a']:
                    # user wants to see all available entries
                    print_available_options()

                else:
                    # unrecognized command given
                    print(command + ': unknown command')

            if count > 0:
                # indicate number of successfully ran operations
                print(INSTALLED_COLOUR + str(count)
                      + '\033[38;5;248m operation' + ('s' if count != 1 else '') + ' performed successfully\033[0m')
            else:
                print(
                    UNKNOWN_STATUS_COLOUR + '0 \033[38;5;248moperations performed'
                )

    # bye
    print(EXIT_MESSAGE)
    exit(0)
