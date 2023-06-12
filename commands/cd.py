from __future__ import annotations
from typing import TYPE_CHECKING, Callable
if TYPE_CHECKING:
    from shell import Shell

from command import _arg, _pop_arg

class CMD_cd:
    """ Change directory command """

    def __new__(cls, shell: Shell, *args: str) -> Callable:
        if not _arg(*args):
            shell.cwd = f"/home/{shell.user.name}"
            return

        fs = shell.system.filesystem

        path, args = _pop_arg(*args)

        if path == "~":
            shell.cwd = f"/home/{shell.user.name}"
            return

        if path.startswith('/'):
            if fs.exists(path):
                if not fs.get_node_at(path).is_dir():
                    shell.system.print(f"cd: not a directory: {path}")
                    return
                shell.cwd = path
                return
        else:
            new_path = (shell.cwd if shell.cwd != '/' else '')+'/'+path
            if fs.exists(new_path):
                if not fs.get_node_at(new_path).is_dir():
                    shell.system.print(f"cd: not a directory: {path}")
                    return
                shell.cwd = new_path
                return

        shell.system.print(f"cd: no such file or directory: {path}")

