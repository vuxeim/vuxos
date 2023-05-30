from filesystem import Filesystem
from system import System
from shell import Shell
from user import User

filesystem = Filesystem()
system = System(name='VuxOS', fs=filesystem)
shell = Shell(name='vxsh')
user = User(name='vuxeim')

system.login(user=user, shell=shell)
shell.interact()
