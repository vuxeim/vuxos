from user import User
from system import System
from shell import Shell


system = System('VuxOS')
shell = Shell('vush')
user = User('stas')

system.login(user=user, shell=shell)
user.command('cd', '/root')
user.command('pwd')
user.command('cd', '~')
user.command('pwd')
shell.interact()
