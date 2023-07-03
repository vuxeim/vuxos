from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from shell import Shell

from command import _arg, _pop_arg

class CMD_cat:
    """ Print file content """

    CMD = "cat"

    def specify_name(self) -> None:
        self.sys_print(f"{self.CMD}: Please specify file name")

    def is_directory(self) -> None:
        name = self.path.raw_path
        self.sys_print(f"{self.CMD}: {name}: Is a directory")

    def no_file(self) -> None:
        name = self.path.raw_path
        self.sys_print(f"{self.CMD}: {name}: No such file or directory")

    def __init__(self, shell: Shell, *args: str) -> None:
        self.shell = shell
        self.sys_print = self.shell.system.print
        fs = shell.system.filesystem

        if not _arg(*args):
            return self.specify_name()

        path, args = _pop_arg(*args)
        self.path = self.shell.pathify(path)

        if not fs.exists(self.path):
            return self.no_file()

        node = fs.get_node_at(self.path)

        if not node.is_file():
            return self.is_directory()

        return self.sys_print(node.content)
