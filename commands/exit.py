from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from shell import Shell

class CMD_exit:
    """ Exit shell session """

    def __new__(cls, shell: Shell, *args: str) -> None:
        shell.interactive = False
