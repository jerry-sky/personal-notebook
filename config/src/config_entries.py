import os
from helper.programs import install_apt_program, install_global_javascript_program, pull_docker_image

from model import ConfigEntries, ConfigEntry, ConfigEntryGroup, InstallationPackage, Status
from helper.files import toggle_fileblock
from helper.links import toggle_file_links, toggle_desktop_file_links
from helper.ex import ex
from env import CFD, HD, HDC, ISD, UBU, USD, FXD


config_entries: ConfigEntries = [

    ConfigEntryGroup(
        name='Desktop environment',
        list=[

            ConfigEntry(
                description='load DE configuration (dconf)',
                shorthand='dco',
                installation_packages=[
                    InstallationPackage(
                        install_func=lambda: ex(
                            'dconf load /<'
                            + UBU + '/dconf.conf'
                        ),
                        is_installed=lambda: Status.Unknown,
                    ),
                ],
            ),

            ConfigEntry(
                description='install utilities',
                shorthand='deu',
                installation_packages=[
                    install_apt_program([
                        # advanced (per-program) audio management utility
                        'pavucontrol',
                        # CPU power management
                        'indicator-cpufreq',
                        # execute HUD device commands within X.org window system
                        'xdotool',
                    ]),
                    # fix CPU Freq Indicator to work within Gtk 4.0
                    toggle_fileblock(
                        FXD + '/indicator_cpufreq.py',
                        '/usr/lib/python3/dist-packages/indicator_cpufreq/indicator.py',
                        sudo=True,
                        line_number_location=17,
                    ),
                    # AppImage programs require this utility
                    install_apt_program(
                        'libfuse2',
                        apt_repository='universe',
                    ),
                    # for changing the background of the login screen in Ubuntu
                    InstallationPackage(
                        install_func=lambda: ex(
                            ISD + '/install-ubuntu-login-screen-background-tool.sh',
                        ),
                        is_installed=lambda: ex(
                            'command -v ubuntu-gdm-set-background.sh >/dev/null',
                        ) == 0,
                    ),
                ],
            ),

            ConfigEntry(
                description='install (Neo)Vim',
                shorthand='rds',
                installation_packages=[
                    install_apt_program('neovim'),
                    toggle_file_links(
                        CFD + '/vim/init.vim',
                        HD + '/.config/nvim/',
                    ),
                    toggle_file_links(
                        HD + '/.config/nvim',
                        HD + '.vimrc',
                    ),
                ],
            ),

            ConfigEntry(
                description='install KBCT (key remapping tool)',
                shorthand='kbc',
                installation_packages=[
                    toggle_file_links(
                        CFD + '/kbct/config.yml',
                        '/etc/kbct/config.yml',
                        sudo=True,
                    ),
                    toggle_file_links(
                        CFD + '/kbct/kbct.service',
                        '/usr/lib/systemd/system/kbct.service',
                        sudo=True,
                    ),
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

            # adapted from: https://github.com/swaywm/sway/issues/595#issuecomment-425888305
            # JetBrains IDE will stay in focus even though its windows are in background.
            # This issues happens primarily when having two windows open on two separate workspaces (virtual desktops).
            # Alt-tab–ing does work without this fix, however switching between apps (META+Tab) does not.
            ConfigEntry(
                description='fix Java programs stealing focus (JetBrains)',
                shorthand='fjp',
                installation_packages=[
                    toggle_fileblock(
                        source=CFD + '/etc/profile',
                        target='/etc/profile',
                        sudo=True,
                    ),
                ],
            )

        ],
    ),

    ConfigEntryGroup(
        name='Programs',
        list=[

            ConfigEntry(
                description='install utilities',
                shorthand='put',
                installation_packages=[
                    install_apt_program([
                        'python3-pip',
                        'filezilla',
                        'bat',
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

            ConfigEntry(
                description='install Docker',
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
                        ],
                    ),
                ],
            ),

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

            ConfigEntry(
                description='install Pandoc (through Pandocker)',
                shorthand='pdk',
                installation_packages=[
                    pull_docker_image([
                        'dalibo/pandocker',
                    ]),
                ],
            ),

            ConfigEntry(
                description='install Signal',
                shorthand='sgl',
                installation_packages=[
                    InstallationPackage(
                        install_func=lambda: ex(
                            ISD + '/install-signal.sh',
                        ),
                        is_installed=lambda: ex(
                            'command -v signal-desktop >/dev/null',
                        ) == 0,
                    ),
                ],
            ),

            ConfigEntry(
                description='install Telegram',
                shorthand='tlg',
                installation_packages=[
                    InstallationPackage(
                        install_func=lambda: ex(
                            ISD + '/install-telegram.sh'),
                        is_installed=lambda: ex(
                            'ls ' + HD + '/.local/share/applications | grep -i telegram.desktop >/dev/null') == 0,
                    ),
                ],
            ),

            ConfigEntry(
                description='install Discord',
                shorthand='dsc',
                installation_packages=[
                    InstallationPackage(
                        install_func=lambda: ex(
                            ISD + '/install-discord.sh'),
                        is_installed=lambda: ex(
                            'command -v discord >/dev/null') == 0,
                    ),
                ],
            ),

            ConfigEntry(
                description='install Insync',
                shorthand='ins',
                installation_packages=[
                    InstallationPackage(
                        install_func=lambda: ex(
                            ISD + '/install-insync.sh'),
                        is_installed=lambda: ex(
                            'command -v insync >/dev/null') == 0,
                    ),
                ],
            ),

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
                        ],
                    ),
                ],
            ),

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

        ],
    ),

    ConfigEntryGroup(
        name='General config',
        list=[

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
                        HD + '/.bash_aliases',
                    ),
                    toggle_file_links(
                        CFD + '/.inputrc',
                        HD + '/.inputrc',
                    ),
                ],
            ),

        ],
    ),

    ConfigEntryGroup(
        name='Other',
        list=[

            ConfigEntry(
                description='install additional fonts',
                shorthand='fnt',
                installation_packages=[
                    InstallationPackage(
                        install_func=lambda: ex(
                            ISD + '/install-additional-fonts.sh',
                        ),
                        is_installed=lambda: [
                            os.path.exists(
                                '/usr/share/fonts/truetype/' + x
                            ) for x in ['Merriweather', 'Fira Code', 'Fira Sans']
                        ],
                    ),
                ],
            ),

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
                    toggle_desktop_file_links(
                        USD + '/audio-loopback.desktop',
                        '/usr/share/applications/audio-loopback.desktop',
                    ),
                ],
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

        ],
    ),

]
