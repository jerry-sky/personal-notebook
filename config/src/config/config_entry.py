from typing import Union, List
from types import FunctionType
from enum import Enum


class Status(Enum):
    NotInstalled = 0
    Installed = 1
    Unknown = 2


class ConfigEntry(object):
    '''
    A config entry that describes installation of a particular component
    of the user’s environment.
    '''

    __description: str
    __shorthand: str
    __execute_funcs: Union[FunctionType, List[FunctionType]]
    __is_installed_funcs: FunctionType = lambda: Status.Unknown
    __toggable: bool

    def __init__(self, description: str, shorthand: str, execute: List[FunctionType], is_installed: List[FunctionType], toggable: bool = True):
        self.__description = description
        self.__shorthand = shorthand
        self.__is_installed_funcs = is_installed
        self.__execute_funcs = execute
        self.__toggable = toggable

    @property
    def description(self):
        '''
        Short description of the config entry.
        '''
        return self.__description

    @property
    def shorthand(self):
        '''
        Command-like short name that will invoke this config entry.
        '''
        return self.__shorthand

    @property
    def is_installed(self) -> Status:
        '''
        Returns the collective state of the entry given all provided
        `is_installed` functions.
        '''

        status = Status.Installed
        for f in self.__is_installed_funcs:
            o = f()
            if o == Status.NotInstalled:
                return Status.NotInstalled

            elif o == Status.Unknown:
                status = Status.Unknown

        return status

    def execute(self) -> None:
        '''
        Executes all given `execute` functions.
        '''
        reached = 0
        try:
            for f in self.__execute_funcs:
                f()
                reached += 1

        except Exception as e:
            # should an error occur, the functions that were already
            # executed need to be exected once more;
            # this is not a problem for functions that are toggable
            # — meaning they can “turn the thing off” after
            # it has been “turned on”
            if self.__toggable:
                for j in range(0, reached):
                    self.__execute_funcs[j]()

            # raise the exception again for later error handling
            raise e
