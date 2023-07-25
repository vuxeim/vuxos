from __future__ import annotations
from enum import StrEnum, auto
import json

class _FIELD(StrEnum):
    NAME = auto()
    TYPE = auto()
    CONTENT = auto()
    NODES = auto()
    PARENT = auto()

class _TYPE(StrEnum):
    FILE = auto()
    DIRECTORY = auto()

class Node:
    """
    Represent a file or directory.

    Fields:
        _type: enum value, FILE or DIRECTORY
        name: file name with extension
        content: file content (empty string if directory)
        nodes: children list (empty list if file)
        parent: parent node object
        _path: absolute path
    """

    _type: _TYPE
    name: str
    content: str
    nodes: list[Node]
    parent: Node | None
    _path: str

    def __init__(self, *, type: _TYPE, name: str, content: str, parent: Node | None) -> None:
        self._type = type
        self.name = name
        self.content = content
        self.nodes = list()
        self.parent = parent
        self._path = self._get_abs_path(self)

    @property
    def type(self) -> str:
        return str(self._type)

    def is_dir(self) -> bool:
        return self._type == _TYPE.DIRECTORY

    def is_file(self) -> bool:
        return self._type == _TYPE.FILE

    def _get_abs_path(self, node: Node, path: str = '') -> str:
        """
        Returns absolute path without
        using os-dependent path abstraction.
        """
        if node.parent == None:
            return '/' if not path else path
        return self._get_abs_path(node.parent, f'/{node.name}{path}')

    def __repr__(self):
        return f"{self._type.capitalize()}: {self.name} ({self._path})"

class Disk:
    """ Represents a hard drive """

    STORAGE_TYPE: str = 'json'

    def __init__(self, *, name: str) -> None:
        self.name = name
        self.data: dict = self._read()

    def _read(self) -> dict:
        """ Load data from disk file """
        st = self.STORAGE_TYPE
        extension = ('.'+st) if st != '' else ''
        filename = self.name+extension
        with open(filename, 'rb') as f:
            return json.load(f)

    def get_structure(self) -> Node:
        """ Invokes recursive method to get a files structure """
        return self._get_node(data=self.data, parent=None)

    def _get_node(self, data: dict, parent: Node | None) -> Node:
        """ Get tree structure of all files and directories """
        _type = data[_FIELD.TYPE]
        _name = data[_FIELD.NAME]
        _content = data[_FIELD.CONTENT]
        _nodes = data[_FIELD.NODES]
        obj = Node(type=_type, name=_name, content=_content, parent=parent)
        for node in _nodes:
            obj.nodes.append(self._get_node(node, obj))
        return obj
