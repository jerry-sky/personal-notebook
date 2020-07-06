from config_entries.config_entry import ConfigEntry
from config_entries.copy_some_lines import copy_some_lines
import shutil
import os
import pathlib
import re

HD = os.path.expanduser('~')
CD = str(pathlib.Path().absolute())


# shorthanded copy function
def cp(source, target, create_dirs=False, tree=False):
    if create_dirs:
        try:
            os.makedirs(target)
        except:
            pass
    if tree:
        shutil.copytree(source, target, copy_function=shutil.copy2)
    else:
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


config_entries = [
    ConfigEntry(
        description='append a few lines to .bashrc (changes PS1 and PATH)',
        shorthand='brc',
        execute=lambda: copy_some_lines(
            CD + '/config-files/.bashrc', HD + '/.bashrc')
    ),

    ConfigEntry(
        description='swap Control_R and Menu keys (good for keyboards without a dedicated Menu key)',
        shorthand='kym',
        execute=lambda: copy_some_lines(
            CD + '/config-files/.key_remap', HD + '/.bashrc')
    ),

    ConfigEntry(
        description='copy .bash_aliases',
        shorthand='bas',
        execute=lambda: cp(CD + '/config-files/.bash_aliases', HD + '/')
    ),

    ConfigEntry(
        description='copy .bash_aliases but with `code-insiders` instead of `code`',
        shorthand='bas-insiders',
        execute=bash_aliases_insiders
    ),

    ConfigEntry(
        description='copy redshift config file',
        shorthand='rds',
        execute=lambda: cp(
            CD + '/config-files/redshift.conf', HD + '/.config/')
    ),

    ConfigEntry(
        description='copy Vivaldi browser.html file',
        shorthand='viv',
        execute=lambda: cp(CD + '/config-files/vivaldi/browser.html',
                           '/opt/vivaldi/resources/vivaldi/')
    ),

    ConfigEntry(
        description='copy neovim init file',
        shorthand='nvi',
        execute=lambda: cp(CD + '/config-files/nvim/init.vim',
                           HD + '/.config/nvim/', create_dirs=True)
    ),

    ConfigEntry(
        description='copy java formatter file',
        shorthand='jav',
        execute=lambda: cp(
            CD + '/config-files/java-formatter.xml', HD + '/.config/')
    ),

    ConfigEntry(
        description='copy menu icon file',
        shorthand='men',
        execute=lambda: cp(
            CD + '/config-files/menu-icon.png', '/usr/share/icons/')
    ),

    ConfigEntry(
        description='load Cinnamon keyboard shortcuts',
        shorthand='cks',
        execute=lambda: ex(
            'dconf load /org/cinnamon/desktop/keybindings/ < ./config-files/cinnamon-keyboard-shortcuts.conf')
    ),

    ConfigEntry(
        description='copy utility scripts',
        shorthand='cus',
        execute=lambda: cp(CD + '/utility-scripts',
                           '/opt/utility-scripts', tree=True)
    ),

    ConfigEntry(
        description='set IBus icon colour',
        shorthand='ibu',
        execute=lambda: ex(
            '/usr/bin/gsettings set org.freedesktop.ibus.panel xkb-icon-rgba "#cfcfcf"')
    ),


]
