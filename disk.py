from __future__ import annotations
from enum import StrEnum, auto
import json

class FIELDS(StrEnum):
    NAME = auto()
    TYPE = auto()
    CONTENT = auto()
    NODES = auto()

class TYPES(StrEnum):
    FILE = auto()
    DIRECTORY = auto()

class Node:
    """
    Represent file or directory.

    Fields:
        name: file name with extension
        type: enum value, FILE or DIRECTORY
        content: file content (empty string if directory)
        nodes: children list (empty list if file)
        parent: parent node object
    """

    name: str
    type: TYPES
    content: str
    nodes: list[Node]
    parent: Node | None

    def __init__(self, type: TYPES, name: str, content: str, parent: Node | None) -> None:
        self.type = type
        self.name = name
        self.content = content
        self.nodes = list()
        self.parent = parent

    def __repr__(self):
        return f"{self.type.capitalize()}: {self.name}"

class Disk:
    """ Represents a hard drive """

    STORAGE_TYPE: str = 'json'

    def __init__(self, *, name: str) -> None:
        self.name = name
        self.data: dict = self.read()

    def read(self) -> dict:
        """ Load data from disk file """
        st = __class__.STORAGE_TYPE
        extension = ('.'+st) if st != '' else ''
        filename = self.name+extension
        with open(filename, 'rb') as f:
            return json.load(f)

    def get_structure(self) -> Node:
        return self._get_node_object(self.data, None)

    def _get_node_object(self, data: dict, parent: Node | None) -> Node:
        """ Get tree structure of all files and directories """
        obj = Node(data[FIELDS.TYPE], data[FIELDS.NAME], data[FIELDS.CONTENT], parent)
        for node in data[FIELDS.NODES]:
            obj.nodes.append(self._get_node_object(node, obj))
        return obj
