class LTrim:
    def __init__(self):
        pass

    @staticmethod
    def trim(input: str, to_remove: str) -> str:
        n = len(input)  # 1
        if n == 0:  # 2
            raise ValueError("Строка не должна быть пустой")  # 3
        i = 0  # 4

        while i < len(input) and input[i] in to_remove:  # 5
            i += 1  # 6

        return input[i:]  # 7


s = "HeHello"
to_remove = "He"
trimmer = LTrim()
print(trimmer.trim(s, to_remove))
