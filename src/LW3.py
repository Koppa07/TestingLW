class RleCodec:
    @staticmethod
    def encode(input: str) -> str:
        if not isinstance(input, str):
            raise TypeError("Входное значение должно быть строкой.")

        if len(input) < 1:
            raise ValueError("Входная строка не должна быть пустой.")

        output = ""
        count = 1

        for i in range(1, len(input)):
            if input[i] == input[i - 1]:
                count += 1
            else:
                output += input[i - 1]

                if count > 1:
                    output += str(count)

                count = 1

        output += input[-1]

        if count > 1:
            output += str(count)

        return output

    @staticmethod
    def decode(input: str) -> str:
        if not isinstance(input, str):
            raise TypeError("Входное значение должно быть строкой.")

        if len(input) < 1:
            raise ValueError("Входная строка не должна быть пустой.")

        if not RleCodec.is_valid(input):
            raise ValueError("Некорректная RLE-строка.")

        result = ""
        i = 0

        while i < len(input):
            char = input[i]
            i += 1

            count = ""

            while i < len(input) and input[i].isdigit():
                count += input[i]
                i += 1

            if count == "":
                count = 1
            else:
                count = int(count)

            result += char * count

        return result

    @staticmethod
    def is_valid(s: str) -> bool:
        if not isinstance(s, str):
            return False

        if s == "":
            return False

        i = 0

        while i < len(s):
            # Первый символ группы должен быть буквой
            if not s[i].isalpha():
                return False

            i += 1

            # Собираем число после буквы, если оно есть
            number = ""

            while i < len(s) and s[i].isdigit():
                number += s[i]
                i += 1

            # Если число указано, оно должно быть >= 2
            if number != "" and int(number) < 2:
                return False

        return True
