from typing import List, Union
from model import InstallationPackage
from helper.ex import ex


PROGRAM_NAME = Union[str, List[str]]


def __gen_ex(merge: bool, command: str, program_name):
    if merge:
        return lambda: ex(command.format(' '.join(program_name)))
    else:
        return lambda: [ex(command.format(p)) == 0
                        for p in program_name]


def __install_program(
    program_name: PROGRAM_NAME,
    install_command: str,
    uninstall_command: str,
    verify_installation: str,
    merge_map: List[bool] = [False, False, False],
) -> InstallationPackage:

    if isinstance(program_name, list):
        return InstallationPackage(
            install_func=__gen_ex(
                merge_map[0],
                install_command,
                program_name,
            ),
            uninstall_func=__gen_ex(
                merge_map[1],
                uninstall_command,
                program_name,
            ),
            is_installed=__gen_ex(
                merge_map[2],
                verify_installation,
                program_name,
            ),
        )

    else:
        return InstallationPackage(
            install_func=lambda: ex(install_command.format(program_name)),
            uninstall_func=lambda: ex(uninstall_command.format(program_name)),
            is_installed=lambda: ex(verify_installation.format(program_name)) == 0,
        )


def install_apt_program(program_name: PROGRAM_NAME) -> InstallationPackage:
    '''
    Installs given program(s) through Aptitude.
    '''
    return __install_program(
        program_name=program_name,
        install_command='sudo apt install -y {0}',
        uninstall_command='sudo apt remove -y {0}',
        verify_installation='command -v {0} >/dev/null || dpkg -s {0} 2>/dev/null >/dev/null',
        merge_map=[True, True, False],
    )


def install_python_program(program_name: PROGRAM_NAME) -> InstallationPackage:
    '''
    Installs given program(s) through Python installer (PIP).
    '''
    return __install_program(
        program_name=program_name,
        install_command='python3 -m pip install {0}',
        uninstall_command='python3 -m pip uninstall {0}',
        verify_installation='python3 -m pip show {0} 2>/dev/null >/dev/null',
        merge_map=[True, True, False],
    )


def install_global_javascript_program(program_name: PROGRAM_NAME) -> InstallationPackage:
    '''
    Installs given program(s) through the default JavaScript package manager (NPM).
    '''
    return __install_program(
        program_name=program_name,
        install_command='npm install -g {0}',
        uninstall_command='npm uninstall -g {0}',
        verify_installation='npm ls -g 2>/dev/null | grep {0} >/dev/null',
        merge_map=[True, True, False],
    )


def pull_docker_image(program_name: PROGRAM_NAME) -> InstallationPackage:
    '''
    “Installs” as in downloads a Docker image with a given program pre-installed.
    '''
    return __install_program(
        program_name=program_name,
        install_command='docker pull {0}',
        uninstall_command='docker image rm {0}',
        verify_installation='docker image ls | grep {0} >/dev/null',
        merge_map=[False, False, False],
    )
