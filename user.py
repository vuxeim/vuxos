from typing import TYPE_CHECKING
if TYPE_CHECKING: from shell import Shell

class User:
    """
    Represents user interacting
    with system through shell.
    """

    def __init__(self, *, name: str) -> None:
        self.name = name
        self.shell: Shell

    def command(self, command: str, *args) -> None:
        """ Issue a command as user """
        self.shell.execute(command, *args)
