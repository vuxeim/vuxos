from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from shell import Shell

from command import _arg, _pop_arg

class CMD_ls:
    """ List directory content """

    CMD = 'ls'

    def no_such_file_or_dir(self) -> None:
        name = self.path.raw_path
        msg = f"{self.CMD}: cannot access '{name}': No such file or directory"
        self.sys_print(msg)

    def __init__(self, shell: Shell, *args: str) -> None:
        self.shell = shell
        self.sys_print = self.shell.system.print
        fs = shell.system.filesystem

        if _arg(*args):
            arg, args = _pop_arg(*args)
            if arg != '-l':
                flag_l = False
                self.path = self.shell.pathify(arg)
            else:
                flag_l = True
                if _arg(*args):
                    path, args = _pop_arg(*args)
                    self.path = self.shell.pathify(path)
                else:
                    self.path = shell.cwd
        else:
            flag_l = False
            self.path = shell.cwd

        if not fs.exists(self.path):
            return self.no_such_file_or_dir()

        fmt = lambda node: f"{node.type.capitalize()}: {node.name}"
        get_line = lambda node: node.__repr__() if flag_l else fmt(node)
        lines = [get_line(n) for n in fs.listdir(self.path)]

        return self.sys_print('\n'.join(lines))
