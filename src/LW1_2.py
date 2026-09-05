def sum(x: list[int], N: int) -> int:
    s = 0  # 15
    for i in range(N):  # 16
        s += x[i]  # 17
    return s  # 18


def read_int(prompt: str) -> int:
    print(prompt)  # 26, 29
    x = int(input(prompt))  # 27, 30
    return x  # 28, 31


def function():
    N = 10  # 3
    a = [1, 3, -5, 0, 4, 6, -1, 9, 3, 2]  # 4
    m = a[0]  # 5
    for i in range(N):  # 6
        if m < a[i]:  # 7
            m = a[i]  # 8
    print(m)  # 13

    s = sum(a, N)  # 14
    print(s)  # 19

    z = s // m  # 20
    k = 0  # 21

    for i in range(N):  # 22
        if a[i] > z:  # 23
            k += a[i]  # 24
        else:
            k -= a[i]  # 25

    print(k)  # 25 (после завершения цикла)

    x = read_int("")  # 26
    y = read_int("")  # 29
    s = 0  # 32
    while x != 0 and y != 0:  # 33
        x -= 1  # 34
        y -= 1  # 35
        s += x + y  # 36
    print(s)  # 37


if __name__ == "__main__":  # 1
    function()  # 2
