import getpass
import re
import pathlib
import os
import shutil
from types import FunctionType
from typing import List, Tuple, Union

from config.config_entry import ConfigEntry, Status
from config.utilities import toggle_fileblock, does_contain_file_block, do_files_partially_overlap, do_lists_partially_overlap, copy_file_with_special_variables

HD = os.path.expanduser('~')
CD = str(pathlib.Path().absolute())
USER = getpass.getuser()


def ex(command: str, sudo: bool = False):
    '''
    Executes given command using the system shell.
    '''
    return os.system(
        ('sudo ' if sudo else '')
        + command
    )


def cp(source: str, target: str, sudo: bool = False):
    '''
    Copies given file to the desired location.

    Optionally creates a tree of directories with respect to the given
    target path.
    '''
    # create the target directory if it doesn’t exist
    os.makedirs(os.path.dirname(target), exist_ok=True)

    if os.path.isdir(source):
        # file is a directory
        # copy recursively
        ex('cp -r ' + source + ' ' + target, sudo=sudo)

    else:
        # file is not a directory
        ex('cp ' + source + ' ' + target, sudo=sudo)


def toggle_file(source: str, target: str, sudo: bool = False, variables: List[Tuple[str]] = None):
    '''
    Copies the source file to the target location or removes the file
    in the target location if it’s there.
    '''
    if os.path.exists(target):
        ex('rm -r ' + target, sudo=sudo)

    else:
        cp(source, target, sudo=sudo) \
            if variables is None \
            else copy_file_with_special_variables(source, target, variables)


def sf(bool_val: Union[bool, List[bool]], if_true: Status = Status.Installed, if_false: Status = Status.NotInstalled) -> Status:
    '''
    Converts boolean value into a `Status` value.

    *`sf` stands for `status_function`*
    '''
    if type(bool_val) == list:
        return if_true if len(bool_val) == sum(bool_val) \
            else if_false

    return if_true if bool_val else if_false


