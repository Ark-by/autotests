#!/usr/bin/env python3
"""
🎯 Интерактивный запуск тестов с выбором категорий и браузера
"""

import os
import subprocess
import sys
from datetime import datetime

def clear_screen():
    """Очистка экрана"""
    os.system('cls' if os.name == 'nt' else 'clear')

def print_menu(current_browser):
    """Вывод меню выбора тестов с текущим браузером"""
    print("="*50)
    print("🤖 АВТОМАТИЗИРОВАННЫЙ ЗАПУСК ТЕСТОВ")
    print("="*50)
    print("\n📋 ВЫБЕРИТЕ КАТЕГОРИЮ ТЕСТОВ:\n")
    print("1. ✅ ВСЕ ТЕСТЫ")
    print("2. 🔐 ТЕСТЫ АВТОРИЗАЦИИ")
    print("3. 🛍️  ТЕСТЫ ТОВАРОВ")
    print("4. 🛒 ТЕСТЫ КОРЗИНЫ")
    print("5. 🔁 E2E ТЕСТЫ (полный цикл покупки)")
    print("6. 📊 DATA-DRIVEN ТЕСТЫ")
    print("7. 🧪 ВЫБОР ОПРЕДЕЛЕННОГО ТЕСТА")
    print(f"8. 🌐 ВЫБОР БРАУЗЕРА (текущий: {current_browser.upper()})")
    print("9. 📋 ТОЛЬКО ОТЧЕТ (без запуска тестов)")
    print("0. ❌ ВЫХОД")
    print("\n" + "="*50)

def get_user_choice():
    """Получение выбора пользователя"""
    try:
        choice = input("\n🎯 Введите номер выбора (0-9): ").strip()
        return int(choice)
    except ValueError:
        return -1

def choose_browser():
    """Выбор браузера для тестов"""
    print("\n🌐 ВЫБЕРИТЕ БРАУЗЕР ДЛЯ ТЕСТИРОВАНИЯ:\n")
    print("1. 🚀 Chrome (по умолчанию)")
    print("2. 🦊 Firefox")
    print("3. ↩️  Назад")
    
    try:
        choice = input("\n🎯 Введите номер выбора (1-3): ").strip()
        browser_choice = int(choice)
        
        if browser_choice == 1:
            return "chrome"
        elif browser_choice == 2:
            return "firefox"
        elif browser_choice == 3:
            return None
        else:
            print("❌ Неверный выбор! Используется Chrome.")
            return "chrome"
    except ValueError:
        print("❌ Неверный ввод! Используется Chrome.")
        return "chrome"

def run_tests(command, category_name, browser="chrome"):
    """Запуск тестов с генерацией отчета и выбором браузера"""
    # Создаем папку reports если не существует
    if not os.path.exists('reports'):
        os.makedirs('reports')
    
    # Генерируем имя файла с timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    report_file = f"reports/{category_name}_{browser}_{timestamp}.html"
    
    # Добавляем опции для отчета и браузера
    full_command = command + [
        f'--browser={browser}',
        f'--html={report_file}',
        '--self-contained-html',
        '-v',
        '-s'
    ]
    
    print(f"\n🚀 Запуск: {category_name}")
    print(f"🌐 Браузер: {browser.upper()}")
    print(f"📊 Отчет будет сохранен в: {report_file}")
    print("⏳ Выполнение...\n")
    
    # Запускаем тесты
    result = subprocess.run(full_command)
    
    return result.returncode, report_file

def run_all_tests(browser="chrome"):
    """Запуск всех тестов"""
    return run_tests(['pytest', 'tests/'], "ALL_TESTS", browser)

def run_login_tests(browser="chrome"):
    """Запуск тестов авторизации"""
    return run_tests(['pytest', 'tests/test_login_pom.py', 'tests/test_parametrized_login.py', '-m', 'login'], "LOGIN_TESTS", browser)

def run_products_tests(browser="chrome"):
    """Запуск тестов товаров"""
    return run_tests(['pytest', 'tests/test_products.py', '-m', 'products'], "PRODUCTS_TESTS", browser)

def run_cart_tests(browser="chrome"):
    """Запуск тестов корзины"""
    return run_tests(['pytest', 'tests/test_cart.py', '-m', 'cart'], "CART_TESTS", browser)

