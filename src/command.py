from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from shell import Shell


class CommandNotFound(Exception): ...
class NoRemainingArguments(Exception): ...


class Command:
    CMD: str
    DOC: str
    def __init__(self, shell: Shell, *args: str): ...


def command(cls: type) -> type:
    class _class(cls):
        CMD = cls.__name__.removeprefix('CMD_')
        DOC = cls.__doc__ or ''
        def __init__(self, shell: Shell, *args) -> None:
            shell.system.debug(self.CMD)
            super().__init__(shell, *args)
    return _class


class Resolver:

    _commands: dict[str, type[Command]]

    def __init__(self) -> None:
        from commands import commands

        # commands = __import__('commads').commands
        self._commands = {name.removeprefix('CMD_'): cmd for name, cmd in commands}

    def get(self, command: str) -> type[Command]:
        """
        Returns function corresponding
        to specified name.
        Raises CommandNotFound.
        """

        if command == '':
            return Command

        cmd = self._commands.get(command, None)
        if cmd == None:
            raise CommandNotFound(command.join("''"))
        return cmd

    def get_list(self) -> list[type[Command]]:
        return list(self._commands.values())

    def get_names_list(self) -> list[str]:
        return list(self._commands.keys())

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
