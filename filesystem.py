from __future__ import annotations
from disk import Disk, Node

class NodeNotFound(Exception): ...

class Filesystem:

    def __init__(self, *, disk: Disk):
        self._structure: Node = disk.get_structure()

    def exists(self, path: str) -> bool:
        try:
            self.get_node_at(path)
        except NodeNotFound:
            return False
        else:
            return True

    def _get_node(self, structure: Node, names: list[str]) -> Node:
        """ Returns node object of from corresponding path """

        # Recursion -- base case
        if len(names) < 1:
            return structure

        name = names.pop(0)

        # The root '/' special case
        # No need to loop over children
        if name == '/':
            return self._get_node(structure, names)

        for n in structure.nodes:
            if n.name == name:
                return self._get_node(n, names)

        raise NodeNotFound

    def get_node_at(self, path: str) -> Node:
        """ Uses recursive method _get_node() """
        if path == '/':
            nodes = ['/']
        else:
            nodes = path.split('/')
            if nodes[0] == '':
                nodes[0] = '/'
        return self._get_node(self._structure, nodes)

    def listdir(self, path: str) -> list[Node]:
        """
        Returns directory content.
        Raises FileNotFoundError.
        """
        if self.exists(path):
            node = self.get_node_at(path)
            return node.nodes
        raise FileNotFoundError("Dont catch, use exists() method")

