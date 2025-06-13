import sys
from pathlib import Path


def main():
    print(sys.argv[0])
    current = Path.cwd()
    _from = sys.argv[1]
    _to = sys.argv[2]

    if _from.startswith("/"):
        _from = Path(_from)
    else:
        _from = current / _from

    if _to.startswith("/"):
        _to = Path(_to)
    else:
        _to = current / _to

    for file in _from.iterdir():
        file.replace(_to / file.name)


if __name__ == "__main__":
    main()
