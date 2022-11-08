import os.path

import dotenv

REPO_DIR = os.path.join(
    os.path.dirname(__file__),
    "..",
    "..",
)
SRC_DIR = os.path.join(
    REPO_DIR,
    "src",
)

dotenv.load_dotenv(os.path.join(REPO_DIR, ".env"))
