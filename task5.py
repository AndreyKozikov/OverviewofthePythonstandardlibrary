# Задача 5. Запуск из командной строки
# Напишите код, который запускается из командной строки и получает на вход путь
# до директории на ПК. Соберите информацию о содержимом в виде объектов
# namedtuple. Каждый объект хранит: имя файла без расширения или название
# каталога, расширение, если это файл, флаг каталога, название родительского
# каталога. В процессе сбора сохраните данные в текстовый файл используя
# логирование.
# Подсказка № 1
# Используйте функцию os.path.join() для правильного построения путей к файлам
# и каталогам в зависимости от операционной системы.
# Подсказка № 2
# Используйте os.path.isdir() для проверки, является ли указанный путь
# директорией перед тем как пытаться получить его содержимое.
# Подсказка № 3
# Используйте os.path.splitext() для разделения имени файла на основную часть
# и расширение, где расширение можно очистить от начальной точки.
# Подсказка № 4
# Используйте logging.basicConfig() для настройки логирования, указав уровень
# логирования и формат сообщений.
# Подсказка № 5
# Определите namedtuple для хранения информации о файлах и каталогах, что
# позволяет легко управлять структурой данных и логированием.

import os
import argparse
import logging
from collections import namedtuple

FileInfo = namedtuple('FileInfo', ['name', 'extension', 'is_dir', 'parent_dir'])
logging.basicConfig(filename='file_info.log', level=logging.INFO,
                    format='%(asctime)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S', encoding="utf-8")

def get_item_info(full_path_to_item):
    parent_dir = os.path.basename(os.path.dirname(full_path_to_item))
    is_dir = os.path.isdir(full_path_to_item)

    if is_dir:
        name = os.path.basename(full_path_to_item)
        extension = ""
    else:
        name, extension = os.path.splitext(os.path.basename(full_path_to_item))
        extension = extension[1:] if extension else ''
    return FileInfo(name, extension, is_dir, parent_dir)

def directory_analize(dir_path):
    for item in os.listdir(dir_path):
        full_path_to_item = os.path.join(dir_path, item)
        item_info = get_item_info(full_path_to_item)
        log_message = (f"Name: {item_info.name}, Extension: {item_info.extension}, "
                       f"Is directory: {item_info.is_dir}, Parrent directory: {item_info.parent_dir}")
        logging.info(log_message)
        if item_info.is_dir:
            directory_analize(full_path_to_item)


def main():
    parser = argparse.ArgumentParser(description="Процесс собирает информацию о содержимом каталога, "
                                                 "переданного через параметр командной строки")
    parser.add_argument("dir", help="Путь до директории")

    args = parser.parse_args()
    directory = args.dir

    if not os.path.splitext(directory):
        print("Введенный путь не найден")
        return
    logging.info(f"Начат процесс сбора информации о содержимом директории {directory}")
    directory_analize(directory)
    logging.info("Процесс сбора информации закончен")


if __name__ == "__main__":
    main()
