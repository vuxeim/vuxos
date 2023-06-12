from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from shell import Shell

from command import _arg, _pop_arg

class CMD_parent:

    def unknown_argument(self) -> None:
        self.shell.system.print(f"Unknown argument: {self.arg}")

    def __init__(self, shell: Shell, *args: str) -> None:
        self.shell = shell
        fs = shell.system.filesystem

        if _arg(*args):
            self.arg, args = _pop_arg(*args)
            return self.unknown_argument()

        parent = fs.get_node_at(shell.cwd).parent
        shell.system.print(f".. = {parent}")
