from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from shell import Shell

from command import _arg, _pop_arg

class CMD_parent:
    """ Prints parent directory """

    CMD = 'parent'

    def unknown_argument(self) -> None:
        self.sys_print(f'{self.CMD}: Unknown argument: {self.arg}')

    def no_parent(self) -> None:
        self.sys_print(f'{self.CMD}: \'/\' is the root of the filesystem')

    def __init__(self, shell: Shell, *args: str) -> None:
        self.shell = shell
        self.sys_print = self.shell.system.print
        fs = shell.system.filesystem

        if _arg(*args):
            self.arg, args = _pop_arg(*args)
            return self.unknown_argument()

        node = fs.get_node_at(shell.cwd)
        parent = node.parent
        if parent == None:
            if node.name != '/':
                raise Exception("Non-root node does not have parent")
            return self.no_parent()

        self.sys_print(f".. = {parent}")
