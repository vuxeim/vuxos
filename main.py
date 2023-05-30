from user import User
from system import System
from shell import Shell

system = System('VuxOS')
shell = Shell('vush')
user = User('stas')

system.login(user=user, shell=shell)
shell.interact()
