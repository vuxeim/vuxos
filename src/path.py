from __future__ import annotations


class Path:
    """
    Represents path
    # TODO: add support for `..`
    """

    def __init__(self, *, path: str, username: str, cwd: str) -> None:

        if not self.safe(path):
            return

        self.raw_path = path
        self._user = username
        self._cwd = cwd
        self.absolute = self._as_absolute()
        self.pretty = self._prettify()

    @staticmethod
    def safe(path: str) -> bool:
        if path == '':
            raise Exception("Empty string as path")
        return True

    def _prettify(self) -> str:
        """
        Replaces home dir with `~` symbol
        """
        pr = self.absolute
        home_dir = f'/home/{self._user}'
        if pr.startswith(home_dir):
            pr = f'~{pr.removeprefix(home_dir)}'
        return pr

    def _as_absolute(self) -> str:
        """
        Transforms relative path
        to absolute one.
        """

        absp = self.raw_path
        if len(absp) > 1 and absp.endswith('/'):
            absp = absp.removesuffix('/')

        if absp == '~':
            absp = f'/home/{self._user}'

        elif absp == '/':
            absp = '/'

        elif absp == '.':
            absp = self._cwd

        elif absp.startswith("~/"):
            absp = f'/home/{self._user}/{absp.removeprefix("~/")}'

        elif absp.startswith('./'):
            absp = f'{self._cwd}/{absp.removeprefix("./")}'

        elif absp.startswith('/'):
            absp = absp

        else:
            if self._cwd == '/':
                absp = f'/{absp}'
            else:
                absp = f'{self._cwd}/{absp}'

        return absp

    def nodify(self) -> list[str]:
        """
        Represents path as list of strings.
        Ex. /home/user/.config/example.conf =
        ['/', 'home', 'user', '.config', 'example.conf']
        """
        if self.absolute == '/':
            nodes = ['/']
        else:
            nodes = self.absolute.split('/')
            if nodes[0] == '':
                nodes[0] = '/'
        return nodes

    @classmethod
    def empty(cls) -> Path:
        """ Returns path object with mock data """
        return cls(path='/', username='user', cwd='')
