import pytest
from src.LW5 import LTrim

test_data = [("H", "H", ""), ("Hello", "He", "llo"), ("H", "A", "H")]


@pytest.mark.parametrize("input,to_remove,expected", test_data)
def test_trim(input, to_remove, expected):
    assert LTrim.trim(input, to_remove) == expected


def test_trim_negative():
    with pytest.raises(ValueError):
        LTrim.trim("", "")
