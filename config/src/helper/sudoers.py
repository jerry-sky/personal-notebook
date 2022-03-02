from env import USER
from helper.ex import ex
from model import InstallationPackage


def sudoers_nopasswd(program: str):
    '''
    Creates a file in `/etc/sudoers.d` that allows running given program
    with root privileges without providing password.
    '''
    return InstallationPackage(
        install_func=lambda: ex(f'''
            printf "%s\n" "{USER} ALL=(root) NOPASSWD: `whereis {program} | awk '{{print $2}}'`" \\
                | sudo tee /etc/sudoers.d/{program} >/dev/null
        '''),
        uninstall_func=lambda: ex(f'sudo rm /etc/sudoers.d/{program}'),
        is_installed=lambda: ex(f'test -f /etc/sudoers.d/{program}') == 0,
    )
