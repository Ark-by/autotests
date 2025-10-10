# Autotests Project

Проект автоматизированного тестирования.

## Структура проекта

```
autotests/
├── pages/          # Page Objects - классы для работы со страницами приложения
│   ├── __init__.py
│   ├── login_page.py      # Страница логина
├── tests/          # Тестовые сценарии
│   ├── __init__.py
│   ├── test_login_pom.py          # Базовые тесты логина
│   ├── test_parametrized_login.py # Параметризованные тесты
│   └── test_data_driven.py        # Data-driven тесты
├── locators/       # Локаторы элементов
│   ├── __init__.py
│   ├── login_page_locators.py     # Локаторы страницы логина
├── logs/           # Логи выполнения тестов
│   └── test.log    # Автоматически создаваемый файл логов
├── screenshots/    # Скриншоты при падении тестов
│   └── FAILED_*.png  # Скриншоты с префиксом FAILED_
├── data/           # Тестовые данные и конфигурации
│   ├── __init__.py
│   ├── test_users.json    # JSON с пользователями для тестов
├── utils/          # Вспомогательные утилиты и хелперы
│   ├── __init__.py
│   ├── logger.py          # Настройка логирования
├── conftest.py     # Фикстуры pytest - настройка драйвера, хуки
└── pytest.ini      # Конфигурация pytest - маркеры, настройки
```

## Установка и запуск

```bash
# Создание виртуального окружения
python -m venv venv

# Активация (Windows)
venv\Scripts\activate

# Деактивация (Windows)
venv\Scripts\deactivate
или просто deactivate

# Установка зависимостей
pip install -r requirements.txt
или
pip install selenium pytest webdriver-manager 

# Запуск в Firefox
pytest tests/ --browser=firefox -v

# Запуск в Chrome
pytest tests/ --browser=chrome -v
```
