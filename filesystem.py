from disk import Disk, Node
from path import Path

class Filesystem:

    def __init__(self, *, disk: Disk):
        self._structure: Node = disk.get_structure()

    def exists(self, path: Path) -> bool:
        try:
            _ = path.get_node(self._structure)
        except FileNotFoundError:
            return False
        else:
            return True

    def listdir(self, path: str) -> list[Node]:
        """
        Returns directory content.
        Raises FileNotFoundError.
        """
        p = Path(path=path)
        if self.exists(p):
            node = p.get_node(self._structure)
            return node.nodes
        raise FileNotFoundError(path)

def _random_files():
    """ Generate mock file names """
    import string, random
    rnd_letter = lambda: random.choice(string.ascii_letters)
    rnd_rng = lambda i, x: range(random.randint(i, x))
    rnd_name = lambda: ''.join([rnd_letter() for _ in rnd_rng(5, 10)])
    return [rnd_name() for _ in rnd_rng(5, 10)]
