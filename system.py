from user import User
from shell import Shell


class System:

    def __init__(self, name: str):
        self.name = name
        self.user = None


    def login(self, *, user: User, shell: Shell):
        self.user = user
        user.shell = shell

        shell.cwd = f"/home/{user.name}"
        shell.system = self

        self.print(f"User {user.name} has logged in!")


    def print(self, text: str):
        print(text)

