import json
import os
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path

import requests
from beartype.typing import Optional
from dataclasses_json import DataClassJsonMixin, config
from github import Github
from marshmallow import fields

from general_utils.log_utils import logger


# https://discord.com/api/download/stable?platform=linux&format=deb
@dataclass
class RepoToUpdate(DataClassJsonMixin):
    owner: str
    name: str
    last_updated: Optional[datetime] = field(
        metadata=config(
            encoder=datetime.isoformat,
            decoder=datetime.fromisoformat,
            mm_field=fields.DateTime(format="iso"),
        ),
        default=None,
    )

    file_location: Path = None

    def __str__(self):
        return f"{self.owner}/{self.name}"


downloads = Path.home() / "Downloads"
config_path = Path.home() / ".config" / "update_programs" / "config.json"

if not config_path.exists():
    raise Exception(f"Config must exist: {config_path}")

repos = json.loads(config_path.read_text())

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
        raise Exception(f"Too many debs to download. {repo_to_update=}, {deb_names=}")

for repo_to_update in repos:
    command = f"sudo dpkg -i {repo_to_update.file_location}"
    logger.info(f"Running command: {command}")
    os.system(command)
    print(command)
