import logging
import os

def setup_logger():
    """Простая настройка логирования"""

    # Настраиваем логирование
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler('logs/test.log', encoding='utf-8'),
            logging.StreamHandler()  # Вывод в консоль
        ],
        force=True
    )

    return logging.getLogger('test_logger')