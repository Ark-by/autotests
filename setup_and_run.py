#!/usr/bin/env python3
"""
🛠️ Автоматическая установка и запуск проекта автотестирования
"""

import os
import sys
import subprocess
import platform
from pathlib import Path

def print_colored(text, color_code):
    """Вывод цветного текста"""
    if platform.system() != "Windows":
        print(f"\033[{color_code}m{text}\033[0m")
    else:
        print(text)

def check_python():
    """Проверить наличие Python"""
    try:
        version = sys.version_info
        print_colored(f"🐍 Python версия: {version.major}.{version.minor}.{version.micro}", "32")
        return True
    except Exception as e:
        print_colored("❌ Python не найден!", "31")
        return False

def create_venv():
    """Создать виртуальное окружение"""
    venv_path = Path("venv")
    
    if venv_path.exists():
        print_colored("📁 Виртуальное окружение уже существует", "33")
        return True
    
    print_colored("🔧 Создание виртуального окружения...", "36")
    try:
        subprocess.run([sys.executable, "-m", "venv", "venv"], check=True)
        print_colored("✅ Виртуальное окружение создано", "32")
        return True
    except subprocess.CalledProcessError as e:
        print_colored(f"❌ Ошибка при создании venv: {e}", "31")
        return False

def get_venv_python():
    """Получить путь к Python в виртуальном окружении"""
    if platform.system() == "Windows":
        return Path("venv/Scripts/python.exe")
    else:
        return Path("venv/bin/python")

def install_requirements():
    """Установить зависимости"""
    venv_python = get_venv_python()
    
    if not venv_python.exists():
        print_colored("❌ Python в виртуальном окружении не найден", "31")
        return False
    
    print_colored("📦 Обновление pip...", "36")
    try:
        subprocess.run([str(venv_python), "-m", "pip", "install", "--upgrade", "pip"], check=True)
    except subprocess.CalledProcessError:
        print_colored("⚠️ Не удалось обновить pip, продолжаем...", "33")
    
    print_colored("📦 Установка зависимостей...", "36")
    try:
        subprocess.run([str(venv_python), "-m", "pip", "install", "-r", "requirements.txt"], check=True)
        print_colored("✅ Зависимости установлены", "32")
        return True
    except subprocess.CalledProcessError as e:
        print_colored(f"❌ Ошибка установки зависимостей: {e}", "31")
        return False

def run_tests():
    """Запустить тесты"""
    venv_python = get_venv_python()
    
    if not venv_python.exists():
        print_colored("❌ Виртуальное окружение не настроено", "31")
        return False
    
    print_colored("🚀 Запуск интерактивного тестового раннера...", "36")
    try:
        subprocess.run([str(venv_python), "run_interactive.py"], check=True)
        return True
    except subprocess.CalledProcessError as e:
        print_colored(f"❌ Ошибка запуска тестов: {e}", "31")
        return False
    except KeyboardInterrupt:
        print_colored("\n👋 Завершение работы...", "33")
        return True

def main():
    """Основная функция"""
    print_colored("="*50, "34")
    print_colored("🤖 АВТОМАТИЗИРОВАННАЯ УСТАНОВКА ПРОЕКТА", "34")
    print_colored("="*50, "34")
    print()
    
    # Проверяем Python
    if not check_python():
        return
    
    # Создаем venv
    if not create_venv():
        return
    
    # Устанавливаем зависимости
    if not install_requirements():
        return
    
    print_colored("\n🎉 Установка завершена успешно!", "32")
    print_colored("="*50, "34")
    
    # Запускаем тесты
    run_tests()

if __name__ == "__main__":
    main()