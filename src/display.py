"""
Run this as a script.

Read binary file and print
hexdump-like output.
"""

import sys

def main(file: str):

    try:
        with open(file, 'rb') as f:
            data = f.read()
    except FileNotFoundError:
        return print(f'No such file \'{file}\'')

    # In python 3.12: itertools.batched
    x = [data[i:i+8] for i in range(0, len(data), 8)]

    y = []
    for z in x:
        s = ''
        for o in z:
            if 32 <= o and o <= 126:
                s += chr(o) + " "
            else:
                s += '. '
        y.append(s)

    if len(x) % 2 != 0:
        x.append(b'')
        y.append('')

    fmt = lambda s: s.hex().ljust(16, ' ')

    for i in range(0, len(x), 2):
        print(fmt(x[i]), fmt(x[i+1]), y[i], y[i+1])

if __name__ == "__main__":
    file = sys.argv[1] if len(sys.argv) > 1 else 'D.bin'
    main(file)
