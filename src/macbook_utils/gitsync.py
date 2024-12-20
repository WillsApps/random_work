import os
from pathlib import Path
from sys import argv

from dotenv import load_dotenv
from github import Auth
from github import Github
from github.Branch import Branch
from github.Workflow import Workflow

env_file = Path(__file__).parent.parent.parent / ".env"
load_dotenv(env_file)


def dispatch(workflow: Workflow, branch: Branch, path: str, env: str):
    print(f"Dispatching {path=}, {env=}")
    workflow.create_dispatch(branch, {"stage": env, "path": path})


def main():
    branch_name = argv[1]

    auth = Auth.Token(os.environ["GITHUB_TOKEN"])
    g = Github(auth=auth)
    repo = g.get_repo("verana-health/vh-airflow")
    branch = repo.get_branch(branch_name)
    workflow = repo.get_workflow("sync_dags.yml")
    # dispatch(workflow, branch, "integrations/", "testing")
    # dispatch(workflow, branch, "", "develop")
    # dispatch(workflow, branch, "utils/", "testing")
    # dispatch(workflow, branch, "", "new_staging")
    # dispatch(workflow, branch, "integrations/")
    # time.sleep(5)
    # dispatch(workflow, branch, "operators/")
    # time.sleep(5)
    dispatch(workflow, branch, "entities/", "new_staging")
    dispatch(workflow, branch, "integrations/cdh/", "new_staging")


if __name__ == "__main__":
    main()
