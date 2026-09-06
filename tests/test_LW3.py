import pytest
from src.LW3 import RleCodec

test_data_encoding = [
    ("AABBBC", "A2B3C"),
    ("AAA", "A3"),
    ("ц", "ц"),
    ("ABC", "ABC"),
    ("A", "A"),
]
test_data_decoding = [
    ("A2B3C", "AABBBC"),
    ("A3", "AAA"),
    ("ц", "ц"),
    ("ABC", "ABC"),
    ("A10", "AAAAAAAAAA"),
]
test_data_decoding_failures = [
    "1",
    "",
    "П0",
    "B-1",
    "A1",
    "A0",
]
test_data_is_valid = [
    "A",
    "ABC",
    "A2B3C",
    "ф",
    "A3",
    "A10",
]
test_data_is_valid_failures = [
    "1",
    "",
    "П0",
    "B-1",
    "A1",
    "A0",
]


@pytest.mark.parametrize("input, expected", test_data_encoding)
def test_encoding(input, expected):

    actual_result = RleCodec.encode(input)

    assert actual_result == expected


def test_encoding_none():
    with pytest.raises(TypeError):
        RleCodec.encode(None)


def test_encoding_empty():
    with pytest.raises(ValueError):
        RleCodec.encode("")


@pytest.mark.parametrize("input, expected", test_data_decoding)
def test_decoding(input, expected):
    actual_result = RleCodec.decode(input)

    assert actual_result == expected


def test_decoding_none():
    with pytest.raises(TypeError):
        RleCodec.decode(None)


@pytest.mark.parametrize("input", test_data_decoding_failures)
def test_decoding_negative(input):
    with pytest.raises(ValueError):
        RleCodec.decode(input)


@pytest.mark.parametrize("input", test_data_is_valid)
def test_is_valid(input):
    actual_result = RleCodec.is_valid(input)
    assert True == actual_result


@pytest.mark.parametrize("input", test_data_is_valid_failures)
def test_is_valid_negative(input):
    actual_result = RleCodec.is_valid(input)
    assert False == actual_result
