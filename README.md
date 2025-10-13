# Autotests Project

Проект автоматизированного тестирования.

## Структура проекта

```
autotests/                          # 🎯 Корневая директория проекта
│
├── 📁 pages/                       # 📄 Page Object Model - классы для работы со страницами
│   ├── __init__.py                 #    Инициализатор пакета
│   ├── base_page.py                # 🏠 Базовый класс для всех страниц
│   ├── login_page.py               # 🔐 Страница авторизации
│   ├── products_page.py            # 🛍️ Страница товаров
│   ├── cart_page.py                # 🛒 Страница корзины
│   └── checkout_page.py            # 📦 Страница оформления заказа
│
├── 📁 tests/                       # 🧪 Тестовые сценарии - все автотесты проекта
│   ├── __init__.py                 #    Инициализатор пакета
│   ├── test_login_pom.py           # ✅ Базовые тесты логина (Page Object Pattern)
│   ├── test_parametrized_login.py  # 🔄 Параметризованные тесты - один тест, много данных
│   ├── test_data_driven.py         # 📊 Data-driven тесты - данные из внешних источников
│   ├── test_cart.py                # 🛒 Тесты корзины
│   ├── test_products.py            # 🛍️ Тесты товаров
│   └── test_e2e_flow.py            # 🔁 E2E тесты полного цикла покупки
│
├── 📁 locators/                    # 🎯 Локаторы элементов - селекторы для поиска элементов
│   ├── __init__.py                 #    Инициализатор пакета
│   ├── login_page_locators.py      # 📍 Локаторы страницы логина (ID, XPath, CSS)
│   ├── products_page_locators.py   # 🛍️ Локаторы страницы товаров
│   ├── cart_page_locators.py       # 🛒 Локаторы страницы корзины
│   └── checkout_page_locators.py   # 📦 Локаторы страницы оформления заказа
│
├── 📁 logs/                        # 📝 Логи выполнения - запись результатов тестирования
│   └── test.log                    # 🕒 Автоматически создаваемый файл логов тестов
│
├── 📁 screenshots/                 # 🖼️ Скриншоты - снимки экрана при падении тестов
│   └── FAILED_*.png                # ❌ Скриншоты с префиксом FAILED_ при ошибках
│
├── 📁 data/                        # 💾 Тестовые данные - внешние данные для тестов
│   ├── __init__.py                 #    Инициализатор пакета
│   └── test_data.json              # 👥 JSON-файл с пользователями для тестирования
│
├── 📁 utils/                       # 🛠️ Вспомогательные утилиты - общие функции
│   ├── __init__.py                 #    Инициализатор пакета
│   ├── logger.py                   # 📋 Настройка логирования - конфигурация логгера
│   └── wait_utils.py               # ⏳ Утилиты ожидания
│
├── 📁 reports/                     # 📊 HTML отчеты - результаты выполнения тестов
│   └── report.html                 # 📄 Автоматически генерируемый отчет
│
├── 🔧 conftest.py                  # ⚙️ Фикстуры pytest - настройка драйвера, хуки (обновленный)
├── ⚙️ pytest.ini                   # 📄 Конфигурация pytest - маркеры, настройки запуска
└── 🚀 run_tests.py                 # ▶️ Скрипт для запуска тестов с настройками (опционально)
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

#Запуск интерактивного скрипта
python run_interactive.py

# Запуск в Firefox
pytest tests/ --browser=firefox

# Запуск в Chrome
pytest tests/ --browser=chrome
```
