import json
from pathlib import Path

STEAM_ROOT = Path.home() / ".steam/steam"

BG3_STEAM_ID = 1086940

BG3_PATH = (
    STEAM_ROOT
    / f"steamapps/compatdata/{BG3_STEAM_ID}/pfx/drive_c/users/steamuser/AppData/Local/Larian Studios/Baldur's Gate 3"
)
PUBLIC_XML = BG3_PATH / "PlayerProfiles/Public/modsettings.lsx"
MODS_DIR = BG3_PATH / "Mods"

STEAM_XML = STEAM_ROOT / f"userdata/91173939/{BG3_STEAM_ID}/modsettings.lsx"
print(STEAM_XML)
TEMP_DIR = Path(__file__).parent / "temp"
MOD_DEPENDENCIES = json.loads(
    (Path(__file__).parent / "mod_dependencies.json").read_text()
)
