import pytest
import time
from pages.login_page import LoginPage

class TestLoginPage:
    def test_successful_login(self, driver):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login("standard_user", "secret_sauce")
        assert "/inventory.html" in driver.current_url
        assert "Swag Labs" in login_page.get_page_title()
        time.sleep(2)

    def test_invalid_password(self, driver):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login("standard_user", "wrong_password")
        assert login_page.is_error_message_displayed()
        error_text = login_page.get_error_message()
        assert "Username and password do not match" in error_text
        print(f"Ошибка: {error_text}")
        time.sleep(2)

    def test_locked_out_user(self, driver):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login("locked_out_user", "secret_sauce")
        assert login_page.is_error_message_displayed()
        error_text = login_page.get_error_message()
        assert "Sorry, this user has been locked out" in error_text
        print(f"Ошибка: {error_text}")
        time.sleep(2)

    def test_empty_credentials(self, driver):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.click_login_button()
        assert login_page.is_error_message_displayed()
        error_text = login_page.get_error_message()
        assert "Username is required" in error_text
        print(f"Ошибка: {error_text}")
        time.sleep(2)

    def test_successful_logout(self, driver):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login("standard_user", "secret_sauce")
        login_page.logout()
        assert "https://autotests.alspio.com/" in driver.current_url