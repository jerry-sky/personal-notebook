from typing import Union, List
from types import FunctionType
from enum import Enum


class Status(Enum):
    NotInstalled = 0
    Installed = 1
    Unknown = 2


class InstallationPackage(object):
    '''
    This class is essentially a named tuple of three functions:
    - `install`,
    - `uninstall`,
    - `is_installed`,
    which manage a particular part of a particular config entry be it
    a config file or installation of a program.
    '''

    __install: FunctionType
    __uninstall: FunctionType
    __is_installed: FunctionType
    __is_immutable: bool

    def __init__(self, install_func: FunctionType, uninstall_func: FunctionType = None, is_installed: FunctionType = None):
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
        self.__install

    def uninstall(self) -> None:
        '''
        Runs the functions that uninstall this package.
        '''
        self.__uninstall

    @property
    def is_installed(self) -> None:
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


class ConfigEntry(object):
    '''
    A config entry that describes installation of a particular component
    of the user’s environment.
    '''

    __description: str
    __shorthand: str
    __installation_packages: List[InstallationPackage]

    def __init__(self, description: str, shorthand: str, installation_packages: Union[List[InstallationPackage], InstallationPackage]):
        self.__description = description
        self.__shorthand = shorthand

        # ensure it is a list of installation packages
        if type(installation_packages) is list:
            self.__installation_packages = installation_packages
        else:
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
        status = Status.Installed
        for i in self.__installation_packages:
            o = i.is_installed
            if o == Status.NotInstalled:
                return Status.NotInstalled

            elif o == Status.Unknown:
                status = Status.Unknown

        return status

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

    def install(self) -> None:
        '''
        Installs all installation packages related to this config entry.
        '''
        for i in self.__installation_packages:
            i.install()

    def uninstall(self) -> None:
        '''
        Uninstalls all installation packages related to this config entry.
        '''
        if self.is_immutable:
            return

        for i in self.__installation_packages:
            i.uninstall()
