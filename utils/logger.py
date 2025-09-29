import logging
import os

def setup_logger():
    """Простая настройка логирования"""
    # Создаем папку для логов
    if not os.path.exists('logs'):
        os.makedirs('logs')

    # Настраиваем логирование
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(message)s',
        handlers=[
            logging.FileHandler('logs/test.log', encoding='utf-8'),
            logging.StreamHandler()  # Вывод в консоль
        ]
    )

    return logging.getLogger('test_logger')