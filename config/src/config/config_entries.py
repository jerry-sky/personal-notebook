import getpass
import re
import pathlib
import os
import shutil
from types import FunctionType
from typing import List, Tuple, Union

from config.config_entry import ConfigEntry, Status, InstallationPackage
from config.utilities import toggle_fileblock as __toggle_fileblock, does_contain_file_block, do_files_partially_overlap, do_lists_partially_overlap, copy_file_with_special_variables

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


def lns(source: str, target: str, sudo: bool = False):
    '''
    Creates a symbolic link in the target directory to the file
    in the source directory.
    '''

    if os.path.isdir(source):
        # file is a directory
        ex('mkdir -p -- ' + target, sudo)
        ex(
            'find '  # find all files in the source directory
            + source
            + ' -type f | while read f; do sudo ln -s "$f"'
            + ' ' + target
            # and create links to the in the target directory
            + '/${f##*/}; done'
        )
    else:
        # file is not a directory
        ex('mkdir -p -- ' + os.path.dirname(target), sudo)
        ex('ln -s ' + source + ' ' + target, sudo)


def toggle_file_links(source: str, target: str, sudo: bool = False):
    '''
    Creates links to a provided file or files in a directory or deletes
    them if they exist.

    Returns an `InstallationPackage`.
    '''
    return InstallationPackage(
        install_func=lambda: lns(source, target, sudo),
        uninstall_func=lambda: ex('rm -r ' + target, sudo),
        is_installed=lambda: True if os.path.exists(target) else False
    )


def toggle_fileblock(source: str, target: str, sudo: bool = False):
    '''
    An `InstallationPackage` wrapper around `utilities.toggle_file`.
    '''
    return InstallationPackage(
        install_func=lambda: __toggle_fileblock(source, target, True),
        uninstall_func=lambda: __toggle_fileblock(source, target, False),
        is_installed=lambda: does_contain_file_block(source, target)
    )


