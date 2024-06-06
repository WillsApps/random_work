import os
from sys import argv

from github import Github
from github.Branch import Branch
from github.Repository import Repository
from github.Workflow import Workflow
from github.Requester import Requester

from github import Auth

from dotenv import load_dotenv
from pathlib import Path
env_file = (Path(__file__).parent.parent.parent / ".env")
load_dotenv(env_file)

token = os.environ["GITHUB_TOKEN"]

branch_name = argv[1]

# using an access token
auth = Auth.Token(token)
g = Github(auth=auth)
repo = g.get_repo("verana-health/vh-airflow")
branch = repo.get_branch(branch_name)
workflow = repo.get_workflow("sync_dags.yml")
workflow.create_dispatch(branch, {
    "stage": "testing",
    "path": "integrations/"
})