config_entries = [

    # Blender
    ConfigEntry(
        description='install Blender',
        shorthand='bld',
        execute=[
            lambda: ex(CD + '/src/scripts/install-blender.sh')
        ],
        is_installed=[
            lambda: sf(
                ex('command -v blender >/dev/null') == 0
            )
        ],
        toggable=False
    ),

    # Telegram
    ConfigEntry(
        description='install Telegram',
        shorthand='tlg',
        execute=[
            lambda: ex(CD + '/src/scripts/install-telegram.sh')
        ],
        is_installed=[
            lambda: sf(
                ex('ls ' + HD + '/.local/share/applications | grep -i telegram.desktop >/dev/null') == 0
            )
        ],
        toggable=False
    ),

    # Discord
    ConfigEntry(
        description='install Discord',
        shorthand='dsc',
        execute=[
            lambda: ex(CD + '/src/scripts/install-discord.sh')
        ],
        is_installed=[
            lambda: sf(
                ex('command -v discord >/dev/null') == 0
            )
        ],
        toggable=False
    ),

    # Insync
    ConfigEntry(
        description='install Insync',
        shorthand='ins',
        execute=[
            lambda: ex(CD + '/src/scripts/install-insync.sh')
        ],
        is_installed=[
            lambda: sf(
                ex('command -v insync >/dev/null') == 0
            )
        ],
        toggable=False
    ),

    # GPG signing for Git
    ConfigEntry(
        description='enable GPG signing in Git',
        shorthand='gpg',
        execute=[
            lambda: ex(CD + '/src/scripts/enable-git-signing.sh')
        ],
        is_installed=[
            lambda: sf(
                ex('[ -n "$(git config --global user.signingKey)" ]') == 0
            )
        ],
        toggable=False
    ),

    # load Bash config
    ConfigEntry(
        description='load Bash config',
        shorthand='brc',
        execute=[
            # copy settings for the `PATH` and `PS1` variables
            lambda: toggle_fileblock(
                CD + '/config-files/.bashrc',
                HD + '/.bashrc'
            ),
            # copy the `.bash_aliases` file
            lambda: toggle_file(
                CD + '/config-files/.bash_aliases',
                HD + '/.bash_aliases'
            )
        ],
        is_installed=[
            lambda: sf(
                does_contain_file_block(
                    CD + '/config-files/.bashrc',
                    HD + '/.bashrc'
                )
            ),
            lambda: sf(
                do_files_partially_overlap(
                    CD + '/config-files/.bash_aliases',
                    HD + '/.bash_aliases'
                )
            )
        ]
    ),

    # swap Control_R and Menu keys
    ConfigEntry(
        description='swap Control_R and Menu keys (good for keyboards without a dedicated Menu key)',
        shorthand='kym',
        execute=[
            lambda: toggle_fileblock(
                CD + '/config-files/.key_remap',
                HD + '/.bashrc'
            )
        ],
        is_installed=[
            lambda: sf(
                does_contain_file_block(
                    CD + '/config-files/.key_remap',
                    HD + '/.bashrc'
                )
            )
        ]
    ),

    # install config files
    ConfigEntry(
        description='install config files for: RedShift, Java formatter, and Neovim',
        shorthand='rds',
        execute=[
            lambda: toggle_file(
                CD + '/config-files/redshift.conf',
                HD + '/.config/redshift.conf'
            ),
            lambda: toggle_file(
                CD + '/config-files/nvim/init.vim',
                HD + '/.config/nvim/'
            ),
            lambda: toggle_file(
                CD + '/config-files/java-formatter.xml',
                HD + '/.config/java-formatter.xml'
            )
        ],
        is_installed=[
            lambda: sf(
                do_files_partially_overlap(
                    CD + '/config-files/redshift.conf',
                    HD + '/.config/redshift.conf'
                )
            ),
            lambda: sf(
                do_files_partially_overlap(
                    CD + '/config-files/nvim/init.vim',
                    HD + '/.config/nvim/init.vim'
                )
            ),
            lambda: sf(
                do_files_partially_overlap(
                    CD + '/config-files/java-formatter.xml',
                    HD + '/.config/java-formatter.xml'
                )
            )
        ]
    ),

    # load Cinnamon keyboard shortcuts
    ConfigEntry(
        description='Cinnamon: load keyboard shortcuts',
        shorthand='cks',
        execute=[
            lambda: ex(
                'dconf load / < ' + CD + '/config-files/cinnamon/keyboard-shortcuts.conf'
            ),
            lambda: toggle_file(
                CD + '/config-files/keyboard_volume_knob', HD + '/keyboard_volume_knob'
            )
        ],
        is_installed=[
            lambda: Status.Unknown,
            lambda: sf(
                os.path.exists(HD + '/keyboard_volume_knob')
            )
        ],
        toggable=False
    ),

    # theme for Cinnamon DE
    ConfigEntry(
        description='Cinnamon: install theme',
        shorthand='thm',
        execute=[
            lambda: ex(
                CD + '/src/scripts/cinnamon-install-theme.sh'
            )
        ],
        is_installed=[
            lambda: Status.Unknown
        ],
        toggable=False
    ),

    # other settings for Cinnamon DE
    ConfigEntry(
        description='Cinnamon: load other DE settings',
        shorthand='cos',
        execute=[
            lambda: ex(
                'dconf load / < ' + CD + '/config-files/cinnamon/other-settings.conf'
            )
        ],
        is_installed=[
            lambda: Status.Unknown
        ],
        toggable=False
    ),

    # additional fonts
    ConfigEntry(
        description='install additional fonts',
        shorthand='fnt',
        execute=[
            lambda: ex(
                CD + '/src/scripts/install-additional-fonts.sh'
            )
        ],
        is_installed=[
            lambda: sf(
                [
                    os.path.exists(
                        '/usr/share/fonts/truetype/' + x
                    ) for x in ['merriweather', 'fira-code', 'fira-sans']
                ]
            )
        ],
        toggable=False
    ),

    # copy utility scripts
    ConfigEntry(
        description='copy utility scripts',
        shorthand='cus',
        execute=[
            lambda: toggle_file(
                CD + '/utility-scripts',
                '/opt/utility-scripts',
                sudo=True
            )
        ],
        is_installed=[
            lambda: sf(
                [
                    do_files_partially_overlap(
                        CD + '/utility-scripts/' + f,
                        '/opt/utility-scripts/' + f
                    ) for f in os.listdir(CD + '/utility-scripts')
                ]
            )
        ]
    ),

    # set IBus icon colour
    ConfigEntry(
        description='set IBus icon colour',
        shorthand='ibu',
        execute=[
            lambda: ex(
                '/usr/bin/gsettings set org.freedesktop.ibus.panel xkb-icon-rgba "#c0c0c0"'
            )
        ],
        is_installed=[
            lambda: Status.Unknown
        ],
        toggable=False
    ),

    # enable start on boot for the Audio Loopback program
    ConfigEntry(
        description='enable start on boot for the Audio Loopback program',
        shorthand='alp',
        execute=[
            lambda: toggle_file(
                CD + '/config-files/autostart/audio-loopback.desktop',
                HD + '/.config/autostart/audio-loopback.desktop',
                variables=[(r'USER', USER)]
            ),
            lambda: toggle_file(
                CD + '/config-files/.audloop',
                HD + '/.audloop'
            )
        ],
        is_installed=[
            lambda: sf(
                os.path.exists(
                    HD + '/.config/autostart/audio-loopback.desktop'
                )
            ),
            lambda: sf(
                os.path.exists(
                    HD + '/.audloop'
                )
            )
        ]
    ),

    ConfigEntry(
        description='enable start on boot for the second keyboard program (make sure the exec is ready)',
        shorthand='skb',
        execute=[
            lambda: toggle_file(
                CD + '/config-files/autostart/second-keyboard.desktop',
                HD + '/.config/autostart/second-keyboard.desktop',
                variables=[(r'USER', USER)]
            )
        ],
        is_installed=[
            lambda: sf(
                os.path.exists(
                    HD + '/.config/autostart/second-keyboard.desktop'
                )
            )
        ]
    )

]
