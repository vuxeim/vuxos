from user import User


class System:

    def __init__(self, name: str):
        self.name = name
        self.cwd = None
        self.user = None


    def login(self, user: User):
        self.user = user
        self.cwd = f"/home/{user.name}"
        self.print(f"User {self.user.name} has logged in!")


    def print(self, text: str):
        print(text)

