from command import resolver


class User:

    def __init__(self, name: str):
        self.name = name
        self.shell = None


    def command(self, command: str, *args):
        cmd = resolver.get(command)
        cmd(self.shell, *args)
