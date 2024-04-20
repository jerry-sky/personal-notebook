import os

from helper.ex import ex
from model import InstallationPackage


def __toggle_file_links(source: str, target: str, sudo: bool = False):
    '''
    Creates a symbolic link in the target directory to the file
    in the source directory.
    '''

    if os.path.isdir(source):
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
        ex('mkdir -p -- ' + os.path.dirname(target), sudo)
        ex('ln -s -- ' + source + ' ' + target, sudo)


def __remove_file_links(source: str, target: str, sudo: bool = False):
    '''
    Removes all symbolic links present in the target directory defined by the source directory.
    '''

    if os.path.isdir(source) and os.path.isdir(target):
        for l in os.listdir(source):
            p = os.path.join(target, l)
            ex('rm -f -- ' + p, sudo)
    else:
        ex('rm -rf -- ' + target, sudo)


def toggle_file_links(source: str, target: str, sudo: bool = False):
    '''
    Creates links to a provided file or files in a directory or deletes
    them if they exist.

    Returns an `InstallationPackage`.
    '''
    return InstallationPackage(
        install_func=lambda: __toggle_file_links(source, target, sudo),
        uninstall_func=lambda: ex('rm -rf -- ' + target, sudo),
        is_installed=lambda: True if os.path.exists(target) else False
    )


def toggle_dir_link(source: str, target: str, sudo: bool = False):
    '''
    Creates link to provided directory in another location.
    '''
    return InstallationPackage(
        install_func=lambda: ex('ln -s -- ' + source + ' ' + target, sudo),
        uninstall_func=lambda: ex('rm -f -- ' + target, sudo),
        is_installed=lambda: True if os.path.exists(target) else False,
    )


def toggle_desktop_file_links(source: str, target: str):
    '''
    Does the same thing as `toggle_file_links` and updated the desktop database.
    '''
    sudo = True
    return InstallationPackage(
        install_func=lambda: __toggle_file_links(source, target, sudo) and ex('sudo update-desktop-database'),
        uninstall_func=lambda: __remove_file_links(source, target, sudo) and ex('sudo update-desktop-database'),
        is_installed=lambda: True if os.path.exists(target) else False
    )
