# Autotests Project

Проект автоматизированного тестирования.

## Структура проекта

```
autotests/                          # 🎯 Корневая директория проекта
│
├── 📁 pages/                       # 📄 Page Object Model - классы для работы со страницами
│   ├── __init__.py                 #    Инициализатор пакета
│   └── login_page.py               # 🔐 Страница авторизации - методы и элементы логина
│
├── 📁 tests/                       # 🧪 Тестовые сценарии - все автотесты проекта
│   ├── __init__.py                 #    Инициализатор пакета
│   ├── test_login_pom.py           # ✅ Базовые тесты логина (Page Object Pattern)
│   ├── test_parametrized_login.py  # 🔄 Параметризованные тесты - один тест, много данных
│   └── test_data_driven.py         # 📊 Data-driven тесты - данные из внешних источников
│
├── 📁 locators/                    # 🎯 Локаторы элементов - селекторы для поиска элементов
│   ├── __init__.py                 #    Инициализатор пакета
│   └── login_page_locators.py      #  📍 Локаторы страницы логина (ID, XPath, CSS)
│
├── 📁 logs/                        # 📝 Логи выполнения - запись результатов тестирования
│   └── test.log                    # 🕒 Автоматически создаваемый файл логов тестов
│
├── 📁 screenshots/                 # 🖼️ Скриншоты - снимки экрана при падении тестов
│   └── FAILED_*.png                # ❌ Скриншоты с префиксом FAILED_ при ошибках
│
├── 📁 data/                        # 💾 Тестовые данные - внешние данные для тестов
│   ├── __init__.py                 #    Инициализатор пакета
│   └── test_users.json             # 👥 JSON-файл с пользователями для тестирования
│
├── 📁 utils/                       # 🛠️ Вспомогательные утилиты - общие функции
│   ├── __init__.py                 #    Инициализатор пакета
│   └── logger.py                   # 📋 Настройка логирования - конфигурация логгера
│
├── 🔧 conftest.py                  # ⚙️ Фикстуры pytest - настройка драйвера, хуки
└── ⚙️ pytest.ini                   # 📄 Конфигурация pytest - маркеры, настройки запуска
```

## Установка и запуск

```bash
# Клонирование проекта
git clone https://github.com/Ark-by/autotests.git

# Переход в каталог проекта
cd autotests

# Создание виртуального окружения
python -m venv venv

# Активация (Windows)
venv\Scripts\activate

# Деактивация (Windows)
venv\Scripts\deactivate

# Установка зависимостей
pip install -r requirements.txt
или
pip install selenium pytest webdriver-manager 

# Запуск в Firefox
pytest tests/ --browser=firefox -v

# Запуск в Chrome
pytest tests/ --browser=chrome -v
```
