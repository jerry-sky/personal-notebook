import os
from helper.programs import install_apt_program, install_global_javascript_program

from model import ConfigEntries, ConfigEntry, ConfigEntryGroup, InstallationPackage, Status
from helper.files import toggle_fileblock
from helper.links import toggle_file_links, toggle_desktop_file_links
from helper.ex import ex
from env import AUD, CFD, HD, HDC, ISD, UBU, USD


config_entries: ConfigEntries = [

    ConfigEntryGroup(
        name='Desktop environment',
        list=[

            # desktop environment configuration
            ConfigEntry(
                description='load DE configuration (dconf)',
                shorthand='dco',
                installation_packages=[
                    InstallationPackage(
                        install_func=lambda: ex(
                            'dconf load <'
                            + UBU + '/dconf.conf'
                        ),
                        is_installed=lambda: Status.Unknown,
                    ),
                ],
            ),

            # complimentary programs that are part of the desktop environment
            ConfigEntry(
                description='install utilities',
                shorthand='deu',
                installation_packages=[
                    install_apt_program([
                        # advanced (per-program) audio management utility
                        'pavucontrol',
                        # CPU power management
                        'indicator-cpufreq',
                        # night mode
                        'redshift',
                        'redshift-gtk',
                    ]),
                ],
            ),

            # KBCT — key remapping
            ConfigEntry(
                description='install KBCT (key remapping tool)',
                shorthand='kbc',
                installation_packages=[
                    InstallationPackage(
                        install_func=lambda: ex(
                            ISD + '/install-kbct.sh'
                        ),
                        is_installed=lambda: ex(
                            'command -v kbct >/dev/null'
                        ) == 0,
                    ),
                ]
            ),

            ConfigEntry(
                description='install ‘audio loopback’',
                shorthand='aud',
                installation_packages=[
                    toggle_desktop_file_links(
                        AUD + '/audio-loopback.desktop',
                        '/usr/share/applications/audio-loopback.desktop',
                    ),
                ],
            ),

            # iBus
            ConfigEntry(
                description='install iBus-Anthy, iBus-Hangul',
                shorthand='ibu',
                installation_packages=[
                    install_apt_program([
                        'ibus-anthy',
                        'ibus-hangul',
                    ]),
                ],
            ),

            ConfigEntry(
                description='install Touchégg (touchpad gestures)',
                shorthand='tou',
                installation_packages=[
                    InstallationPackage(
                        install_func=lambda: ex(
                            ISD + '/install-touchégg.sh'
                        ),
                        is_installed=lambda: ex(
                            'command -v touchegg >/dev/null'
                        ) == 0,
                    ),
                    toggle_file_links(
                        source=CFD + '/touchégg/touchegg.conf',
                        target=HDC + '/touchegg/touchegg.conf',
                    ),
                ],
            ),

        ],
    ),

    ConfigEntryGroup(
        name='Programs',
        list=[

            # various utilities
            ConfigEntry(
                description='install utilities',
                shorthand='put',
                installation_packages=[
                    install_apt_program([
                        'python3-pip',
                        'filezilla',
                    ]),
                ],
            ),

            ConfigEntry(
                description='install JS utilities',
                shorthand='duj',
                installation_packages=[
                    install_global_javascript_program([
                        # other JavaScript package managers
                        'pnpm',
                        'yarn',
                        # JavaScript daemon
                        'nodemon',
                        # updating packages in a project
                        'npm-check-updates',
                    ]),
                ],
            ),

            ConfigEntry(
                description='install Git utilities',
                shorthand='duj',
                installation_packages=[
                    install_global_javascript_program([
                        # trimming unnecessary local branches (already merged, deleted from origin)
                        'git-trim',
                    ]),
                ],
            ),

            # TeX Live
            ConfigEntry(
                description='install TeX Live',
                shorthand='tex',
                installation_packages=[
                    InstallationPackage(
                        install_func=lambda: ex(
                            ISD + '/install-tex-live.sh'
                        ),
                        is_installed=lambda: ex(
                            '. ~/.bashrc && printf $PATH | grep texlive >/dev/null'
                        ) == 0
                    ),
                ]
            ),

            # Docker
            ConfigEntry(
                description='install Docker and Docker-Compose',
                shorthand='dck',
                installation_packages=[
                    InstallationPackage(
                        install_func=lambda: ex(
                            ISD + '/install-docker.sh',
                        ),
                        is_installed=lambda: [
                            ex(
                                'command -v docker >/dev/null',
                            ) == 0,
                            ex(
                                'command -v docker-compose >/dev/null',
                            ) == 0,
                        ],
                    ),
                ],
            ),

            # Blender
            ConfigEntry(
                description='install Blender',
                shorthand='bld',
                installation_packages=[
                    InstallationPackage(
                        install_func=lambda: ex(
                            ISD + '/install-blender.sh'),
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
            ),

            # Node environment
            ConfigEntry(
                description='install NVM, NodeJS, NPM',
                shorthand='nvm',
                installation_packages=[
                    InstallationPackage(
                        install_func=lambda: ex(
                            ISD + '/install-node.sh'
                        ),
                        is_installed=lambda: [
                            ex('command -v node >/dev/null') == 0,
                        ]
                    ),
                ]
            ),

        ]
    ),

    ConfigEntryGroup(
        name='General config',
        list=[

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
    ),

    ConfigEntryGroup(
        name='Other',
        list=[

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
                            ) for x in ['Merriweather', 'Fira Code', 'Fira Sans']
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
                    ),
                    install_apt_program('wmctrl'),
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
            ),

            ConfigEntry(
                description='enable automount on boot for a drive',
                shorthand='mnt',
                installation_packages=[
                    InstallationPackage(
                        install_func=lambda: ex(
                            ISD + '/automount.sh',
                        ),
                    ),
                ],
            ),

            ConfigEntry(
                description='“fix” VS Code so it does not display toast notifications (dirty)',
                shorthand='fcd',
                installation_packages=[
                    InstallationPackage(
                        install_func=lambda: ex(
                            ISD + '/fix-vscode.sh',
                        ),
                    ),
                ],
            ),

        ],
    ),

]
