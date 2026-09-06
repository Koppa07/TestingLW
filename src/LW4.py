class PointAreaChecker:
    def __init__(self, R):
        if R <= 0:
            raise ValueError("Радиус должен быть больше 0")

        self.R = R

    def test_point(self, x, y) -> int:
        distance_squared = x**2 + y**2
        inside_circle = distance_squared <= self.R**2

        if not inside_circle:
            return 3
        if (x > 0 and y >= x) or (x < 0 and y <= x):
            return 1

        return 2
