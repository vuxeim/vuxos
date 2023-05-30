from user import User
from system import System
from shell import Shell

system = System('VuxOS')
shell = Shell('vxsh')
user = User('vuxeim')

system.login(user=user, shell=shell)
shell.interact()
