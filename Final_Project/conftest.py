from webbrowser import Chrome
from webdriver_manager.chrome import ChromeDriverManager
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.drivers.firefox import GeckoDriver
from webdriver_manager.firefox import GeckoDriverManager


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome',
                     help="Choose browser: chrome or firefox")
    parser.addoption(
        "--language",
        action="store",
        default="en",
        help="language to use for tests (e.g., en, ru)"
    )

@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    browser = None
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        #options = webdriver.ChromeOptions()
        #options.add_argument("--headless")
        service = Service(executable_path=ChromeDriverManager().install())
        browser = webdriver.Chrome(service=service, options=options)
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        service = Service(executable_path=GeckoDriverManager().install())
        browser = webdriver.Firefox()
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nquit browser..")
    browser.quit()