import logging
import math

# Настройка базового конфигуратора (аналог ILoggerFactory)
logging.basicConfig(
    level=logging.DEBUG, format="%(asctime)s [%(levelname)s] %(name)s: %(message)s"
)

# Логгеры с категориями для разделения потоков вывода
debug_logger = logging.getLogger("Debugger")  # Окно отладки (FN шаг)
trace_logger = logging.getLogger("TraceLogger")  # Окно трассировщика (LN шаг)


# Интегрируемая функция (пример: f(x) = ln(1/x))
def f(x: float) -> float:
    if x <= 0:
        raise ValueError(f"Точка x={x} выходит за область определения функции ln(1/x)")
    return math.log(1 + x) / x


def midpoint_rectangle_method(a: float, b: float, n: int) -> float:
    # Обобщенная формула прямоугольников (по средним точкам)
    h = (b - a) / n
    total_sum = 0.0

    for k in range(n):
        x_mid = a + (k + 0.5) * h

        assert a <= x_mid <= b, (
            f"Ошибка: Точка x_mid={x_mid} вышла за границы [{a}, {b}]"
        )

        total_sum += f(x_mid)

    return total_sum * h


def main():
    trace_logger.info("Начало работы программы численного интегрирования")

    # Пределы интегрирования и точность
    a = 0.1
    b = 1.0
    epsilon = 0.0001

    FN = 12  # Номер шага для вывода в отладчик
    LN = 19  # Номер шага для вывода в трассировщик

    n = 2  # Начальное количество разбиений
    iteration = 1  # Счётчик итераций
    delta_2n = float("inf")

    trace_logger.info("Параметры: a = %f, b = %f, eps = %f", a, b, epsilon)

    try:
        # Вычисление первичного приближения (In)
        I_n = midpoint_rectangle_method(a, b, n)

        # Вычисления продолжаются, пока погрешность Delta_2n > epsilon
        while delta_2n > epsilon:
            n_2n = 2 * n

            # Вычисление приближения с удвоенным числом шагов (I_2n)
            I_2n = midpoint_rectangle_method(a, b, n_2n)

            # Оценка погрешности по правилу Рунге для метода прямоугольников (Theta = 1/3)
            delta_2n = (1.0 / 3.0) * abs(I_2n - I_n)

            # Трассировка всех изменяющихся переменных на каждой итерации
            trace_logger.debug(
                "Итерация %d: n = %d, I_n = %.6f, I_2n = %.6f, Delta_2n = %.8f",
                iteration,
                n_2n,
                I_n,
                I_2n,
                delta_2n,
            )

            # Проверка шага FN (12) — вывод в отладчик
            if iteration == FN:
                debug_logger.info(
                    "[FN Step = %d] Значение интеграла I_2n = %.6f", FN, I_2n
                )

            # Проверка шага LN (19) — вывод в трассировщик
            if iteration == LN:
                trace_logger.info(
                    "[LN Step = %d] Значение интеграла I_2n = %.6f", LN, I_2n
                )

            # Подготовка к следующей итерации
            I_n = I_2n
            n = n_2n
            iteration += 1

        trace_logger.info(
            "Вычисления успешно завершены. Итоговое значение интеграла: %.6f, Погрешность: %.8f (за %d итераций)",
            I_2n,
            delta_2n,
            iteration - 1,
        )

    except AssertionError as e:
        trace_logger.error("Нарушено условие (Assert): %s", e)
    except Exception as e:
        trace_logger.critical(
            "Возникла критическая ошибка при вычислениях: %s", e, exc_info=True
        )


if __name__ == "__main__":
    main()
