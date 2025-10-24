#!/usr/bin/env python3
"""
🎯 Интерактивный запуск тестов с выбором категорий и браузера
"""

import os
import subprocess
import sys
import shutil
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
    print("2. 🧪 ВЫБОР ОПРЕДЕЛЕННОГО ТЕСТА")
    print(f"3. 🌐 ВЫБОР БРАУЗЕРА (текущий: {current_browser.upper()})")
    print("4. 🗑️  ПОЛНОЕ УДАЛЕНИЕ ПРОЕКТА AUTOTESTS")
    print("0. ❌ ВЫХОД")
    print("\n" + "="*50)

def get_user_choice():
    """Получение выбора пользователя"""
    try:
        choice = input("\n🎯 Введите номер выбора (0-4): ").strip()
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

def delete_autotests_project():
    """Полное удаление проекта autotests (включая venv и корневую папку)"""
    print("\n🗑️ " + "="*60)
    print("🚨 ПОЛНОЕ УДАЛЕНИЕ ПРОЕКТА AUTOTESTS")
    print("="*60)
    print("\n⚠️  ВНИМАНИЕ: Это действие необратимо!")
    print("❌ Будут удалены ВСЕ файлы и папки проекта, включая:")
    print("   - Виртуальное окружение (venv)")
    print("   - Все тестовые файлы и отчеты")
    print("   - Корневая папка проекта autotests")
    
    # Определяем корневую папку проекта
    project_root = os.path.abspath('.')
    project_name = os.path.basename(project_root)
    
    print(f"📁 Папка проекта: {project_root}")
    
    # Показываем содержимое для удаления
    print("\n📋 Содержимое для удаления:")
    for item in os.listdir('.'):
        item_path = os.path.join(project_root, item)
        if os.path.isdir(item_path):
            print(f"   📁 {item}/")
        else:
            print(f"   📄 {item}")
    
    # Запрос подтверждения
    confirmation = input("\n🚨 Для подтверждения полного удаления введите 'УДАЛИТЬ ПРОЕКТ': ").strip()
    
    if confirmation != 'УДАЛИТЬ ПРОЕКТ':
        print("✅ Удаление отменено")
        input("\n⏎ Нажмите Enter для продолжения...")
        return False
    
    # Начинаем удаление
    print("\n🔴 Начало удаления проекта...")
    
    try:
        # Создаем список для хранения ошибок
        errors = []
        
        # Удаляем все файлы и папки в корне проекта
        for item in os.listdir('.'):
            item_path = os.path.join(project_root, item)
            try:
                if os.path.isfile(item_path) or os.path.islink(item_path):
                    os.remove(item_path)
                    print(f"✅ Удален файл: {item}")
                elif os.path.isdir(item_path):
                    shutil.rmtree(item_path)
                    print(f"✅ Удалена папка: {item}/")
            except Exception as e:
                errors.append(f"{item}: {e}")
        
        if errors:
            print(f"\n⚠️  Произошло {len(errors)} ошибок при удалении:")
            for error in errors:
                print(f"   ❌ {error}")
        
        print("\n🎉 Проект autotests успешно удален!")
        print("📁 Все файлы и папки были удалены из текущей директории.")
        print("\n💡 Теперь вы можете:")
        print("   - Закрыть это окно")
        print("   - Удалить пустую папку autotests вручную")
        print("   - Или создать новый проект")
        
        # Даем время прочитать сообщение
        input("\n⏎ Нажмите Enter для завершения...")
        return True
        
    except Exception as e:
        print(f"❌ Критическая ошибка при удалении: {e}")
        input("\n⏎ Нажмите Enter для продолжения...")
        return False

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
            result = run_specific_test(current_browser)
            if result:
                returncode, report = result
            else:
                input("\n⏎ Нажмите Enter для продолжения...")
                continue
        elif choice == 3:
            new_browser = choose_browser()
            if new_browser:
                current_browser = new_browser
                print(f"\n✅ Браузер изменен на: {current_browser.upper()}")
            input("\n⏎ Нажмите Enter для продолжения...")
            continue
        elif choice == 4:
            success = delete_autotests_project()
            if success:
                # Если удаление прошло успешно, завершаем программу
                sys.exit(0)
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