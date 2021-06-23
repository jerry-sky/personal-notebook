from helper.ex import ex
import os
from model import InstallationPackage


def __toggle_file_links(source: str, target: str, sudo: bool = False):
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
        ex('ln -fs -- ' + source + ' ' + target, sudo)


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
