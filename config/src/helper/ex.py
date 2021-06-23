import os


def ex(command: str, sudo: bool = False):
    '''
    Executes given command using the system shell.
    '''
    return os.system(
        ('sudo ' if sudo else '')
        + command
    )
