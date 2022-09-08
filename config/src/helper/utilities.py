from model import ConfigEntries, Status, ConfigEntry


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


def max_shorthand_length(config_entries: ConfigEntries):
    '''
    Get the maximum length of all shorthands across all config entries.
    '''
    return max([len(ce.shorthand) for ce in flatten_config_entries(config_entries)])


def flatten_config_entries(config_entries: ConfigEntries):
    return [ce for group in config_entries for ce in group.list]


def print_available_options(config_entries: ConfigEntries):
    '''
    Prints all available entries as a list.
    '''

    command_length = max_shorthand_length(config_entries)

    # print available config entries
    print('\n\033[1mAvailable configs:\033[0m\n')
    for group in config_entries:
        print(group.name)
        for ce in group.list:
            print_entry(ce, command_length=command_length)

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


def print_entry(config_entry: ConfigEntry, command_length=0, single=False) -> None:
    '''
    Prints all information about given entry.
    '''
    # check if the entry has been installed
    is_installed = NOT_INSTALLED_CHARACTER
    if config_entry.is_installed == Status.Installed:
        is_installed = INSTALLED_CHARACTER
    elif config_entry.is_installed == Status.Unknown:
        is_installed = UNKNOWN_STATUS_CHARACTER

    if single:
        print(
            '\033[0;38;5;205m' + config_entry.description + '\033[0m'
        )
    else:
        # print its command, install status and short description
        print(
            '  \033[38;5;244m•\033[0m \033[38;5;248m[\033[0m \033[38;5;135;1m'
            + config_entry.shorthand
            + (' ' * abs(command_length - len(config_entry.shorthand)))
            + '\033[0m \033[38;5;248m] '
            + is_installed
            + '\033[0m \033[38;5;244m→\033[0m \033[38;5;205m'
            + config_entry.description + '\033[0m')


def execute_entry(config_entry: ConfigEntry) -> bool:
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

    if not config_entry.is_immutable:
        available_options += [reinstall, uninstall]

    # print the status of the config entry
    print_entry(config_entry, single=True)
    # ask the user what he wants to do with the entry
    print('\033[1mChoose between:')
    for o in available_options:
        print('  \033[4m' + o[:1] + '\033[0;1m' + o[1:])

    # take only first two letters from the names of the options
    # — user has to input these two letters of their chosen option
    available_options_cmds = [x[:1] for x in available_options]
    cmd_index = 0
    x = input()
    while x not in available_options_cmds:
        x = input(
            '\033[0mplease choose one of the options listed above\033[1m\n')

    cmd_index = available_options_cmds.index(x)
    chosen_option = available_options[cmd_index]

    # clean up
    print('\033[0m', end='')

    if chosen_option == install:
        config_entry.install()
        return True
    elif chosen_option == reinstall:
        config_entry.uninstall()
        config_entry.install()
        return True
    elif chosen_option == uninstall:
        config_entry.uninstall()
        return True

    return False
