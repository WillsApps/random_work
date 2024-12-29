from abc import ABC, abstractmethod
from unittest.mock import MagicMock

from _pytest.monkeypatch import MonkeyPatch

from src.class_hierarchy import print_func
from src.class_hierarchy.print_func import print_all


class Base(ABC):
    @abstractmethod
    def print_me(self, index: int):
        raise NotImplementedError()


def test_print_all(monkeypatch: MonkeyPatch) -> None:
    mock_child_one = MagicMock()
    mock_child_one.print_me.return_value = True
    mock_child_one.__setattr__("print_me", mock_child_one.print_me)
    mock_child_two = MagicMock()
    mock_child_two.print_me.return_value = True
    mock_child_two.__setattr__("print_me", mock_child_two.print_me)
    mock_class_map = {
        "one": mock_child_one,
        "two": mock_child_two,
    }
    monkeypatch.setattr(print_func, "CLASS_MAP", mock_class_map)
    print_all(["one", "two", "two", "two", "one"], Base.print_me)
    assert mock_child_one.print_me.call_count == 2
    child_one_call_args = mock_child_one.print_me.call_args_list
    assert child_one_call_args[0].args == (0,)
    assert child_one_call_args[1].args == (4,)

    assert mock_child_two.print_me.call_count == 3
    child_two_call_args = mock_child_two.print_me.call_args_list
    assert child_two_call_args[0].args == (1,)
    assert child_two_call_args[1].args == (2,)
    assert child_two_call_args[2].args == (3,)
