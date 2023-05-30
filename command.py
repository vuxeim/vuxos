from os import OperatingSystem


resolver = {
    'cd': cd_cmd,
    'pwd': pwd_cmd,
}


def cd_cmd(os: OperatingSystem, path: str):
    os.cwd = path


def pwd_cmd(os: OperatingSystem):
    os.print(os.cwd)
