from disk import Disk
from filesystem import Filesystem
from system import System
from shell import Shell
from user import User

disk = Disk(name='D')
filesystem = Filesystem(disk=disk)
system = System(name='VuxOS', fs=filesystem)
shell = Shell(name='vxsh')
user = User(name='vuxeim')

system.login(user=user, shell=shell)
shell.interact()
