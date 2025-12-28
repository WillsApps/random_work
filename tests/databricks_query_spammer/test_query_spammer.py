from datetime import datetime, timedelta
from unittest.mock import MagicMock, patch

import pytest

from databricks_query_spammer.query_spammer import (
    get_expected_end_time,
    pretty_timedelta,
)


@patch("databricks_query_spammer.query_spammer.datetime")
def test_get_expected_end_time(mock_datetime: MagicMock):
    mock_datetime.now.return_value = datetime.fromisoformat("2025-05-12T00:06:00.000000")
    start_time = datetime.fromisoformat("2025-05-12T00:00:00.000000")
    actual_time_left, actual_end_time = get_expected_end_time(start_time, 1, 10)
    expected_time_left = timedelta(minutes=54)
    expected_end_time = datetime.fromisoformat("2025-05-12T01:00:00.000000")
    assert actual_time_left == expected_time_left
    assert actual_end_time == expected_end_time


@patch("databricks_query_spammer.query_spammer.datetime")
def test_get_expected_end_time_0_index(mock_datetime: MagicMock):
    mock_datetime.now.return_value = datetime.fromisoformat("2025-05-12T00:06:00.000000")
    start_time = datetime.fromisoformat("2025-05-12T00:00:00.000000")
    actual_time_left, actual_end_time = get_expected_end_time(start_time, 0, 10)
    expected_time_left = timedelta(days=41, seconds=57600)
    expected_end_time = datetime.fromisoformat("2025-06-22T16:06:00.000000")
    assert actual_time_left == expected_time_left
    assert actual_end_time == expected_end_time


@pytest.mark.parametrize(
    "example,expected",
    [
        (
            timedelta(hours=2, minutes=3, seconds=5),
            "(hours=2, minutes=3, seconds=5)",
        ),
        (
            timedelta(hours=24, minutes=3, seconds=5),
            "(days=1, minutes=3, seconds=5)",
        ),
        (timedelta(seconds=5), "(seconds=5)"),
    ],
)
def test_pretty_timedelta(example: timedelta, expected: str):
    assert pretty_timedelta(example) == expected
