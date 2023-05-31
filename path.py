from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING: from filesystem import Node
from enum import StrEnum, auto

class PATHTYPE(StrEnum):
    ABSOLUTE = auto()
    RELATIVE = auto()

class Path:

    def __init__(self, *, path: str) -> None:
        self.path = path
        self.type = __class__._get_type(path)
        if path == '/':
            self.nodes = ['/']
        else:
            self.nodes = path.split('/')
        self.nodes[0] = '/' if self.nodes[0] == '' else self.nodes[0]

    @staticmethod
    def _get_type(path: str) -> PATHTYPE:
        if path.startswith('/'):
            return PATHTYPE.ABSOLUTE
        return PATHTYPE.RELATIVE

    def get_node(self, structure: Node, names: list[str] | None = None) -> Node:
        if names == None:
            names = self.nodes.copy()

        # Recursion -- base case
        if len(names) < 1:
            return structure

        name = names.pop(0)

        # The root '/' special case
        # No need to loop over children
        if name == '/':
            return self.get_node(structure, names)

        for n in structure.nodes:
            if n.name == name:
                return self.get_node(n, names)

        raise FileNotFoundError(self.path)
