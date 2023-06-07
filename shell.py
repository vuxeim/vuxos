from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from system import System
    from user import User
from command import Resolver, CommandNotFound

class Shell:

    # Resolver for built-in shell commands
    resolver: Resolver = Resolver()

    def __init__(self, *, name: str) -> None:
        self.name = name

        self.interactive = False
        self.cwd = str()
        self.prompt = str()
        self.system: System
        self.user: User

    def execute(self, command: str = '', *args) -> None:
        """
        Decide if command is a shell built-in command
        or a installed software.
        Then runs it.
        """
        try:
            cmd = self.resolver.get(command)
        except CommandNotFound:
            self.system.print(f"command not found: {command}")
        else:
            cmd(self, *args)
        finally:
            self.update_prompt()

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
        path = path_color+self.cwd
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
