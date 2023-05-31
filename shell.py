from __future__ import annotations


from command import Resolver, CommandNotFound
from system import System
from user import User

class Shell:

    resolver: Resolver = Resolver()

    def __init__(self, *, name: str) -> None:
        self.name = name

        self.interactive = False
        self.cwd = str()
        self.prompt = str()
        self.system: System
        self.user: User

    def execute(self, command: str = '', *args) -> None:
        try:
            cmd = self.resolver.get(command)
        except CommandNotFound:
            self.system.print(f"Command '{command}' not found!")
        else:
            cmd(self, *args)
        finally:
            self.update_prompt()

    def update_prompt(self) -> None:
        self.prompt = f"{self.user.name}@{self.system.name} {self.cwd} > "

    def interact(self) -> None:
        self.interactive = True
        while self.interactive:
            try:
                inp = input(self.prompt)
            except EOFError:
                self.interactive = False
                print()
            else:
                self.execute(*inp.split())
