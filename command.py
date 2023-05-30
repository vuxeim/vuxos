from __future__ import annotations
from typing import Callable, TYPE_CHECKING
if TYPE_CHECKING: from shell import Shell

class CommandNotFound(Exception): ...
class NotEnaughArguments(Exception): ...

class Resolver:

    _C: dict = {'': lambda _:...}

    def __init__(self) -> None:
        items = lambda: globals().items()
        is_fun = lambda fun: type(fun) == type(is_fun)
        rep = lambda name: name.replace('CMD_', '', 1)
        is_cmd = lambda name: name.startswith('CMD_')

        self._C |= {rep(n): f for n, f in items() if is_fun(f) and is_cmd(n)}

    def get(self, command: str) -> Callable:
        cmd = self._C.get(command, None)
        if cmd == None: raise CommandNotFound(f"'{command}'")
        return cmd

def __pop_arg(*args: str) -> tuple[str, tuple[str, ...]]:
    if len(args) < 1: raise NotEnaughArguments
    return args[0], args[1:]

def CMD_cd(shell: Shell, *args: str) -> None:
    try:
        path, args = __pop_arg(*args)
    except NotEnaughArguments:
        shell.system.print(f"cd: Path not specified!")
    else:
        shell.cwd = path

def CMD_pwd(shell: Shell, *args: str) -> None:
    shell.system.print(shell.cwd, raw=True)

def CMD_exit(shell: Shell, *args: str) -> None:
    shell.interactive = False
