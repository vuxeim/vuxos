from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from shell import Shell
    from filesystem import Filesystem

from user import User

class System:

    def __init__(self, *, name: str, fs: Filesystem):
        self.name = name
        self.filesystem = fs
        self.user: User

    def login(self, *, user: User, shell: Shell):
        self.user = user
        user.shell = shell

        shell.user = user
        shell.cwd = f"/home/{user.name}"
        shell.system = self

        self.print(f"User {user.name} has logged in!")
        shell.update_prompt()

    def print(self, text: str, *, raw: bool = False) -> None:
        if raw: return print(text)
        print(f"{self.user.shell.name}: {text}")
