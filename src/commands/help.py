from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from shell import Shell


class CMD_help:
    """ List all available commands """

    def __init__(self, shell: Shell, *args: str) -> None:
        for cmd in shell.resolver.get_list():
            shell.system.print(f'{cmd.CMD} => {cmd.DOC.strip()}')
