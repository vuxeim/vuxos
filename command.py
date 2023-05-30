from typing import Callable

class CommandNotFound(Exception): ...

class Resolver:

    _C: dict = dict()

    def __init__(self) -> None:
        items = lambda: globals().items()
        is_fun = lambda fun: type(fun) == type(is_fun)
        rep = lambda name: name.replace('CMD_', '', 1)
        is_cmd = lambda name: name.startswith('CMD_')

        self._C = {rep(n): f for n, f in items() if is_fun(f) and is_cmd(n)}

    def get(self, command: str) -> Callable:
        cmd = self._C.get(command, None)
        if cmd == None:
            raise CommandNotFound(f"'{command}'")
        return cmd

def __get_arg(amount: int, *args):
    return args[0:amount]

def CMD_cd(shell: 'Shell', *args) -> None:
    path, = __get_arg(1, *args)
    shell.cwd = path

def CMD_pwd(shell: 'Shell', *args) -> None:
    shell.system.print(shell.cwd)

def CMD_exit(shell: 'Shell', *args) -> None:
    shell.interactive = False
