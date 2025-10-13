import pytest
import os
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


for folder in ['screenshots', 'reports']:
    if not os.path.exists(folder):
        os.makedirs(folder)

def take_screenshot(driver, test_name):
    """Функция для создания скриншотов"""

    timestamp = datetime.now().strftime("%H%M%S")
    filename = f"screenshots/{test_name}_{timestamp}.png"

    driver.save_screenshot(filename)
    print(f"Скриншот сохранен: {filename}")

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Выбор браузера: chrome или firefox")

@pytest.fixture
def driver(request):
    
    browser_name = request.config.getoption("--browser")
    
    if browser_name == "firefox":
        service = FirefoxService(GeckoDriverManager().install())
        driver = webdriver.Firefox(service=service)
    else:
        service = ChromeService(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)
    
    driver.implicitly_wait(2)
    driver.maximize_window()
    
    yield driver
    driver.quit()

@pytest.fixture(autouse=True)
def screenshot_on_failure(request, driver):
    """Автоматически делает скриншот при падении теста"""
    def fin():
        if hasattr(request.node, 'rep_call') and request.node.rep_call.failed:
            test_name = request.node.name
            take_screenshot(driver, f"FAILED_{test_name}")
    
    request.addfinalizer(fin)

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Хук для получения результата теста"""
    outcome = yield
    rep = outcome.get_result()

    setattr(item, "rep_" + rep.when, rep)