from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from system import System
    from user import User

from path import Path
from command import Resolver, CommandNotFound

class Shell:

    # Resolver for built-in shell commands
    resolver: Resolver = Resolver()

    def __init__(self, *, name: str) -> None:
        self.name = name
        self.interactive: bool = False
        self.prompt = str()
        self.system: System
        self.cwd: Path = Path.empty()
        self.user: User

    def execute(self, command: str = '', *args) -> None:
        """
        Decide if command is a shell
        built-in command or a installed
        software. Then runs it.
        """
        try:
            cmd = self.resolver.get(command)
        except CommandNotFound:
            self.system.print(f"command not found: {command}")
        else:
            cmd(self, *args)
        finally:
            self.update_prompt()

    def pathify(self, path: str) -> Path:
        """ Returns path object from string """
        name = self.user.name
        cwd = self.cwd.absolute
        return Path(path=path, username=name, cwd=cwd)

    def create_session(self, *, system: System) -> None:
        """
        Allows shell to interact with
        underlaying operating system.
        """
        self.system = system

    def attach_user(self, *, user: User) -> None:
        """
        Allows user to interact with
        operating system via shell
        """
        self.user = user
        self.user.attach_session(shell=self)
        self.cwd = self.pathify("~")

    def update_prompt(self) -> None:
        """ Straightforward """
        name_color = "\x1b[33m"
        at_color = "\x1b[31m"
        system_color = "\x1b[37m"
        path_color = "\x1b[35m"
        arrow_color = "\x1b[36m"
        reset = "\x1b[0m"
        username = name_color+self.user.name
        at = at_color+'@'
        machine = system_color+self.system.name
        path = path_color+self.cwd.pretty
        arrow = arrow_color+'>'+reset
        self.prompt = f"{username}{at}{machine} {path} {arrow} "

    def interact(self) -> None:
        """
        Makes shell session interactive.
        Enables ability to type in commands.
        """
        self.interactive = True
        while self.interactive:
            try:
                inp = input(self.prompt)
            except EOFError:
                self.interactive = False
            else:
                self.execute(*inp.split())
