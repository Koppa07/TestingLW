import logging

logging.basicConfig(
    level=logging.DEBUG, format="%(asctime)s [%(levelname)s] %(name)s: %(message)s"
)

logger = logging.getLogger("SequenceSumLogger")

# Эмуляция 64-битного знаковое целого числа (INT64_MAX)
MAX_INT = 2**63 - 1


def calculate_factorial_sum(N: int) -> int:
    """
    Вычисляет сумму факториалов от n_0 до n_N с проверкой переполнения через assert.
    """
    logger.info("Начало вычисления суммы факториалов от 0 до %d", N)

    total_sum = 0
    current_factorial = 1  # n_0 = 1

    for i in range(N + 1):
        if i == 0:
            current_factorial = 1
            logger.debug("Шаг i = 0: n_0 = 1")
        else:
            # Проверка арифметического переполнения при умножении: n_i = n_{i-1} * i
            assert current_factorial <= MAX_INT // i, (
                f"Арифметическое переполнение при вычислении факториала на шаге i = {i}! "
                f"Значение {current_factorial} * {i} превышает MAX_INT ({MAX_INT})"
            )
            current_factorial = current_factorial * i
            logger.debug("Шаг i = %d: n_%d = %d", i, i, current_factorial)

        # Проверка арифметического переполнения при сложении суммы
        assert total_sum <= MAX_INT - current_factorial, (
            f"Арифметическое переполнение при сложении суммы на шаге i = {i}! "
            f"Сумма {total_sum} + {current_factorial} превышает MAX_INT ({MAX_INT})"
        )
        total_sum += current_factorial
        logger.trace if hasattr(logger, "trace") else logger.debug(
            "Текущая сумма элементов S_%d = %d", i, total_sum
        )

    logger.info("Вычисления успешно завершены. Итоговая сумма: %d", total_sum)
    return total_sum


def main():
    # Задаем N для проверки (например, N = 21 вызовет переполнение 64-битного типа)
    N = 21

    try:
        result = calculate_factorial_sum(N)
        print(f"Сумма факториалов от 0 до {N} равна: {result}")
    except AssertionError as error:
        logger.error("Ошибка переполнения (Assert): %s", error)
    except Exception as error:
        logger.critical("Непредвиденная ошибка: %s", error, exc_info=True)


if __name__ == "__main__":
    main()
