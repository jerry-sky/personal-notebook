from config_entries.config_entry import ConfigEntry


def copy_some_lines(source_file: str, target_file: str):
    '''Copies all lines from a source file and appends them to the target file;
    if the lines are already there, removes them.
    '''

    SCRIPT_INITIATOR = '# BEGIN ' + source_file + ' -> ' + target_file + '\n'

    SCRIPT_TERMINATOR = '# END ' + source_file + ' -> ' + target_file + '\n'

    with open(target_file, 'r') as f:
        lines = f.readlines()

    if SCRIPT_INITIATOR in lines and SCRIPT_TERMINATOR in lines:
        # if the lines are already there, remove them
        begin_index = lines.index(SCRIPT_INITIATOR)
        end_index = lines.index(SCRIPT_TERMINATOR)
        lines = lines[:begin_index] + lines[end_index+1:]

    else:
        # add the script's lines
        with open(source_file, 'r') as fi:
            lines += [SCRIPT_INITIATOR]
            lines += fi.readlines()
            lines += [SCRIPT_TERMINATOR]

    with open(target_file, 'w') as fo:
        fo.writelines(lines)

