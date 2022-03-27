#!/usr/bin/env python3
from sys import stdin, exit, argv
from helper.utilities import INSTALLED_COLOUR, UNKNOWN_STATUS_COLOUR, print_available_options, flatten_config_entries, execute_entry
from config_entries import config_entries

EXIT_MESSAGE = '\033[3mbye\033[0m'


config_entries_flat = flatten_config_entries(config_entries)


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

        print_available_options(config_entries)

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
                    UNKNOWN_STATUS_COLOUR +
                    '0 \033[38;5;248moperations performed'
                )

    # bye
    print(EXIT_MESSAGE)
    exit(0)
