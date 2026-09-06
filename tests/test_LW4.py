import pytest
from src.LW4 import PointAreaChecker

test_data_R_negative = [0, -0.001]
test_data = [
    (10, 3, 5, 1),
    (10, 5, 2, 2),
    (10, 15, 5, 3),
    (10, 10, 0, 2),
    (10, 9.999, 0, 2),
    (10, 10.001, 0, 3),
    (10, 5, 5, 1),
    (0.001, 0.0005, 0.0005, 1),
]


@pytest.mark.parametrize("R,x,y,expected", test_data)
def test_point_checker(R, x, y, expected):
    checker = PointAreaChecker(R)

    assert checker.test_point(x, y) == expected


@pytest.mark.parametrize("R", test_data_R_negative)
def test_R_negative(R):
    with pytest.raises(ValueError):
        PointAreaChecker(R)
