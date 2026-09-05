def sqr(x: int) -> int:
    q = x * x  # 8
    return q  # 9


def function():
    N = 10  # 2
    a = [5, 2, 7, -9, 4, 8, -1, 0, 3, 6]  # 3
    s = 0  # 4
    for i in range(N):  # 5
        if a[i] > 0:  # 6.0
            s += sqr(a[i])  # 6.1
    print(f"Сумма квадратов равна: {s}")  # 7


if __name__ == "__main__":  # 0
    function()  # 1
