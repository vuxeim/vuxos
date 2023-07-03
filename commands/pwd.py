from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from shell import Shell

class CMD_pwd:
    """ Prints work directory command """

    CMD = 'pwd'

    def __init__(self, shell: Shell, *args: str) -> None:
        shell.system.print(shell.cwd.absolute)
