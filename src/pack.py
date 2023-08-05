from __future__ import annotations
from typing import TYPE_CHECKING
from enum import StrEnum, auto
import io
import os
import sys
import json
import hashlib

if TYPE_CHECKING:
    from node import TYPE
from disk import Disk
from node import Node


class _FIELD(StrEnum):
    NAME = auto()
    TYPE = auto()
    CONTENT = auto()
    NODES = auto()
    PARENT = auto()


def serialize(node: Node) -> bytes:

    buff = io.BytesIO()
    md5 = lambda path: hashlib.md5(path.encode()).digest()

    meta = b'\x80' if node.is_dir() else b'\x00'
    buff.write(meta) # meta [1 byte]

    idd: bytes = md5(node.path)
    buff.write(idd) # id [16 bytes]

    parent_id: bytes = b'\x00'*16 if node.parent is None else md5(node.parent.path)
    buff.write(parent_id) # parent_id [16 bytes]

    name_digest = node.name.encode()
    name_len = len(name_digest).to_bytes(length=1)
    buff.write(name_len) # name_len [1 byte]
    buff.write(name_digest) # name_digest [bytes]

    if node.is_file():
        content_digest = node.content
        content_len = len(content_digest).to_bytes(length=4)
        buff.write(content_len) # content_len [4 bytes]
        buff.write(content_digest) # content_digest [bytes]

    return buff.getbuffer().tobytes()

def parse_json(data: dict, parent: Node | None = None) -> Node:
    """ Convert json dict to the tree of nodes """

    typee: TYPE = data[_FIELD.TYPE]
    name: str = data[_FIELD.NAME]
    content: bytes = data[_FIELD.CONTENT].encode()
    nodes: list[dict] = data[_FIELD.NODES]

    obj = Node(type=typee, name=name, content=content, parent=parent)

    for node in nodes:
        obj.nodes.append(parse_json(node, obj))

    return obj

def traverse(structure: Node):
    yield structure
    for node in structure.nodes:
        yield from traverse(node)


def main(source: str, to: str):

    try:
        with open(source, 'rb') as f:
            if source.endswith('.bin'):
                parsed = Disk.parse(f)
            elif source.endswith('.json'):
                parsed = parse_json(json.load(f))
            else:
                print(f'Unsupported input file {source!r}')
                return

        if to.endswith('.bin'):
            with open(to, 'wb') as f:
                for n in traverse(parsed):
                    f.write(serialize(n))
        else:
            print(f'Unsupported output file {to!r}')
            return

    except FileNotFoundError as e:
        print(f'No such file {e.filename!r}')
        return

    fmt = lambda s: s.rsplit('.')[1].upper().join('""')
    print(f'Converted from {fmt(source)} to {fmt(to)}')
    print(f'Saved as {to!r}')


if __name__ == '__main__':
    if len(sys.argv) == 3:
        source, to = sys.argv[1:]
    else:
        print(f'./{os.path.basename(__file__)} <source> <target>')
        print(f'For default setup use: ./pack.py D.json D.bin')
        exit(1)

    main(source=source, to=to)