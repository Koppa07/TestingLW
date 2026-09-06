import pytest
from src.LW8 import Сonvertation

test_data = [
    ("0", "0"),
    ("1", "1"),
    ("2", "10"),
    ("15", "1111"),
    ("16", "10000"),
]

test_data_invalid = ["", "abc", "-1"]


@pytest.mark.parametrize("input, expected", test_data)
def test_convert(input, expected):
    assert Сonvertation.convert_to_bin(input) == expected


def test_convert_none():
    with pytest.raises(TypeError):
        Сonvertation.convert_to_bin(None)


@pytest.mark.parametrize("input", test_data_invalid)
def test_convert_empty(input):
    with pytest.raises(ValueError):
        Сonvertation.convert_to_bin(input)
