from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from shell import Shell

from command import _arg, _pop_arg

class CMD_cd:
    """ Change directory command """

    def not_directory(self) -> None:
        self.shell.system.print(f"cd: not a directory: {self.path}")

    def no_such_directory(self) -> None:
        self.shell.system.print(f"cd: no such file or directory: {self.path}")

    def set_cwd(self, path: str) -> None:
        self.shell.cwd = path

    def sys_print(self, text: str) -> None:
        self.shell.system.print(text)

    def __init__(self, shell: Shell, *args: str) -> None:
        self.shell = shell

        if not _arg(*args):
            return self.set_cwd(f"/home/{shell.user.name}")

        self.path, args = _pop_arg(*args)
        fs = shell.system.filesystem

        if self.path == "~":
            return self.set_cwd(f"/home/{shell.user.name}")

        if not self.path.startswith('/'):
            self.path = (shell.cwd if shell.cwd != '/' else '')+'/'+self.path

        if not fs.exists(self.path):
            return self.no_such_directory()

        if not fs.get_node_at(self.path).is_dir():
            return self.not_directory()

        return self.set_cwd(self.path)
