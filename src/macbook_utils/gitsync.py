import os
import time
from sys import argv

from github import Github

from github import Auth

from dotenv import load_dotenv
from pathlib import Path

env_file = Path(__file__).parent.parent.parent / ".env"
load_dotenv(env_file)


def dispatch(workflow, branch, path):
    print(f"Dispatching {path=}")
    workflow.create_dispatch(
        branch, {"stage": "testing", "path": path}
    )


def main():
    branch_name = argv[1]

    auth = Auth.Token(os.environ["GITHUB_TOKEN"])
    g = Github(auth=auth)
    repo = g.get_repo("verana-health/vh-airflow")
    branch = repo.get_branch(branch_name)
    workflow = repo.get_workflow("sync_dags.yml")
    dispatch(workflow, branch, "integrations/")
    # dispatch(workflow, branch, "integrations/")
    # time.sleep(5)
    # dispatch(workflow, branch, "operators/")
    # time.sleep(5)
    # dispatch(workflow, branch, "entities/")


if __name__ == "__main__":
    main()
