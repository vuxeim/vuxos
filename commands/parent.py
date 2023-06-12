from __future__ import annotations
from typing import TYPE_CHECKING, Callable
if TYPE_CHECKING:
    from shell import Shell

from command import _arg, _pop_arg

class CMD_parent:
    def __new__(cls, shell: Shell, *args: str) -> Callable:
        if _arg(*args):
            arg, args = _pop_arg(*args)
            shell.system.print(f"Unknown argument: {arg}")
            return

        pwd = shell.cwd
        parent = shell.system.filesystem.get_node_at(pwd).parent
        shell.system.print(f".. = {parent}")
