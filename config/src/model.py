from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import Callable, Union, List


class Status(Enum):
    NotInstalled = 0
    Installed = 1
    Unknown = 2


@dataclass
class InstallationPackage:
    '''
    This class is essentially a named tuple of three functions:
    - `install`,
    - `uninstall`,
    - `is_installed`,
    which manage a particular part of a particular config entry be it
    a config file or installation of a program.
    '''

    __install: Callable
    __uninstall: Callable
    __is_installed: Callable
    __is_immutable: bool

    def __init__(self, install_func: Callable, uninstall_func: Callable = lambda: None,
                 is_installed: Callable = lambda: None):
        self.__install = install_func
        self.__is_installed = is_installed

        # if no uninstall function provided, mark it as immutable
        if uninstall_func is None:
            self.__uninstall = lambda: None
            self.__is_immutable = True
        else:
            self.__uninstall = uninstall_func
            self.__is_immutable = False

    def install(self) -> None:
        '''
        Runs the function that install this package.
        '''
        self.__install()

    def uninstall(self) -> None:
        '''
        Runs the functions that uninstall this package.
        '''
        self.__uninstall()

    @property
    def is_installed(self) -> Status:
        '''
        Returns the status of the package.
        '''
        if self.__is_installed is None:
            return Status.Unknown
        else:
            output = self.__is_installed()
            if type(output) is list:
                return Status.Installed if sum(output) == len(output) else Status.NotInstalled
            else:
                return Status.Installed if output else Status.NotInstalled

    @property
    def is_immutable(self) -> bool:
        '''
        Nature of the package — if `True` it cannot be
        uninstalled (automatically).
        '''
        return self.__is_immutable


class ConfigEntry:
    '''
    A config entry that describes installation of a particular component
    of the user’s environment.
    '''

    __description: str
    __shorthand: str
    __installation_packages: List[InstallationPackage]
    __child_entries: List = []

    def __init__(
        self,
        description: str,
        shorthand: str,
        installation_packages: Union[List[InstallationPackage], InstallationPackage],
        child_entries: List = [],
    ):
        self.__description = description
        self.__shorthand = shorthand
        self.__child_entries = child_entries

        # ensure it is a list of installation packages
        if type(installation_packages) is list:
            self.__installation_packages = installation_packages
        elif type(installation_packages) is InstallationPackage:
            self.__installation_packages = [installation_packages]

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
        for i in self.__installation_packages:
            o = i.is_installed
            if o == Status.NotInstalled:
                return Status.NotInstalled
            elif o == Status.Unknown:
                return Status.Unknown
        return Status.Installed

    @property
    def installation_packages(self) -> List[InstallationPackage]:
        return self.__installation_packages

    @property
    def is_immutable(self) -> bool:
        '''
        Nature of the config entry — if `True` then the entry cannot
        be uninstalled.
        '''
        for i in self.__installation_packages:
            if i.is_immutable:
                return True

        return False

    def install(self, skip_already_installed=False) -> None:
        '''
        Installs all installation packages related to this config entry.
        '''
        for i in self.__installation_packages:
            if not (skip_already_installed and i.is_installed):
                i.install()

    def uninstall(self) -> None:
        '''
        Uninstalls all installation packages related to this config entry.
        '''
        # uninstall child entries first
        for c in self.__child_entries:
            c.uninstall()
        # uninstall self
        if self.is_immutable:
            return
        else:
            for i in self.__installation_packages:
                i.uninstall()


@dataclass
class ConfigEntryGroup:
    name: str
    list: List[ConfigEntry]


ConfigEntries = List[ConfigEntryGroup]


@dataclass
class ProgramName:
    name: str
    executable: str | None = None

    def __init__(self, name, executable=None):
        self.name = name
        self.executable = executable if executable is not None else name

    @staticmethod
    def from_raw(r: RAW_PROGRAM_NAME) -> Union[ProgramName, List[ProgramName]]:
        if isinstance(r, list):
            return [ProgramName.from_raw(x) for x in r]
        elif isinstance(r, str):
            return ProgramName(r, r)
        elif isinstance(r, ProgramName):
            return r


RAW_PROGRAM_NAME = Union[str, ProgramName, List[Union[str, ProgramName]]]
