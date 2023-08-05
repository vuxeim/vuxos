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
        self._verbose: bool = False

    def login(self, *, user: User, shell: Shell):
        """
        Sets up communication between user,
        shell and operating system.
        """
        self.shell = shell
        shell.create_session(system=self)
        shell.attach_user(user=user)
        shell.update_prompt()
        self.print(f"User {user.name} has logged in!")

    @staticmethod
    def print(text: str) -> None:
        """ Central print function """
        print(text)

    def debug(self, text: str) -> None:
        if self._verbose:
            self.print(text)

    @staticmethod
    def safe_decode(data: bytes) -> str:
        """ Convert bytes to printable string """
        # TODO: (yikes) do it better
        return ''.join([chr(byte) if (32 <= byte and byte <= 126) or byte == 10 else ' ' for byte in data])

    @staticmethod
    def devel_debug_print(*text: str, **kwargs) -> None:
        """ Development-time debug print """
        red = '\x1b[31m'
        reset = '\x1b[0m'
        msg = "### DEBUG PRINT:"
        kv = str(kwargs) if len(kwargs.keys()) > 0 else ""
        print(f"{red}{msg}{reset}")
        print(f"{red}{'_'*len(msg)}{reset}")
        print(*text, kv)
        print(f"{red}{'^'*len(msg)}{reset}")
