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

    def login(self, *, user: User, shell: Shell):
        self.shell = shell
        shell.create_session(system=self)
        shell.attach_user(user=user)
        shell.update_prompt()
        self.print(f"User {user.name} has logged in!")

    def print(self, text: str, *, prefix: bool = False) -> None:
        if not prefix:
            return print(text)
        print(f"{self.shell.name}: {text}")

    def dp(self, *text: str, **kwargs) -> None:
        """ Debug print """
        red = '\x1b[31m'
        reset = '\x1b[0m'
        msg = "### DEBUG PRINT:"
        kv = str(kwargs) if len(kwargs.keys()) > 0 else ""
        print(f"{red}{msg}{reset}")
        print(f"{red}{'_'*len(msg)}{reset}")
        print(*text, kv)
        print(f"{red}{'^'*len(msg)}{reset}")
