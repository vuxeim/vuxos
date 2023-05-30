class User:

    def __init__(self, name: str) -> None:
        self.name = name
        self.shell = None

    def command(self, command: str, *args) -> None:
        self.shell.execute(command, *args)
