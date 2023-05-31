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

    name: str
    type: TYPES
    content: str
    nodes: list[Node]

    def __init__(self, type: TYPES, name: str, content: str) -> None:
        self.type = type
        self.name = name
        self.content = content
        self.nodes = list()

class Disk:

    def __init__(self, *, name: str) -> None:
        self.name = name
        self.data: dict = self.read()

    def read(self) -> dict:
        type = 'json'
        with open(self.name+f"{'.'+type if type else ''}", 'rb') as f:
            return json.load(f)

    def get_structure(self, data: dict | None = None) -> Node:
        if data == None: data = self.data
        n = Node(data[FIELDS.TYPE], data[FIELDS.NAME], data[FIELDS.CONTENT])
        for node in data[FIELDS.NODES]:
            n.nodes.append(self.get_structure(node))
        return n
