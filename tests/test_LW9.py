import pytest
from src.LW9 import Stack

test_data_push = [
    ([10], 10, 1),
    ([10, 20], 20, 2),
    ([10, 20, 30], 30, 3),
]
test_data_is_empty = [
    ([], True),
    ([10], False),
    ([10, 20], False),
]
test_data_size = [
    ([], 0),
    ([10], 1),
    ([10, 20], 2),
    ([10, 20, 30], 3),
]


@pytest.mark.parametrize("values, expected_top, expected_size", test_data_push)
def test_push(values, expected_top, expected_size):
    stack = Stack()
    for value in values:
        stack.push(value)
    assert stack.is_empty() is False
    assert stack.peek() == expected_top
    assert stack.size() == expected_size


def test_pop_empty_stack():
    stack = Stack()
    result = stack.pop()
    assert result is None
    assert stack.is_empty() is True
    assert stack.size() == 0


def test_pop_last_element():
    stack = Stack()
    stack.push(10)
    result = stack.pop()
    assert result == 10
    assert stack.is_empty() is True
    assert stack.size() == 0


def test_pop_from_non_empty_stack():
    stack = Stack()
    stack.push(10)
    stack.push(20)
    result = stack.pop()
    assert result == 20
    assert stack.peek() == 10
    assert stack.size() == 1
    assert stack.is_empty() is False


def test_peek_empty_stack():
    stack = Stack()
    result = stack.peek()
    assert result is None
    assert stack.is_empty() is True


def test_peek_non_empty_stack():
    stack = Stack()
    stack.push(10)
    stack.push(20)
    result = stack.peek()
    assert result == 20
    assert stack.size() == 2


@pytest.mark.parametrize("values, expected", test_data_is_empty)
def test_is_empty(values, expected):
    stack = Stack()
    for value in values:
        stack.push(value)
    assert stack.is_empty() is expected


@pytest.mark.parametrize("values, expected_size", test_data_size)
def test_size(values, expected_size):
    stack = Stack()
    for value in values:
        stack.push(value)

    assert stack.size() == expected_size


def test_stack_lifo():
    stack = Stack()
    stack.push(10)
    stack.push(20)
    stack.push(30)
    assert stack.pop() == 30
    assert stack.pop() == 20
    assert stack.pop() == 10
    assert stack.pop() is None


def test_peek_does_not_remove_element():
    stack = Stack()
    stack.push(10)
    stack.push(20)
    assert stack.peek() == 20
    assert stack.peek() == 20
    assert stack.size() == 2