def run_e2e_tests(browser="chrome"):
    """Запуск E2E тестов"""
    return run_tests(['pytest', 'tests/test_e2e_flow.py', '-m', 'e2e'], "E2E_TESTS", browser)

def run_data_driven_tests(browser="chrome"):
    """Запуск data-driven тестов"""
    return run_tests(['pytest', 'tests/test_data_driven.py', '-m', 'data_driven'], "DATA_DRIVEN_TESTS", browser)

def run_specific_test(browser="chrome"):
    """Запуск конкретного теста"""
    print("\n📁 Доступные тестовые файлы:")
    test_files = [f for f in os.listdir('tests') if f.startswith('test_') and f.endswith('.py')]
    for i, file in enumerate(test_files, 1):
        print(f"   {i}. {file}")
    
    try:
        choice = int(input("\n🎯 Выберите файл (номер): "))
        if 1 <= choice <= len(test_files):
            selected_file = test_files[choice-1]
            print(f"\n🧪 Запуск тестов из: {selected_file}")
            return run_tests(['pytest', f'tests/{selected_file}'], f"SPECIFIC_{selected_file[:-3]}", browser)
        else:
            print("❌ Неверный выбор!")
            return None
    except ValueError:
        print("❌ Введите число!")
        return None

def show_report():
    """Показать информацию об отчетах"""
    if os.path.exists('reports'):
        reports = [f for f in os.listdir('reports') if f.endswith('.html')]
        if reports:
            print("\n📊 Доступные отчеты:")
            for i, report in enumerate(sorted(reports, reverse=True)[:5], 1):  # последние 5 отчетов
                print(f"   {i}. {report}")
            print(f"\n💡 Всего отчетов: {len(reports)}")
            print("📂 Папка: reports/")
            
            # Предлагаем открыть последний отчет
            if reports and input("\n🖥️  Открыть последний отчет в браузере? (y/N): ").lower() == 'y':
                import webbrowser
                latest_report = sorted(reports, reverse=True)[0]
                webbrowser.open(f'file://{os.path.abspath(os.path.join("reports", latest_report))}')
        else:
            print("❌ Отчеты не найдены!")
    else:
        print("❌ Папка reports не существует!")

def main():
    """Основная функция"""
    current_browser = "chrome"  # Браузер по умолчанию
    
    while True:
        clear_screen()
        print_menu(current_browser)
        choice = get_user_choice()
        
        if choice == 0:
            print("\n👋 До свидания!")
            break
        elif choice == 1:
            returncode, report = run_all_tests(current_browser)
        elif choice == 2:
            returncode, report = run_login_tests(current_browser)
        elif choice == 3:
            returncode, report = run_products_tests(current_browser)
        elif choice == 4:
            returncode, report = run_cart_tests(current_browser)
        elif choice == 5:
            returncode, report = run_e2e_tests(current_browser)
        elif choice == 6:
            returncode, report = run_data_driven_tests(current_browser)
        elif choice == 7:
            result = run_specific_test(current_browser)
            if result:
                returncode, report = result
            else:
                input("\n⏎ Нажмите Enter для продолжения...")
                continue
        elif choice == 8:
            new_browser = choose_browser()
            if new_browser:
                current_browser = new_browser
                print(f"\n✅ Браузер изменен на: {current_browser.upper()}")
            input("\n⏎ Нажмите Enter для продолжения...")
            continue
        elif choice == 9:
            show_report()
            input("\n⏎ Нажмите Enter для продолжения...")
            continue
        else:
            print("❌ Неверный выбор! Попробуйте снова.")
            input("\n⏎ Нажмите Enter для продолжения...")
            continue
        
        # Показываем результат
        if returncode == 0:
            print(f"\n✅ Тесты завершены успешно!")
        else:
            print(f"\n❌ Некоторые тесты завершились с ошибками")
        
        print(f"📊 Отчет: {report}")
        
        # Предлагаем открыть отчет в браузере
        if input("\n🖥️  Открыть отчет в браузере? (y/n): ").lower() == 'y':
            import webbrowser
            webbrowser.open(f'file://{os.path.abspath(report)}')
        
        input("\n⏎ Нажмите Enter для продолжения...")

if __name__ == "__main__":
    main()