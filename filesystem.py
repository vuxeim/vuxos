class Filesystem:

    def __init__(self):
        ...

    def listdir(self, path: str) -> list[str]:
        return _random_files()

def _random_files():
    import string, random
    rnd_letter = lambda: random.choice(string.ascii_letters)
    rnd_rng = lambda i, x: range(random.randint(i, x))
    rnd_name = lambda: ''.join([rnd_letter() for _ in rnd_rng(5, 10)])
    return [rnd_name() for _ in rnd_rng(5, 10)]