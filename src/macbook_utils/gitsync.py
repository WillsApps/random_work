import os
from sys import argv

from github import Github

from github import Auth

from dotenv import load_dotenv
from pathlib import Path

env_file = Path(__file__).parent.parent.parent / ".env"
load_dotenv(env_file)


def main():
    branch_name = argv[1]

    auth = Auth.Token(os.environ["GITHUB_TOKEN"])
    g = Github(auth=auth)
    repo = g.get_repo("verana-health/vh-airflow")
    branch = repo.get_branch(branch_name)
    workflow = repo.get_workflow("sync_dags.yml")
    workflow.create_dispatch(
        branch, {"stage": "testing", "path": "integrations/"}
    )


if __name__ == "__main__":
    main()
