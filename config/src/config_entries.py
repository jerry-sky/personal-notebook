import getpass
import pathlib
import os

from model import ConfigEntry, Status, InstallationPackage
from helper.files import toggle_fileblock
from helper.links import toggle_file_links
from helper.ex import ex

# home directory
HD = os.path.expanduser('~')
# root config directory
CD = str(pathlib.Path().absolute())
# installation script directory
ISD = CD + '/install-scripts'
# config files directory
CFD = CD + '/config-files'
# utility scripts directory
USD = CD + '/utility-scripts'
# second-keyboard directory
SKD = CD + '/second-keyboard'
# audio directory
AUD = CD + '/audio'

# username
USER = getpass.getuser()

# default installer/ verifier commands
utilities_default_installer = 'sudo apt-get install -y {}'
utilities_default_verifier = 'dpkg -l {} >/dev/null'
utilities_python_installer = 'python3 -m pip install {}'
utilities_python_verifier = 'python3 -m pip list | grep {} >/dev/null'

# list of all utility programs
utilities = [
    # screenshots
    (utilities_default_installer, utilities_default_verifier, 'maim xclip xdotool'),
    # file management
    (utilities_default_installer, utilities_default_verifier, 'filezilla'),
    # window management
    (utilities_default_installer, utilities_default_verifier, 'wmctrl'),
    # audio management
    (utilities_default_installer, utilities_default_verifier, 'pavucontrol'),
    # python3 base (PIP)
    (utilities_default_installer, utilities_default_verifier, 'python3-pip'),
    # numlock auto on
    (utilities_default_installer, utilities_default_verifier, 'numlockx'),
    # `xte` and such `xautomation` tools
    (utilities_default_installer, utilities_default_verifier, 'xautomation'),
]

