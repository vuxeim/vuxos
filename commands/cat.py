from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from shell import Shell

from command import _arg, _pop_arg

class CMD_cat:
    """ Print file content """

    def specify_name(self) -> None:
        self.shell.system.print(f"cat: Please specify file name")

    def is_directory(self) -> None:
        self.shell.system.print(f"cat: {self.path}: Is a directory")

    def no_file(self) -> None:
        self.shell.system.print(f"cat: {self.path}: No such file or directory")

    def sys_print(self, text: str) -> None:
        self.shell.system.print(text)

    def __init__(self, shell: Shell, *args: str) -> None:
        self.shell = shell

        if not _arg(*args):
            return self.specify_name()

        self.path, args = _pop_arg(*args)
        fs = shell.system.filesystem

        # TODO: find better solution
        if self.path == '~':
            return self.is_directory()

        if not self.path.startswith('/'):
            self.path = (shell.cwd if shell.cwd != '/' else '')+'/'+self.path

        if not fs.exists(self.path):
            return self.no_file()

        node = fs.get_node_at(self.path)

        if not node.is_file():
            return self.is_directory()

        return self.sys_print(node.content)
