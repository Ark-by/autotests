# Autotests Project

Проект автоматизированного тестирования с использованием Page Object Model (POM).

## Структура проекта

```
autotests/
├── pages/          # Page Objects
├── tests/          # Тестовые сценарии
├── locators/       # Локаторы элементов
├── logs/           # Логи
├── screenshots     # Скриншоты
├── conftest.py     # Фикстуры pytest
└── pytest.ini      # Конфигурация pytest
```

## Установка и запуск

```bash
# Создание виртуального окружения
python -m venv venv

# Активация (Windows)
venv\Scripts\activate

# Установка зависимостей
pip install -r requirements.txt

# Запуск в Firefox
pytest tests/ --browser=firefox -v

# Запуск в Chrome
pytest tests/ --browser=chrome -v
```

## Технологии

- Python
- Selenium
- Pytest
- Page Object Model