config_entries = [

    # Blender
    ConfigEntry(
        description='install Blender',
        shorthand='bld',
        installation_packages=[
            InstallationPackage(
                install_func=lambda: ex(
                    CD + '/src/scripts/install-blender.sh'),
                uninstall_func=False,
                is_installed=lambda: ex('command -v blender >/dev/null') == 0
            )
        ]
    ),

    # Telegram
    ConfigEntry(
        description='install Telegram',
        shorthand='tlg',
        installation_packages=[
            InstallationPackage(
                install_func=lambda: ex(
                    CD + '/src/scripts/install-telegram.sh'),
                is_installed=lambda: ex(
                    'ls ' + HD + '/.local/share/applications | grep -i telegram.desktop >/dev/null') == 0
            )
        ]
    ),

    # Discord
    ConfigEntry(
        description='install Discord',
        shorthand='dsc',
        installation_packages=[
            InstallationPackage(
                install_func=lambda: ex(
                    CD + '/src/scripts/install-discord.sh'),
                is_installed=lambda: ex('command -v discord >/dev/null') == 0
            )
        ]
    ),

    # Insync
    ConfigEntry(
        description='install Insync',
        shorthand='ins',
        installation_packages=[
            InstallationPackage(
                install_func=lambda: ex(CD + '/src/scripts/install-insync.sh'),
                is_installed=lambda: ex('command -v insync >/dev/null') == 0
            )
        ]
    ),

    # GPG signing for Git
    ConfigEntry(
        description='enable GPG signing in Git',
        shorthand='gpg',
        installation_packages=[
            InstallationPackage(
                install_func=lambda: ex(
                    CD + '/src/scripts/enable-git-signing.sh'),
                is_installed=lambda: ex(
                    '[ -n "$(git config --global user.signingKey)" ]') == 0
            )
        ]
    ),

    # load Bash config
    ConfigEntry(
        description='load Bash config',
        shorthand='brc',
        installation_packages=[
            toggle_fileblock(
                CD + '/config-files/.bashrc',
                HD + '/.bashrc'
            ),
            toggle_file_links(
                CD + '/config-files/.bash_aliases',
                HD + '/.bash_aliases'
            )
        ]
    ),

    # swap Control_R and Menu keys
    ConfigEntry(
        description='swap Control_R and Menu keys (good for keyboards without a dedicated Menu key)',
        shorthand='kym',
        installation_packages=[
            toggle_fileblock(
                CD + '/config-files/.key_remap',
                HD + '/.bashrc'
            )
        ]
    ),

    # install config files
    ConfigEntry(
        description='install config files for: RedShift, Java formatter, and Neovim',
        shorthand='rds',
        installation_packages=[
            toggle_file_links(
                CD + '/config-files/redshift.conf',
                HD + '/.config/redshift.conf'
            ),
            toggle_file_links(
                CD + '/config-files/nvim/init.vim',
                HD + '/.config/nvim/'
            ),
            toggle_file_links(
                CD + '/config-files/java-formatter.xml',
                HD + '/.config/java-formatter.xml'
            )
        ]
    ),

    # load Cinnamon keyboard shortcuts
    ConfigEntry(
        description='Cinnamon: load keyboard shortcuts',
        shorthand='cks',
        installation_packages=[
            InstallationPackage(
                install_func=lambda: ex(
                    'dconf load / < ' + CD + '/config-files/cinnamon/keyboard-shortcuts.conf'
                )
            ),
            toggle_file_links(
                CD + '/config-files/keyboard_volume_knob', HD + '/keyboard_volume_knob'
            )
        ]
    ),

    # theme for Cinnamon DE
    ConfigEntry(
        description='Cinnamon: install theme',
        shorthand='thm',
        installation_packages=[
            InstallationPackage(
                install_func=lambda: ex(
                    CD + '/src/scripts/cinnamon-install-theme.sh'
                )
            )
        ]
    ),

    # other settings for Cinnamon DE
    ConfigEntry(
        description='Cinnamon: load other DE settings',
        shorthand='cos',
        installation_packages=[
            InstallationPackage(
                install_func=lambda: ex(
                    'dconf load / < ' + CD + '/config-files/cinnamon/other-settings.conf'
                )
            )
        ]
    ),

    # additional fonts
    ConfigEntry(
        description='install additional fonts',
        shorthand='fnt',
        installation_packages=[
            InstallationPackage(
                install_func=lambda: ex(
                    CD + '/src/scripts/install-additional-fonts.sh'
                ),
                is_installed=lambda: [
                    os.path.exists(
                        '/usr/share/fonts/truetype/' + x
                    ) for x in ['merriweather', 'fira-code', 'fira-sans']
                ]
            )
        ]
    ),

    # copy utility scripts
    ConfigEntry(
        description='copy utility scripts',
        shorthand='cus',
        installation_packages=[
            toggle_file_links(
                CD + '/utility-scripts',
                '/opt/utility-scripts',
                sudo=True
            )
        ]
    ),

    # set IBus icon colour
    ConfigEntry(
        description='set IBus icon colour',
        shorthand='ibu',
        installation_packages=[
            InstallationPackage(
                install_func=lambda: ex(
                    '/usr/bin/gsettings set org.freedesktop.ibus.panel xkb-icon-rgba "#c0c0c0"'
                )
            )
        ]
    ),

    # enable start on boot for the Audio Loopback program
    ConfigEntry(
        description='enable start on boot for the Audio Loopback program',
        shorthand='alp',
        installation_packages=[
            toggle_file_links(
                CD + '/config-files/autostart/audio-loopback.desktop',
                HD + '/.config/autostart/audio-loopback.desktop',
            ),
            toggle_file_links(
                CD + '/config-files/.audloop',
                HD + '/.audloop'
            )
        ]
    ),

    ConfigEntry(
        description='enable start on boot for the second keyboard program (make sure the exec is ready)',
        shorthand='skb',
        installation_packages=[
            toggle_file_links(
                CD + '/config-files/autostart/second-keyboard.desktop',
                HD + '/.config/autostart/second-keyboard.desktop',
            )
        ]
    )

]
