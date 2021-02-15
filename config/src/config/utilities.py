from typing import List, Tuple
import os
from config.config_entry import ConfigEntry


def SCRIPT_INITIATOR(source_file, target_file):
    '''
    Generates a fileblock `BEGIN` line.
    '''
    return '# BEGIN ' + \
        source_file + ' -> ' + target_file + '\n'


def SCRIPT_TERMINATOR(source_file, target_file):
    '''
    Generates a fileblock `END` line.
    '''
    return '# END ' + \
        source_file + ' -> ' + target_file + '\n'


def toggle_fileblock(source_file: str, target_file: str, state=None):
    '''
    Copies all contents of the source file and appends them
    to the target file as a “file block”.
    If the file block is already present in the target file
    the function removes it.

    `state` argument:
        - `None` — toggle
        - `True` — (re)install
        - `False` — uninstall (do nothing)

    Copied lines are wrapped with additional special lines that
    indicate where the file block begins and ends.

    ---

    Example:

    `source-file.txt`<<EOF:
    ```txt
    VARIABLE='value'
    EOF
    ```

    ---

    The modified target file `target-file.txt`<<EOF:
    ```txt
    target file header

    target file contents

    # BEGIN source-file.txt -> target-file.txt
    VARIABLE='value'
    # END source-file.txt -> target-file.txt
    EOF
    ```

    '''

    si = SCRIPT_INITIATOR(source_file, target_file)
    st = SCRIPT_TERMINATOR(source_file, target_file)

    fileblock = []

    with open(target_file, 'r') as f:
        # read the source file
        fileblock = f.readlines()

    fileblock_present = si in fileblock and st in fileblock

    # compute state
    if state is None:
        # toggle
        if fileblock_present:
            state = False
        else:
            state = True
    elif state:
        # install
        if fileblock_present:
            state = None
        else:
            state = True
    else:
        # uninstall
        if fileblock_present:
            state = False
        else:
            state = None

    if state == True:  # explicit — state can be `None`
        # add the fileblock to the target file
        with open(source_file, 'r') as fi:
            fileblock += [si]
            fileblock += fi.readlines()
            fileblock += [st]

    elif state == False:  # explicit — state can be `None`
        # remove the fileblock
        begin_index = fileblock.index(si)
        end_index = fileblock.index(st)
        fileblock = fileblock[:begin_index] + fileblock[end_index+1:]

    # write the changes ot the target file
    with open(target_file, 'w') as fo:
        fo.writelines(fileblock)


def does_contain_file_block(source_file: str, target_file: str):
    '''
    Verifies if the contents of the source file are in the target file.
    '''

    si = SCRIPT_INITIATOR(source_file, target_file)
    st = SCRIPT_TERMINATOR(source_file, target_file)

    with open(target_file, 'r') as f:
        lines = f.readlines()

    if si in lines and st in lines:
        return True
    else:
        return False


def copy_file_with_special_variables(source: str, target: str, vars: List[Tuple[str]]) -> None:
    '''
    Replaces variable placeholders with given values in the source
    file and copies the file to a new location.
    (the source file remains unchanged of course)
    '''

    with open(source, 'r+') as fi, open(target, 'w+') as fo:

        file_contents = fi.read()

        for var in vars:
            variable_name = r'${' + var[0] + r'}'
            value = var[1]

            file_contents = file_contents.replace(variable_name, value)

        fo.write(file_contents)


def do_files_partially_overlap(source_file: str, target_file: str) -> bool:
    '''
    Checks if the target file contains all lines of the source file
    (in the correct order).
    '''

    target_lines = []
    source_lines = []

    try:
        with open(target_file, 'r') as f:
            target_lines = f.readlines()
    except FileNotFoundError as e:
        return False

    with open(source_file, 'r') as f:
        source_lines = f.readlines()

    return do_lists_partially_overlap(source_lines, target_lines)


def do_lists_partially_overlap(source_list: List, target_list: List) -> bool:
    '''
    Checks if the target list contains all lines of the source list.
    '''
    if [x for x in target_list if x in source_list] == source_list:
        return True
    else:
        return False
