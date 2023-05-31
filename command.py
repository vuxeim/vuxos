from __future__ import annotations
from typing import Callable, TYPE_CHECKING
if TYPE_CHECKING: from shell import Shell

class CommandNotFound(Exception): ...
class NoRemainingArguments(Exception): ...

class Resolver:
    """
    Makes functions from *this* file
    conveniently available through
    class methods.

    A bit hacky.
    """

    _C: dict = {'': lambda _:...}

    def __init__(self) -> None:
        self._load()

    def _load(self):
        """
        Stores functions that starts with 'CMD_'
        from *this* file to a variable.
        """
        items = lambda: globals().items()
        is_fun = lambda fun: type(fun) == type(is_fun)
        rep = lambda name: name.replace('CMD_', '', 1)
        is_cmd = lambda name: name.startswith('CMD_')

        self._C |= {rep(n): f for n, f in items() if is_fun(f) and is_cmd(n)}

    def get(self, command: str) -> Callable:
        """
        Returns function corresponding
        to specified name.
        Raises CommandNotFound.
        """
        cmd = self._C.get(command, None)
        if cmd == None:
            raise CommandNotFound(command.join("''"))
        return cmd

def __pop_arg(*args: str) -> tuple[str, tuple[str, ...]]:
    """ Pop next argument from args list """
    if len(args) < 1:
        raise NoRemainingArguments
    return args[0], args[1:]

def __arg(*args: str) -> bool:
    """ Whether there are arguments left in list """
    if len(args) > 0:
        return True
    return False

def CMD_cd(shell: Shell, *args: str) -> None:
    """ Change directory command """
    if __arg(*args):
        path, args = __pop_arg(*args)
        shell.cwd = path
    else:
        shell.system.print(f"cd: Path not specified!")

def CMD_pwd(shell: Shell, *args: str) -> None:
    """ Print work directory command """
    shell.system.print(shell.cwd, raw=True)

def CMD_exit(shell: Shell, *args: str) -> None:
    """ Exit shell session """
    shell.interactive = False

def CMD_ls(shell: Shell, *args: str) -> None:
    """ List directory content """
    if __arg(*args):
        path, args = __pop_arg(*args)
    else:
        path = shell.cwd

    try:
        nodes = shell.system.filesystem.listdir(path)
    except FileNotFoundError:
        shell.system.print(f"ls: cannot access '{path}': No such file or directory")
    else:
        lines = [f"{n.type.lower()}: {n.name}" for n in nodes]
        shell.system.print('\n'.join(lines), raw=True)
