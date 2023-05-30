from command import Resolver

class Shell:

    resolver: Resolver = Resolver()

    def __init__(self, name: str) -> None:
        self.name = name
        self.cwd = None
        self.system = None

    def execute(self, command: str, *args) -> None:
        cmd = self.resolver.get(command)
        cmd(self, *args)
