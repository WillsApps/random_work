from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
from typing import Optional

from dataclasses_json import DataClassJsonMixin, config
from github import Github
from marshmallow import fields


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


downloads = Path.home() / "Downloads" / "zips"
config_path = Path.home() / ".config" / "update_programs" / "config.json"
# print(config_path.read_text())
# exit()
# if not config_path.exists():
#     raise Exception(f"Config must exist: {config_path}")
#
# repos = json.loads(config_path.read_text())

owner = "rustdesk"
repo_name = "rustdesk"
github = Github()
repo = github.get_repo(f"{owner}/{repo_name}")
b = repo.get_branches()
print(repo.branches_url)
for br in b:
    print(br.name)
url = repo.get_latest_release().zipball_url
print(url)
# request_for_file = requests.get(url, stream=True)
# z = zipfile.ZipFile(io.BytesIO(request_for_file.content))
# target = downloads / owner/ repo_name
# target.mkdir(parents=True, exist_ok=True)
# z.extractall(downloads / repo_name)