config_entries = [

    {
        'name': 'Programs and utilities',
        'list': [

            # various utilities
            ConfigEntry(
                description='install utilities',
                shorthand='utl',
                installation_packages=[
                    InstallationPackage(
                        install_func=lambda: [
                            ex(util[0].format(util[2]), sudo=True) for util in utilities
                        ],
                        is_installed=lambda: [
                            ex(util[1].format(sub_util)) == 0 for util in utilities for sub_util in util[2].split(' ')
                        ]
                    )
                ]
            ),

            # Blender
            ConfigEntry(
                description='install Blender',
                shorthand='bld',
                installation_packages=[
                    InstallationPackage(
                        install_func=lambda: ex(
                            ISD + '/install-blender.sh'),
                        uninstall_func=False,
                        is_installed=lambda: ex(
                            'command -v blender >/dev/null') == 0
                    )
                ]
            ),

            # OBS
            ConfigEntry(
                description='install OBS',
                shorthand='obs',
                installation_packages=[
                    InstallationPackage(
                        install_func=lambda: ex(
                            ISD + '/install-obs.sh'),
                        uninstall_func=False,
                        is_installed=lambda: ex(
                            'command -v obs >/dev/null') == 0
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
                            ISD + '/install-telegram.sh'),
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
                            ISD + '/install-discord.sh'),
                        is_installed=lambda: ex(
                            'command -v discord >/dev/null') == 0
                    )
                ]
            ),

            # Insync
            ConfigEntry(
                description='install Insync',
                shorthand='ins',
                installation_packages=[
                    InstallationPackage(
                        install_func=lambda: ex(
                            ISD + '/install-insync.sh'),
                        is_installed=lambda: ex(
                            'command -v insync >/dev/null') == 0
                    )
                ]
            ),

            # Unity 3D
            ConfigEntry(
                description='install Unity Hub, .NET SDK+Runtime, and Mono',
                shorthand='unt',
                installation_packages=[
                    InstallationPackage(
                        install_func=lambda: ex(
                            ISD + '/install-unity.sh'),
                        is_installed=lambda: [
                            ex('command -v unity-hub >/dev/null') == 0,
                            ex('command -v mono >/dev/null') == 0,
                            ex('command -v dotnet >/dev/null') == 0,
                        ]
                    )
                ]
            )

        ]
    },

    {
        'name': 'General config',
        'list': [

            # GPG signing for Git
            ConfigEntry(
                description='enable GPG signing in Git',
                shorthand='gpg',
                installation_packages=[
                    InstallationPackage(
                        install_func=lambda: ex(
                            ISD + '/enable-git-signing.sh'),
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
                        CFD + '/.bashrc',
                        HD + '/.bashrc'
                    ),
                    toggle_file_links(
                        CFD + '/.bash_aliases',
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
                        CFD + '/.key_remap',
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
                        CFD + '/redshift/redshift.conf',
                        HD + '/.config/redshift.conf'
                    ),
                    toggle_file_links(
                        CFD + '/nvim/init.vim',
                        HD + '/.config/nvim/'
                    ),
                    toggle_file_links(
                        CFD + '/java/java-formatter.xml',
                        HD + '/.config/java-formatter.xml'
                    )
                ]
            ),

        ]
    },

    {
        'name': 'Desktop environment',
        'list': [

            # i3-gaps
            ConfigEntry(
                description='install i3 WM',
                shorthand='i3w',
                installation_packages=[
                    InstallationPackage(
                        install_func=lambda: ex(
                            CD + '/src/scripts/install-i3.sh'
                        ),
                        is_installed=lambda: ex(
                            'command -v i3 >/dev/null'
                        ) == 0
                    )
                ]
            ),

            # theme
            ConfigEntry(
                description='install theme',
                shorthand='thm',
                installation_packages=[
                    InstallationPackage(
                        install_func=lambda: ex(
                            CD + '/src/scripts/install-theme.sh'
                        )
                    )
                ]
            ),

            # i3 and i3status
            ConfigEntry(
                description='base config',
                shorthand='i3c',
                installation_packages=[
                    toggle_file_links(
                        CFD + '/i3/i3/config',
                        HD + '/.config/i3/config'
                    ),
                    toggle_file_links(
                        CFD + '/i3/i3status/config',
                        HD + '/.config/i3status/config'
                    ),
                    toggle_file_links(
                        CFD + '/i3/dunst/dunstrc',
                        HD + '/.config/dunst/dunstrc'
                    ),
                    toggle_file_links(
                        CFD + '/i3/compton/compton.conf',
                        HD + '/.config/compton.conf'
                    ),
                    # keyboard knob switcher
                    toggle_file_links(
                        CFD + '/keyboard-volume-knob',
                        HD + '/keyboard-volume-knob'
                    )
                ]
            ),

            ConfigEntry(
                description='enable start on boot for the second keyboard program (make sure the exec is ready)',
                shorthand='skb',
                installation_packages=[
                    InstallationPackage(
                        install_func=lambda: [
                            # copy the sudoers file
                            ex(
                                'sudo cp ' + CD + '/config-files/sudoers.d/second-keyboard /etc/sudoers.d/second-keyboard && ' \
                                + 'sudo chown root:root /etc/sudoers.d/second-keyboard'
                            ),
                            # make room for the ‘gain access’ script
                            ex(
                                'mkdir -p ' + HD + '/second-keyboard'
                            ),
                            # copy the script
                            ex(
                                'sudo cp ' + CD + '/second-keyboard/gain-access.sh ' \
                                + HD + '/second-keyboard/gain-access.sh'
                            ),
                            # give root access to it
                            ex(
                                'sudo chown root:root ' + HD + '/second-keyboard/gain-access.sh && ' \
                                + 'sudo chmod 4755 ' + HD + '/second-keyboard/gain-access.sh'
                            )
                        ],
                        is_installed=lambda: ex(
                            'test -f ' + HD + '/second-keyboard/gain-access.sh'
                        ) == 0
                    ),
                ]
            ),

        ]
    },

    {
        'name': 'Other',
        'list': [

            # additional fonts
            ConfigEntry(
                description='install additional fonts',
                shorthand='fnt',
                installation_packages=[
                    InstallationPackage(
                        install_func=lambda: ex(
                            ISD + '/install-additional-fonts.sh'
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
                        USD,
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

            # Intel related graphical settings
            ConfigEntry(
                description='use ‘no tearing’ option for Intel graphics drivers',
                shorthand='int',
                installation_packages=[
                    toggle_file_links(
                        CFD + '/graphics/20-intel.conf',
                        '/etc/X11/xorg.conf.d/20-intel.conf',
                        sudo=True
                    )
                ]
            )

        ]
    }

]

# flatten the list
config_entries_flat = [ce for group in config_entries for ce in group['list']]