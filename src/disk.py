from __future__ import annotations
from io import BufferedReader

from node import Node, TYPE


class Disk:
    """ Represents a hard drive """

    TYPE_MAP: dict = {b'\x80': TYPE.DIRECTORY, b'\x00': TYPE.FILE}

    def __init__(self, *, name: str) -> None:
        self._name = name

    def get_structure(self) -> Node:
        """ Read and parse disk file """

        try:
            with open(self._name+'.bin', 'rb') as f:
                return self.parse(f)
        except FileNotFoundError as e:
            print('No disk file found')
            print('Create disk file with pack.py')
            exit(1)

    @staticmethod
    def parse(data: BufferedReader) -> Node:
        """ Convert binary blob of data to a tree of nodes """

        res = {}
        while data.peek():
            idd, parent_id, node = __class__._deserialize_next(data)
            res.update({idd: (parent_id, node)})

        dirs = {idd: node for idd, (_, node) in res.items() if node.is_dir()}

        root = None
        for _, (parent_id, node) in res.items():
            parent = dirs.get(parent_id, None)
            node.parent = parent
            if parent is not None:
                parent.nodes.append(node)
            else:
                root = node

        if root is None:
            raise Exception('Bad structure. Could not get the root.')

        return root

    @staticmethod
    def _deserialize_next(buff: BufferedReader) -> tuple[str, str, Node]:
        """ Convert binary blob of data to a node object """

        meta = buff.read(1)
        if meta not in (b'\x80', b'\x00'):
            raise Exception(f'Unknown node type {meta}')

        typee = __class__.TYPE_MAP[meta]

        idd = buff.read(16).hex()

        parent_id = buff.read(16).hex()

        name_len = int.from_bytes(buff.read(1))
        name = buff.read(name_len).decode()

        content = b''
        if meta == b'\x00':
            content_len = int.from_bytes(buff.read(4))
            content = buff.read(content_len)

        node = Node(type=typee, name=name, content=content, parent=None)
        return idd, parent_id, node
