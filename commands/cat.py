from __future__ import annotations
from typing import Callable, TYPE_CHECKING
if TYPE_CHECKING:
    from shell import Shell

from command import _arg, _pop_arg

class CMD_cat:
    """ Print file content """

    def __new__(cls, shell: Shell, *args: str) -> Callable:

        specify_name = lambda: shell.system.print(f"cat: Please specify file name")
        is_directory = lambda path: shell.system.print(f"cat: {path}: Is a directory")
        no_file = lambda path: shell.system.print(f"cat: {path}: No such file or directory")
        sys_print = lambda content: shell.system.print(content, raw=True)

        if not _arg(*args):
            return specify_name()

        path, args = _pop_arg(*args)

        if path in ('~'):
            return is_directory(path)

        if not path.startswith('/'):
            path = (shell.cwd if shell.cwd != '/' else '')+'/'+path

        if shell.system.filesystem.exists(path):
            node = shell.system.filesystem.get_node_at(path)
            if not node.is_file():
                return is_directory(path)
        else:
            return no_file(path)

        return sys_print(node.content)


