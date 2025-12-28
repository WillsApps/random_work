import pytest

from bg3_linux_mod_manager.mod_manager import (
    build_mod_nodes,
    get_mods_list,
    replace_mods_list,
)
from tests.bg3_mod_manager.samples import (
    GUSTAV_X_MOD,
    MOD_LIST,
    MOD_NODE_5E_SPELLS,
    MOD_NODE_MOD_CONFIGURATION,
    PARSED_XML_ONE_MOD_EMPTY_MOD_ORDER,
    PARSED_XML_ONE_MOD_NO_MOD_ORDER,
    PARSED_XML_TWO_MODS_EMPTY_MOD_ORDER,
    PARSED_XML_TWO_MODS_NO_MOD_ORDER,
    XML_WITH_EMPTY_MOD_ORDER,
    XML_WITH_NO_MOD_ORDER,
)


@pytest.mark.parametrize(
    "test_name, example, number_mods",
    [
        (
            "ONE_MOD_NO_MOD_ORDER",
            PARSED_XML_ONE_MOD_NO_MOD_ORDER,
            1,
        ),
        ("TWO_MODS_NO_MOD_ORDER", PARSED_XML_TWO_MODS_NO_MOD_ORDER, 2),
        ("TWO_MODS_EMPTY_MOD_ORDER", PARSED_XML_TWO_MODS_EMPTY_MOD_ORDER, 2),
        ("ONE_MOD_EMPTY_MOD_ORDER", PARSED_XML_ONE_MOD_EMPTY_MOD_ORDER, 1),
    ],
)
def test_get_mods_list_one_mod(test_name, example, number_mods):
    expected = []
    for _ in range(number_mods):
        expected.append(GUSTAV_X_MOD)

    actual = get_mods_list(example)
    assert actual == expected


def test_build_mod_nodes_5e_spells():
    example = {
        "mods": [
            {
                "modName": "5eSpells",
                "UUID": "fb5f528d-4d48-4bf2-a668-2274d3cfba96",
                "folderName": "5eSpells",
                "version": "1",
                "MD5": "",
            }
        ]
    }
    expected = [MOD_NODE_5E_SPELLS]
    actual = build_mod_nodes(example)
    assert actual == expected


def test_build_mod_nodes_mod_configuration():
    example = {
        "Mods": [
            {
                "Author": "Volitio",
                "Name": "Mod Configuration Menu",
                "Folder": "BG3MCM",
                "Version": "40391659157979136",
                "Description": "Provides an in-game UI that enables players to intuitively manage mod settings and hotkeys.",
                "UUID": "755a8a72-407f-4f0d-9a33-274ac0f0b53d",
                "Created": "2025-05-17T02:17:59.9329551-03:00",
                "Dependencies": [],
                "Group": "ff29b3aa-4c88-431f-9a7a-bf637012e964",
            }
        ],
        "MD5": "405322d230c88a287892f76f0dfb9a4a",
    }
    expected = [MOD_NODE_MOD_CONFIGURATION]
    actual = build_mod_nodes(example)
    assert actual == expected


@pytest.mark.parametrize(
    "test_name, example, expected",
    [
        (
            "ONE_MOD_NO_MOD_ORDER",
            PARSED_XML_ONE_MOD_NO_MOD_ORDER,
            XML_WITH_NO_MOD_ORDER,
        ),
        (
            "TWO_MODS_NO_MOD_ORDER",
            PARSED_XML_TWO_MODS_NO_MOD_ORDER,
            XML_WITH_NO_MOD_ORDER,
        ),
        (
            "TWO_MODS_EMPTY_MOD_ORDER",
            PARSED_XML_TWO_MODS_EMPTY_MOD_ORDER,
            XML_WITH_EMPTY_MOD_ORDER,
        ),
        (
            "ONE_MOD_EMPTY_MOD_ORDER",
            PARSED_XML_ONE_MOD_EMPTY_MOD_ORDER,
            XML_WITH_EMPTY_MOD_ORDER,
        ),
    ],
)
def test_replace_mods_list(test_name, example, expected):
    actual = replace_mods_list(example, MOD_LIST)
    assert actual == expected
