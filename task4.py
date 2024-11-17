# Задача 4. Опции и флаги
# Напишите скрипт, который принимает два аргумента командной строки: число и
# строку. Добавьте следующие опции:
# ● --verbose, если этот флаг установлен, скрипт должен выводить
# дополнительную информацию о процессе.
# ● --repeat, если этот параметр установлен, он должен указывать,
# сколько раз повторить строку в выводе.
# Подсказка № 1
# Используйте import argparse, чтобы работать с аргументами командной строки.
# Подсказка № 2
# Используйте argparse.ArgumentParser для создания объекта парсера, который
# будет обрабатывать входные параметры.
# Подсказка № 3
# Примените метод add_argument для добавления обязательных аргументов number и
# text. Укажите типы данных и описания.
# Подсказка № 4
# Добавьте опцию --verbose с action='store_true' для флага, который активирует
# дополнительный вывод, и --repeat для указания количества повторений строки.

import argparse

parser = argparse.ArgumentParser(description="Скрипт для обработки параметров командной строки")

parser.add_argument("count", type=int, help="Число для обработки")
parser.add_argument("str_to_out", type=str, help="Строка для вывода")

parser.add_argument("--verbose", action="store_true", help="Дополнительная информация о процессе")
parser.add_argument("--repeat", type=int, default=1, help="Количество повторений при выводе строки")

args = parser.parse_args()

if args.verbose:
    print(f"Полученное число: {args.count}")
    print(f"Полученная строка: {args.str_to_out}")
    print(f"Количество повторений: {args.repeat}")

result = (args.str_to_out + "\n") * args.repeat
print(result)



