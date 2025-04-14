from collections import OrderedDict

from poe_scripts.embrace_maddress import (
    get_duration_mod,
    get_key_at_index,
    get_mods_from_index,
)


def test_get_duration_mod():
    assert get_duration_mod([100.0]) == 0.5
    assert get_duration_mod([50.0]) == 0.6666666666666666


def test_get_mods_from_index():
    faster_mods = OrderedDict()
    faster_mods[50.0] = 2
    faster_mods[15.0] = 3
    assert get_mods_from_index(faster_mods, 0) == OrderedDict()
    assert get_mods_from_index(faster_mods, 1) == OrderedDict([(50.0, 2)])
    assert get_mods_from_index(faster_mods, 2) == OrderedDict(
        [
            (50.0, 2),
            (15.0, 3),
        ]
    )


def test_get_key_at_index():
    faster_mods = OrderedDict()
    faster_mods[50.0] = 2
    faster_mods[15.0] = 3
    assert get_key_at_index(faster_mods, 0) == 50.0
    assert get_key_at_index(faster_mods, 1) == 15.0
