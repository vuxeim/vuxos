from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from shell import Shell
    from path import Path
from command import arg, pop_arg


class CMD_cd:
    """ Change directory command """

    CMD = 'cd'

    def not_a_directory(self) -> None:
        path_name = self.path.raw_path
        self.sys_print(f"{self.CMD}: not a directory: {path_name}")

    def no_such_directory(self) -> None:
        path_name = self.path.raw_path
        self.sys_print(f"{self.CMD}: no such file or directory: {path_name}")

    def set_cwd(self, path: Path) -> None:
        self.shell.cwd = path

    def __init__(self, shell: Shell, *args: str) -> None:
        self.shell = shell
        self.sys_print = self.shell.system.print
        fs = shell.system.filesystem

        if not arg(*args):
            self.path = self.shell.pathify('~')
            return self.set_cwd(self.path)

        path, args = pop_arg(*args)
        self.path = self.shell.pathify(path)

        if not fs.exists(self.path):
            return self.no_such_directory()

        if not fs.get_node_at(self.path).is_dir():
            return self.not_a_directory()

        return self.set_cwd(self.path)
