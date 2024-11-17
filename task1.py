# Задание 1. Логирование с использованием нескольких файлов
# Напишите скрипт, который логирует разные типы сообщений в разные файлы.
# Логи уровня DEBUG и INFO должны сохраняться в debug_info.log, а логи уровня
# WARNING и выше — в warnings_errors.log.
# Подсказка № 1
# Создайте логгеры с разными уровнями логирования. Используйте
# logger.setLevel() для установки минимального уровня логирования, который будет
# обрабатываться логгером.
# Подсказка № 2
# Используйте logging.FileHandler для записи логов в файлы. Установите FileHandler
# для записи сообщений в указанные файлы и укажите уровень логирования для
# каждого обработчика с помощью метода setLevel().
# Подсказка № 3
# Настройте формат сообщений с помощью logging.Formatter. Создайте объект
# Formatter для настройки формата сообщений. Примените его к обработчикам с
# помощью метода setFormatter().
# Подсказка № 4
# Добавьте обработчики к логгеру с помощью addHandler(). После настройки
# обработчиков, добавьте их к логгеру с помощью метода addHandler().

# pip install PyYAML

import yaml
import logging.config

with open("logging_config.yaml", "r") as config_file:
    config = yaml.safe_load(config_file)
    logging.config.dictConfig(config)

debug_logger = logging.getLogger('debug_info_logger')
warning_logger = logging.getLogger('warning_logger')

debug_logger.debug('Это отладочное сообщение')
debug_logger.info('Произошло какое-то событие. Всё идёт по плану.')

warning_logger.warning('Это предупреждение')
warning_logger.error('Ошибка, что-то сломалось')
warning_logger.critical('МЫ В ОГНЕ ЧТО ДЕЛАТЬ?!?!')
