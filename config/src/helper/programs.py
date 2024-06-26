from typing import List, Union, Callable
from model import InstallationPackage, ProgramName, RAW_PROGRAM_NAME
from helper.ex import ex


def __gen_ex(merge: bool, command: str, program_name: Union[ProgramName, List[ProgramName]]):
    program_name = [x.name for x in program_name] if isinstance(program_name, list) else [program_name.name]
    if merge:
        return ex(command.format(' '.join(program_name)))
    else:
        return [ex(command.format(p)) == 0
                for p in program_name]


def __gen_is_installed(merge: bool, command: str, program_name: ProgramName):
    program_name = [x.executable for x in program_name] if isinstance(program_name, list) else [program_name.executable]
    if merge:
        return ex(command.format(' '.join(program_name)))
    else:
        return [ex(command.format(p)) == 0
                for p in program_name]


def __install_program(
    program_name: RAW_PROGRAM_NAME,
    install_command: str,
    uninstall_command: str,
    verify_installation: str,
    merge_map=None,
    additional_operation: Callable = None,
) -> InstallationPackage:
    if merge_map is None:
        merge_map = [False, False, False]
    program_name = ProgramName.from_raw(program_name)
    return InstallationPackage(
        install_func=lambda: __gen_ex(
            merge_map[0],
            install_command,
            program_name,
        ) and (additional_operation() if additional_operation else True),
        uninstall_func=lambda: __gen_ex(
            merge_map[1],
            uninstall_command,
            program_name,
        ),
        is_installed=lambda: __gen_is_installed(
            merge_map[2],
            verify_installation,
            program_name,
        ),
    )


def install_apt_program(program_name: RAW_PROGRAM_NAME, apt_repository: str = None) -> InstallationPackage:
    '''
    Installs given program(s) through Aptitude.
    '''
    additional_operation = None
    if apt_repository is not None:
        additional_operation = lambda: ex('add-apt-repository ' + apt_repository, sudo=True)
    return __install_program(
        program_name=program_name,
        install_command='sudo apt install -y {0}',
        uninstall_command='sudo apt remove -y {0}',
        verify_installation='command -v {0} >/dev/null || dpkg -s {0} 2>/dev/null >/dev/null',
        merge_map=[True, True, False],
        additional_operation=additional_operation,
    )


def install_python_program(program_name: RAW_PROGRAM_NAME) -> InstallationPackage:
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


def install_global_javascript_program(program_name: RAW_PROGRAM_NAME) -> InstallationPackage:
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


def pull_docker_image(program_name: RAW_PROGRAM_NAME) -> InstallationPackage:
    '''
    “Installs” as in downloads a Docker image with a given program pre-installed.
    '''
    return __install_program(
        program_name=program_name,
        install_command='docker pull {0}',
        uninstall_command='docker image rm {0}',
        verify_installation='docker image ls --format \'{{{{.Repository}}}}:{{{{.Tag}}}}\' | grep {0} >/dev/null',
        merge_map=[False, False, False],
    )
