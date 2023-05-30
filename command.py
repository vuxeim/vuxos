from shell import Shell

class CMD:
    @staticmethod
    def get_arg(amount: int, *args):
        return args[0:amount]


class Cd_CMD(CMD):

    @staticmethod
    def __init__(shell, *args):
        path, = CMD.get_arg(1, *args)
        shell.cwd = path


class Pwd_CMD(CMD):

    @staticmethod
    def __init__(shell, *args):
        shell.system.print(shell.cwd)

resolver = {
    'cd': Cd_CMD,
    'pwd': Pwd_CMD,
}
