# vuxos
It is like a GUN/Linux emulator in Python. Useless but fun project.
### Features
- it runs fine most of the times
- entering commands like in bash and seeing the result is possible
- plugin system - you can create your own command
- display content of disk file
### How to run
0. Be in `src/` directory
1. Convert JSON file to binary
`python -m pack D.json D.bin`
2. Run `main.py`
```shell
python main.py
```
### Add your own command
1. Create `.py` file in `commands/` directory
2. Define class whose name starts with `CMD_`
3. Define `__init__` method that accepts shell object and arbitrary amount of str objects
```python
def __init__(self, shell: Shell, *args: str)
```
4. Command runs by invoking the `__init__` method, so put business logic in there
5. Access to other parts of the system is possible through `shell.system` variable
### Display binary file
This emulator uses a binary file to store blob of data that represents a hard drive. Use `display.py` script to print content of such file and please your eyes with beaufily hexdump-ish formatted wall of characters.
```shell
python -m display
# or explicitly:
python -m display custom_name.bin
```
### Y?
I do not know. This _emulator_ is essentially an advanced file reader and interpreter that has no sophisticated purpose. (Writing feature is planned for future, so it will promote to a file editor.)