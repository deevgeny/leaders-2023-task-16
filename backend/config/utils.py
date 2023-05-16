import os


def get_secret(name: str, default: str | None = ...) -> str:
    path = os.path.join('/run/secrets/', name)
    if os.path.isfile(path):
        with open(path) as f:
            return f.read()
    return default
