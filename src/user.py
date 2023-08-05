from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from shell import Shell


class NoSessionError(Exception): ...


class User:
    """
    Represents user interacting
    with system through shell.
    """

    def __init__(self, *, name: str) -> None:
        self.name = name
        self.shell: Shell
        self.session: bool = False

    def attach_session(self, *, shell: Shell) -> None:
        """
        Makes user able to interact
        with operating system via shell
        """
        self.session = True
        self.shell = shell

    def command(self, command: str, *args) -> None:
        """ Issue a command as user """
        if self.session == False:
            raise NoSessionError(self.name)
        self.shell.execute(command, *args)
