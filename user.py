from typing import TYPE_CHECKING
if TYPE_CHECKING: from shell import Shell

class User:

    def __init__(self, name: str) -> None:
        self.name = name
        self.shell: Shell

    def command(self, command: str, *args) -> None:
        self.shell.execute(command, *args)
