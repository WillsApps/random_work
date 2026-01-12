import os
from pathlib import Path
from sys import argv

from dotenv import load_dotenv
from github import Auth, Github, Repository
from github.Branch import Branch

env_file = Path(__file__).parent.parent.parent / ".env"
load_dotenv(env_file)


def sync_dags(repo: Repository, branch: Branch, path: str, env: str):
    print(f"Dispatching {path=} for {env=}")
    workflow = repo.get_workflow("sync_dags.yml")
    workflow.create_dispatch(branch, {"stage": env, "path": path})


def ga(repo: Repository, branch: Branch, branch_type: str):
    print(f"Dispatching {branch_type=}")
    workflow = repo.get_workflow("ga.yml")
    workflow.create_dispatch(branch, {"branch_type": branch_type})


def main():
    branch_name = argv[1]

    auth = Auth.Token(os.environ["GITHUB_TOKEN"])
    g = Github(auth=auth)
    repo = g.get_repo("verana-health/vh-airflow")
    # repo = g.get_repo("verana-health/test-from-will")
    branch = repo.get_branch(branch_name)
    # workflow = repo.get_workflow("ga.yml")
    # dispatch(workflow, branch, "", "testing")
    # ga(workflow, branch, "hotfix")
    sync_dags(repo, branch, "curation/", "testing")
    # dispatch(workflow, branch, "utils/", "testing")
    # dispatch(workflow, branch, "integrations/", "testing")
    # dispatch(workflow, branch, "", "sandbox")
    # dispatch(workflow, branch, "", "develop")


if __name__ == "__main__":
    main()
