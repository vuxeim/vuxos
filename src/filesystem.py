from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from disk import Disk, Node
    from path import Path


class _NodeNotFound(Exception): ...


class Filesystem:

    def __init__(self, *, disk: Disk):
        self._structure: Node = disk.get_structure()

    def exists(self, path: Path) -> bool:
        """ Straightforward. """
        try:
            self.get_node_at(path)
        except _NodeNotFound:
            return False
        else:
            return True

    def _get_node(self, structure: Node, names: list[str]) -> Node:
        """
        Recursive.
        Returns node object at corresponding path.
        """

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

        raise _NodeNotFound

    def get_node_at(self, path: Path) -> Node:
        """
        Uses recursive method _get_node()
        to return node at specified path.
        """
        nodes = path.nodify()
        return self._get_node(self._structure, nodes)

    def listdir(self, path: Path) -> list[Node]:
        """
        Returns directory content.
        Raises FileNotFoundError.
        """
        if self.exists(path):
            node = self.get_node_at(path)
            return node.nodes
        raise Exception("Dont catch, use exists() method")
