import logging
from subprocess import run

from utils.log_utils import set_log_stout

log = logging.getLogger(__file__)
log.setLevel(logging.INFO)
set_log_stout(log)


def add_if_py_or_dir(file_path: str):
    log.debug(file_path)
    if file_path.endswith(".py") or file_path.endswith("/"):
        return file_path.strip(" ")
    return ""


def main():
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
                file_paths.add(add_if_py_or_dir(line.split("->")[1]))
            elif "modified:" in line or "new file:" in line:
                file_paths.add(add_if_py_or_dir(line.split(":")[1]))
            elif "removed:" in line:
                continue  #  Don't do anything if the file doesn't exist
            elif "deleted:" in line:
                continue  #  Don't do anything if the file doesn't exist
            else:
                file_paths.add(add_if_py_or_dir(line))

    if "" in file_paths:
        file_paths.remove("")
    log.debug(file_paths)
    log.debug(f"Command: {' '.join(['black', *file_paths])}")
    black_output = (
        run(["black", *file_paths], capture_output=True)
        .stderr.decode()
        # .stdout.decode()
        .replace(
            "\n",
            "\n",
        )
        .replace("\t", "        ")
    )
    log.info(black_output)


if __name__ == "__main__":
    main()
