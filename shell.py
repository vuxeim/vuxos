from command import Resolver, CommandNotFound

class Shell:

    resolver: Resolver = Resolver()

    def __init__(self, name: str) -> None:
        self.interactive = False
        self.name = name
        self.cwd = None
        self.system = None

    def execute(self, command: str, *args) -> None:
        try:
            cmd = self.resolver.get(command)
        except CommandNotFound:
            self.system.print(f"[{self.name}] Command '{command}' not found!")
        else:
            cmd(self, *args)

    def interact(self) -> None:
        self.interactive = True
        while self.interactive:
            self.execute(*input().split())
