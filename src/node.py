from __future__ import annotations
from enum import StrEnum, auto

class TYPE(StrEnum):
    FILE = auto()
    DIRECTORY = auto()

class Node:
    """
    Represent a file or directory.

    Fields:
        type: string value, 'file' or 'directory'
        name: file name with extension
        content: file content (empty string if directory)
        nodes: children list (empty list if file)
        parent: parent node object
        path: absolute path
    """

    def __init__(self, *, type: TYPE, name: str, content: bytes, parent: Node | None) -> None:

        self._type: TYPE = type
        self.name: str = name
        self.content: bytes = content
        self.nodes: list[Node] = list()
        self._parent = parent

    @property
    def parent(self) -> Node | None:
        return self._parent

    @parent.setter
    def parent(self, parent: Node | None) -> None:
        if self.parent is None:
            self._parent = parent
        else:
            msg = f'Parent of node {self} already exists\nand cannot be set to {parent}'
            raise Exception(msg)

    @property
    def path(self):
        return self._get_abs_path(self)

    @property
    def type(self) -> str:
        return str(self._type)

    def is_dir(self) -> bool:
        return self._type == TYPE.DIRECTORY

    def is_file(self) -> bool:
        return self._type == TYPE.FILE

    @staticmethod
    def _get_abs_path(node: Node, path: str = '') -> str:
        """
        Returns absolute path without
        using os-dependent path abstraction.
        """

        if node.parent == None:
            return '/' if not path else path
        return __class__._get_abs_path(node.parent, f'/{node.name}{path}')

    def __repr__(self):
        return f"{self._type.capitalize()}: {self.name} ({self.path})"
