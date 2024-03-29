"""
Exposes command classes from 'commands' directory.
Hacky af but works.
"""


import importlib, os

from command import command, Command


commands: list[tuple[str, type[Command]]] = list()
for f in os.listdir(os.path.dirname(__file__)):
    if f != '__init__.py' and f.endswith('.py'):
        name = f.removesuffix('.py')
        m = importlib.import_module('.'+name, package='commands')
        commands.append((name, command(getattr(m, 'CMD_'+name))))
        del m, name
    del f
del importlib, os, command
