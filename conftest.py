import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

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