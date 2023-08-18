from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from shell import Shell
from command import arg


class CMD_touch:
    """ Create file """
    # TODO Update modification time of file

    CMD = 'touch'

    def specify_name(self) -> None:
        self.sys_print(f"{self.CMD}: missing file operand")

    def __init__(self, shell: Shell, *args: str) -> None:
        self.sys_print = shell.system.print

        if not arg(*args):
            return self.specify_name()

        self.sys_print('plz implement me')
