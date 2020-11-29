from typing import List
import os

def do_files_overlap(source_file: str, target_file: str) -> bool:
    '''
    Checks if the target file contains all lines of the source file (in the correct order).
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

    return do_lists_overlap(source_lines, target_lines)


def do_lists_overlap(source_list: List, target_list: List) -> bool:
    if [x for x in target_list if x in source_list] == source_list:
        return True
    else:
        return False
