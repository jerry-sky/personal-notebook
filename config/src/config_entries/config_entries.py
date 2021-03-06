from config_entries.config_entry import ConfigEntry, Status
from config_entries.toggle_some_lines import toggle_some_lines, check_if_lines_present
from config_entries.file_checking_utilities import do_files_overlap, do_lists_overlap
import shutil
import os
import pathlib
import re

HD = os.path.expanduser('~')
CD = str(pathlib.Path().absolute())

print(HD)

# shorthanded copy function
def cp(source, target, create_dirs=False, tree=False):
    if tree:
        try:
            shutil.rmtree(target)
        except:
            pass
        shutil.copytree(source, target, copy_function=shutil.copy2)
    else:
        if create_dirs:
            try:
                os.makedirs(target)
            except:
                pass
        shutil.copy2(source, target)


# shorthand shell execution function
def ex(command): return os.system(command)


# a special case of a config entry
def bash_aliases_insiders():
    '''Copies `.bash_aliases` but with `code` replaced with `code-insiders`.
    '''
    # first – copy the original file
    cp(CD + '/config-files/.bash_aliases', HD + '/')
    # replace every occurrence of `code` with `code-insiders`
    with open(HD + '/.bash_aliases', 'r+') as fi, open(HD + '/.bash_aliases_tmp', 'w+') as fo:
        for line in fi:
            fo.write(
                re.sub(
                    # replace all occurrences that aren't file paths
                    r'code(?!\/)',
                    'code-insiders',
                    line
                )
            )
    # remove the original file and rename the new one
    os.remove(HD + '/.bash_aliases')
    os.rename(HD + '/.bash_aliases_tmp', HD + '/.bash_aliases')

def bash_aliases_insiders_is_installed():
    '''
    Special case of `is_installed` for the `insiders` version of
    the bash aliases file.
    '''
    try:
        with open(CD + '/config-files/.bash_aliases', 'r') as forg, open(HD + '/.bash_aliases', 'r') as fcur:
            original_lines = forg.readlines()
            insiders_lines = []
            for line in original_lines:
                insiders_lines.append(
                    re.sub(
                        # replace all occurrences that aren't file paths
                        r'code(?!\/)',
                        'code-insiders',
                        line
                    )
                )

            current_lines = fcur.readlines()
            if do_lists_overlap(insiders_lines, current_lines):
                return Status.Installed
            else:
                return Status.NotInstalled
    except:
        return Status.NotInstalled


config_entries = [
    ConfigEntry(
        description='append a few lines to .bashrc (changes PS1 and PATH)',
        shorthand='brc',
        execute=lambda: toggle_some_lines(
            CD + '/config-files/.bashrc', HD + '/.bashrc'),
        is_installed=lambda: Status.Installed if check_if_lines_present(CD + '/config-files/.bashrc', HD + '/.bashrc') else Status.NotInstalled
    ),

    ConfigEntry(
        description='swap Control_R and Menu keys (good for keyboards without a dedicated Menu key)',
        shorthand='kym',
        execute=lambda: toggle_some_lines(
            CD + '/config-files/.key_remap', HD + '/.bashrc'),
        is_installed=lambda: Status.Installed if check_if_lines_present(
            CD + '/config-files/.key_remap', HD + '/.bashrc') else Status.NotInstalled
    ),

    ConfigEntry(
        description='copy .bash_aliases',
        shorthand='bas',
        execute=lambda: cp(CD + '/config-files/.bash_aliases', HD + '/.bash_aliases'),
        is_installed=lambda: Status.Installed if do_files_overlap(CD + '/config-files/.bash_aliases', HD + '/.bash_aliases') else Status.NotInstalled
    ),

    ConfigEntry(
        description='copy .bash_aliases but with `code-insiders` instead of `code`',
        shorthand='bas-ins',
        execute=bash_aliases_insiders,
        is_installed=bash_aliases_insiders_is_installed
    ),

    ConfigEntry(
        description='copy redshift config file',
        shorthand='rds',
        execute=lambda: cp(
            CD + '/config-files/redshift.conf', HD + '/.config/redshift.conf'),
        is_installed=lambda: Status.Installed if do_files_overlap(CD + '/config-files/redshift.conf', HD + '/.config/redshift.conf') else Status.NotInstalled
    ),

    ConfigEntry(
        description='copy neovim init file',
        shorthand='nvi',
        execute=lambda: cp(CD + '/config-files/nvim/init.vim',
                           HD + '/.config/nvim/', create_dirs=True),
        is_installed=lambda: Status.Installed if do_files_overlap(CD + '/config-files/nvim/init.vim', HD + '/.config/nvim/init.vim') else Status.NotInstalled
    ),

    ConfigEntry(
        description='copy java formatter file',
        shorthand='jav',
        execute=lambda: cp(
            CD + '/config-files/java-formatter.xml', HD + '/.config/java-formatter.xml'),
        is_installed=lambda: Status.Installed if do_files_overlap(CD + '/config-files/java-formatter.xml', HD + '/.config/java-formatter.xml') else Status.NotInstalled
    ),

    ConfigEntry(
        description='copy menu icon file',
        shorthand='men',
        execute=lambda: ex('sudo cp ' + CD + '/config-files/menu-icon.png /usr/share/icons/'),
        is_installed=lambda: Status.Installed if os.path.exists('/usr/share/icons/menu-icon.png') else Status.NotInstalled
    ),

    ConfigEntry(
        description='load Cinnamon keyboard shortcuts',
        shorthand='cks',
        execute=lambda: ex(
            'dconf load /org/cinnamon/desktop/keybindings/ < ./config-files/cinnamon-keyboard-shortcuts.conf'),
        is_installed=lambda: Status.Unknown
    ),

    ConfigEntry(
        description='copy utility scripts',
        shorthand='cus',
        execute=lambda: ex('sudo cp -r ' + CD + '/utility-scripts /opt/'),
        is_installed=lambda: Status.Installed if os.path.exists('/opt/utility-scripts') else Status.NotInstalled
    ),

    ConfigEntry(
        description='set IBus icon colour',
        shorthand='ibu',
        execute=lambda: ex(
            '/usr/bin/gsettings set org.freedesktop.ibus.panel xkb-icon-rgba "#cfcfcf"'),
        is_installed=lambda: Status.Unknown
    ),

    ConfigEntry(
        description='copy the keyboard volume knob scripts (more in «readme»)',
        shorthand='ckvb',
        execute=lambda: cp(
            CD + '/config-files/keyboard_volume_knob', HD + '/keyboard_volume_knob', tree=True),
        is_installed=lambda: Status.Installed if os.path.exists(HD + '/keyboard_volume_knob') else Status.NotInstalled
    )

]
