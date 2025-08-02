from unittest.mock import MagicMock

import pytest
from evdev import UInput


@pytest.fixture(scope="function")
def mock_virtual_device() -> UInput:
    return MagicMock(__class__=UInput)
