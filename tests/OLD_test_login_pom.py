import pytest
import time
from pages.login_page import LoginPage
from utils.logger import setup_logger

@pytest.mark.login
class TestLoginPage:
    @pytest.mark.login
    def setup_method(self):
        self.logger = setup_logger()
        self.logger.info("=" * 50)

    @pytest.mark.login
    def test_successful_login(self, driver):
        self.logger.info("Запуск теста: Успешный логин")
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login("standard_user", "secret_sauce")
        assert "/inventory.html" in driver.current_url
        assert "Swag Labs" in login_page.get_page_title()
        self.logger.info("Тест пройден: Логин успешен")
        time.sleep(2)

    @pytest.mark.login
    def test_invalid_password(self, driver):
        self.logger.info("Запуск теста: Вход с неправильным паролем")
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login("standard_user", "wrong_password")
        assert login_page.is_error_message_displayed()
        error_text = login_page.get_error_message()
        assert "Username and password do not match" in error_text
        print(f"Ошибка: {error_text}")
        self.logger.info("Тест пройден: Получено сообщение об ошибке")
        time.sleep(2)

    @pytest.mark.login
    def test_locked_out_user(self, driver):
        self.logger.info("Запуск теста: Вход под заблокированным пользователем")
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login("locked_out_user", "secret_sauce")
        assert login_page.is_error_message_displayed()
        error_text = login_page.get_error_message()
        assert "Sorry, this user has been locked out" in error_text
        print(f"Ошибка: {error_text}")
        self.logger.info("Тест пройден: Получено сообщение о блокировке")
        time.sleep(2)

    @pytest.mark.login
    def test_empty_credentials(self, driver):
        self.logger.info("Запуск теста: Вход с пустыми полями")
        login_page = LoginPage(driver)
        login_page.open()
        login_page.click_login_button()
        assert login_page.is_error_message_displayed()
        error_text = login_page.get_error_message()
        assert "Username is required" in error_text
        print(f"Ошибка: {error_text}")
        self.logger.info("Тест пройден: Получено сообщение об ошибке")
        time.sleep(2)

    @pytest.mark.login
    def test_successful_logout(self, driver):
        self.logger.info("Запуск теста: Успешиный логаут")
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login("standard_user", "secret_sauce")
        login_page.logout()
        assert "https://autotests.alspio.com/" in driver.current_url
        self.logger.info("Тест пройден: Логаут успешен")
        time.sleep(2)

    @pytest.mark.login    
    def test_failed_login_for_screenshot(self, driver):
        """Тест, который упадет для демонстрации скриншота"""
        self.logger.info("Запуск теста: Демонстрация скриншота при падении")

        login_page = LoginPage(driver)
        login_page.open()
        login_page.login("invalid_user", "wrong_password")

        # Это утверждение упадет - и сделается скриншот
        assert "/inventory.html" in driver.current_url, "Этот тест должен упасть!"

        time.sleep(2)