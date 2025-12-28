import os
from dataclasses import dataclass
from datetime import datetime, timedelta

import requests
from beartype.typing import Optional
from dataclasses_json import DataClassJsonMixin

from general_utils.consts import load_env

load_env()


@dataclass
class AccessToken(DataClassJsonMixin):
    access_token: str
    token_type: str
    expires_in: int
    expires_at: Optional[datetime] = None

    def __post_init__(self):
        if self.expires_at is None:
            self.expires_at = datetime.now() + timedelta(seconds=self.expires_in - 10)


def get_access_token() -> AccessToken:
    client_id = os.getenv("SPOTIFY_CLIENT_ID")
    client_secret = os.getenv("SPOTIFY_CLIENT_SECRET")
    response = requests.post(
        "https://accounts.spotify.com/api/token",
        headers={
            "Content-Type": "application/x-www-form-urlencoded",
        },
        data={
            "grant_type": "client_credentials",
            "client_id": client_id,
            "client_secret": client_secret,
        },
    )
    response.raise_for_status()
    access_token = AccessToken.from_dict(response.json())
    return access_token


def get_active_song():
    pass
