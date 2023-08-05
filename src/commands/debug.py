from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from shell import Shell

class CMD_debug:
    """ Toggle system verbosity mode """

    def __init__(self, shell: Shell, *args) -> None:
        sys = shell.system

        sys._verbose = not sys._verbose
        status = 'en' if sys._verbose else 'dis'
        sys.print(f'Verbose mode is {status.capitalize()}abled')
