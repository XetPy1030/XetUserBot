from datetime import timedelta
import re

def parse_timedelta(input_string):
    # Регулярное выражение для захвата чисел и единиц измерения времени
    pattern = r"(\d+)([hms])"
    matches = re.findall(pattern, input_string)

    # Словарь для преобразования единиц измерения в аргументы timedelta
    time_args = {"h": 0, "m": 0, "s": 0}

    for value, unit in matches:
        if unit in time_args:
            time_args[unit] += int(value)

    # Создаем timedelta на основе собранных данных
    return timedelta(hours=time_args["h"], minutes=time_args["m"], seconds=time_args["s"])


if __name__ == "__main__":
    # Пример использования
    td = parse_timedelta("1h 30m 45s")
    print(td)  # 1:30:45
