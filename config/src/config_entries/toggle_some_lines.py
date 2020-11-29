from config_entries.config_entry import ConfigEntry

SCRIPT_INITIATOR = lambda source_file, target_file: '# BEGIN ' + source_file + ' -> ' + target_file + '\n'

SCRIPT_TERMINATOR = lambda source_file, target_file: '# END ' + source_file + ' -> ' + target_file + '\n'


def toggle_some_lines(source_file: str, target_file: str):
    '''
    Copies all lines from a source file and appends them to the target file;
    if the lines are already there, removes them.
    '''

    si = SCRIPT_INITIATOR(source_file, target_file)
    st = SCRIPT_TERMINATOR(source_file, target_file)

    with open(target_file, 'r') as f:
        lines = f.readlines()

    if si in lines and st in lines:
        # if the lines are already there, remove them
        begin_index = lines.index(si)
        end_index = lines.index(st)
        lines = lines[:begin_index] + lines[end_index+1:]

    else:
        # add the script's lines
        with open(source_file, 'r') as fi:
            lines += [si]
            lines += fi.readlines()
            lines += [st]

    with open(target_file, 'w') as fo:
        fo.writelines(lines)


def check_if_lines_present(source_file: str, target_file: str):
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

