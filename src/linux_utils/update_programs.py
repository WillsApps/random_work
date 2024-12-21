import os
from dataclasses import dataclass
from pathlib import Path

import requests
from github import Github

from src.linux_utils import logger


@dataclass
class RepoToUpdate:
    owner: str
    name: str
    file_location: Path = None

    def __str__(self):
        return f"{self.owner}/{self.name}"


downloads = Path.home() / "Downloads"

repos = [
    RepoToUpdate("lutris", "lutris"),
]

github = Github()
for repo_to_update in repos:
    repo = github.get_repo(str(repo_to_update))
    latest = repo.get_latest_release()
    debs = []
    for asset in latest.assets:
        if asset.name.endswith(".deb"):
            debs.append(asset)
    if len(debs) == 1:
        deb = debs[0]
        download_location = downloads / deb.name
        repo_to_update.file_location = download_location
        if download_location.exists():
            continue
        content = requests.get(deb.browser_download_url).content
        with open(downloads / deb.name, "wb") as f:
            f.write(content)
    else:
        deb_names = [deb.name for deb in debs]
        raise Exception(
            f"Too many debs to download. {repo_to_update=}, {deb_names=}"
        )

for repo_to_update in repos:
    command = f"sudo dpkg -i {repo_to_update.file_location}"
    logger.info(f"Running command: {command}")
    os.system(command)
    print(command)
