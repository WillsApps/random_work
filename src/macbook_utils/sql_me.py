import logging
import os
import sys
from pathlib import Path
from subprocess import run
from sqlfluff import fix
import sqlparse
from sqlfluff.core import FluffConfig

from utils.log_utils import set_log_stout

log = logging.getLogger(__file__)
log.setLevel(logging.DEBUG)
set_log_stout(log)


def get_sql_paths_from_dir(path: Path) -> set[Path]:
    if not path.exists():
        return set()
    if path.is_file() and path.suffix == ".sql":
        return {path}

    if not path.is_dir():
        return set()

    paths = set()
    for child in path.iterdir():
        paths.update(get_sql_paths_from_dir(child))
    return paths


def add_if_sql_or_dir(root: Path, git_path: str) -> set[Path]:
    # log.debug(git_path)
    file_path = root / git_path.strip(" ")
    if not file_path.exists():
        return
    return get_sql_paths_from_dir(file_path)


def format_query(query: str, config: FluffConfig):
    query = query.strip()
    if not query:
        return ""
    log.debug(query)
    query = f"{query};"

    fluffed = fix(
        query,
        dialect="postgres",
        config=config,
        # rules=["jinja.padding", "capitalisation.keywords.capitalisation_policy.upper"]
    )
    return fluffed


def get_files_from_git():
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
        # log.debug(line)
        # log.debug(line.startswith("\t") or line.startswith("        "))
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
    return file_paths


def main():
    dialect = sys.argv[2]
    if len(sys.argv) == 3:
        file_paths = [Path(sys.argv[1])]
    else:
        file_paths = get_files_from_git()

    log.debug(file_paths)
    fluff_path = Path(__file__).parent.parent.parent / ".sqlfluff"
    config = FluffConfig.from_path(
        str(fluff_path), overrides={"dialect": dialect}
    )
    for file_path in sorted(file_paths):
        with open(file_path, "r") as f:
            raw = f.read()
        queries = raw.split(";")
        fluffed_queries = []
        for query in queries:
            fluffed_queries.append(format_query(query, config))
        with open(file_path, "w") as f:
            f.write(";\n".join(fluffed_queries))


if __name__ == "__main__":
    main()
