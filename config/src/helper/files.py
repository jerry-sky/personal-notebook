from typing import List, Tuple
from model import InstallationPackage
from helper.ex import ex


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


def copy_file_with_special_variables(source: str, target: str, vars: List[Tuple[str, str]]) -> None:
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


def __toggle_fileblock(
    source_file_path: str,
    target_file_path: str,
    state: bool = None,
    sudo: bool = False,
    line_number_location: int = None
):
    si = SCRIPT_INITIATOR(source_file_path, target_file_path)
    st = SCRIPT_TERMINATOR(source_file_path, target_file_path)

    target_file_contents = []

    with open(target_file_path, 'r') as f:
        # read the source file
        target_file_contents = f.readlines()

    fileblock_present = si in target_file_contents and st in target_file_contents

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
        fileblock = []
        with open(source_file_path, 'r') as fi:
            fileblock += [si]
            fileblock += fi.readlines()
            fileblock += [st]
        # add the fileblock to the target file
        if line_number_location is not None:
            # inject fileblock at a specific location in the file
            target_file_contents = target_file_contents[0:line_number_location] \
                + fileblock \
                + target_file_contents[line_number_location:]
        else:
            target_file_contents += fileblock

    elif state == False:  # explicit — state can be `None`
        # remove the fileblock
        begin_index = target_file_contents.index(si)
        end_index = target_file_contents.index(st)
        target_file_contents = target_file_contents[:begin_index] + \
            target_file_contents[end_index+1:]

    # write the changes to the target file
    ex(
        'cat <<\'EOF\' |'
        + ('sudo ' if sudo else '')
        + 'tee >/dev/null '
        + target_file_path
        + '\n'
        + ''.join(target_file_contents)
        + 'EOF'
    )


def toggle_fileblock(source: str, target: str, sudo: bool = False, line_number_location: int = None):
    '''
    Copies all contents of the source file and appends them
    to the target file as a “file block”.
    If the file block is already present in the target file
    the function removes it.

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

    return InstallationPackage(
        install_func=lambda: __toggle_fileblock(source, target, True, sudo=sudo, line_number_location=line_number_location),
        uninstall_func=lambda: __toggle_fileblock(source, target, False, sudo=sudo),
        is_installed=lambda: does_contain_file_block(source, target)
    )
