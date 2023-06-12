from __future__ import annotations

class CommandNotFound(Exception): ...
class NoRemainingArguments(Exception): ...

class Resolver:

    _C: dict[str, type] = {'': type}

    def __init__(self) -> None:

        self._C |= {n.removeprefix('CMD_'): c for n, c in __import__('commands').commands}

    def get(self, command: str) -> type:
        """
        Returns function corresponding
        to specified name.
        Raises CommandNotFound.
        """
        cmd = self._C.get(command, None)
        if cmd == None:
            raise CommandNotFound(command.join("''"))
        return cmd

def _pop_arg(*args: str) -> tuple[str, tuple[str, ...]]:
    """ Pop next argument from args list """
    if len(args) < 1:
        raise NoRemainingArguments
    return args[0], args[1:]

def _arg(*args: str) -> bool:
    """ Whether there are arguments left in list """
    if len(args) > 0:
        return True
    return False
