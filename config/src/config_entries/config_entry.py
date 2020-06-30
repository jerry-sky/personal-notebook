from typing import NamedTuple
from types import FunctionType

class ConfigEntry(NamedTuple):
    '''
    Attributes:
    - description: short description of the config entry
    - shorthand: command-like short string that will invoke this config entry
    - execute: the function to execute
    '''

    description: str
    shorthand: str
    execute: FunctionType

