import logging
import os
from pathlib import Path
from subprocess import run

import sqlparse

from utils.log_utils import set_log_stout

log = logging.getLogger(__file__)
log.setLevel(logging.DEBUG)
set_log_stout(log)


def get_sql_paths_from_dir(path: Path) -> set[Path]:
    if not path.exists():
        return {}
    if path.is_file() and path.suffix == ".sql":
        return {path}

    if not path.is_dir():
        return {}

    paths = {}
    for child in path.iterdir():
        paths.update(get_sql_paths_from_dir(child))
    return paths


def add_if_sql_or_dir(root: Path, git_path: str) -> set[Path]:
    log.debug(git_path)
    file_path = root / git_path.strip(" ")
    if not file_path.exists():
        return
    return get_sql_paths_from_dir(file_path)


def main():
    root = Path(os.getcwd())
    git_status_output = (
        run(["git", "status"], capture_output=True)
        .stdout.decode()
        .replace(
            "\n",
            "\n",
        )
        .replace("\t", "        ")
    )

    file_paths = set()
    for line in git_status_output.split("\n"):
        log.debug(line)
        log.debug(line.startswith("\t") or line.startswith("        "))
        if line.startswith("        "):
            if "renamed:" in line:
                file_paths.update(add_if_sql_or_dir(root, line.split("->")[1]))
            elif "modified:" in line or "new file:" in line:
                file_paths.update(add_if_sql_or_dir(root, line.split(":")[1]))
            elif "removed:" in line:
                continue  # Don't do anything if the file doesn't exist
            elif "deleted:" in line:
                continue  # Don't do anything if the file doesn't exist
            else:
                file_paths.update(add_if_sql_or_dir(root, line))

    log.debug(file_paths)
    for file_path in sorted(file_paths):
        with open(file_path, "r") as f:
            raw = f.read()
        config = ""
        if "{{ config" in raw:
            split = raw.split("}}")
            config = f"{split[0]}}}}}"
            raw = "}}".join(split[1:])
        formatted = sqlparse.format(
            raw,
            reindent=True,
            keyword_case="upper",
            identifier_case="lower",
            reindent_aligned=True,
            use_space_around_operators=True,
            indent_width=2,
            comma_firs=True,
        )
        with open(file_path, "w") as f:
            f.write(f"{config}\n{formatted}")


if __name__ == "__main__":
    main()
