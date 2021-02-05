from typing import NamedTuple, Union, List
from types import FunctionType
from dataclasses import dataclass
from enum import Enum

class Status(Enum):
    NotInstalled = 0
    Installed = 1
    Unknown = 2


@dataclass
class ConfigEntry:
    '''
    Attributes:
    - description: short description of the config entry
    - shorthand: command-like short string that will invoke this config entry
    - execute: the function to execute
    - is_installed: indicator whether the entry is already installed
    '''

    description: str
    shorthand: str
    execute: Union[FunctionType, List[FunctionType]]
    is_installed: FunctionType = lambda: Status.Unknown
