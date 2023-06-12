from __future__ import annotations
from typing import TYPE_CHECKING, Callable
if TYPE_CHECKING:
    from shell import Shell

from command import _arg, _pop_arg

class CMD_ls:
    """ List directory content """

    def __new__(cls, shell: Shell, *args: str) -> Callable:
        if _arg(*args):
            arg, args = _pop_arg(*args)
            if arg != '-l':
                l = False
                path = arg
            else:
                l = True
                if _arg(*args):
                    path, args = _pop_arg(*args)
                else:
                    path = shell.cwd
        else:
            l = False
            path = shell.cwd

        if shell.system.filesystem.exists(path):
            nodes = shell.system.filesystem.listdir(path)
            lines = [n.__repr__() if l else f"{n.type.capitalize()}: {n.name}" for n in nodes]
            shell.system.print('\n'.join(lines), raw=True)
        else:
            shell.system.print(f"ls: cannot access '{path}': No such file or directory")
