from typing import List, Tuple


def copy_file_with_special_variables(source: str, target: str, *vars: List[Tuple[str]]) -> None:
    '''
    Replaces variable placeholders with given values and copies the file to a new location.
    '''

    with open(source, 'r+') as fi, open(target, 'w+') as fo:

        file_contents = fi.read()

        for var in vars:
            variable_name = r'${' + var[0] + r'}'
            value = var[1]

            file_contents = file_contents.replace(variable_name, value)

        fo.write(file_contents)
