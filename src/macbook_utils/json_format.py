import json
import sys


def main(path: str):
    with open(path, "r") as f:
        contents = json.loads(f.read())

    with open(path, "w") as f:
        f.write(json.dumps(contents, indent=2))


if __name__ == "__main__":
    main(sys.argv[1])
