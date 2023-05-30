from command import Resolver, CommandNotFound

class Shell:

    resolver: Resolver = Resolver()

    def __init__(self, name: str) -> None:
        self.name = name

        self.interactive = False
        self.cwd = None
        self.prompt = str()
        self.system = None
        self.user = None

    def execute(self, command: str, *args) -> None:
        try:
            cmd = self.resolver.get(command)
        except CommandNotFound:
            self.system.print(f"[{self.name}] Command '{command}' not found!")
        else:
            cmd(self, *args)
        self.prompt = f"{self.user.name}@{self.system.name}> "

    def interact(self) -> None:
        self.interactive = True
        while self.interactive:
            self.execute(*input(self.prompt).split())
