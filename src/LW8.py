class Сonvertation:
    def __init__(self):
        pass

    @staticmethod
    def convert_to_bin(input: str) -> str:
        if not isinstance(input, str):
            raise TypeError("На вход должна подаваться строка.")

        if len(input) == 0:
            raise ValueError("Строка не должна быть пустой.")

        n = int(input)

        if n < 0:
            raise ValueError("Число не должно быть отрицательным.")

        if n == 0:
            return "0"

        string = ""

        while n > 0:
            string += str(n % 2)
            n //= 2

        return string[::-1]
