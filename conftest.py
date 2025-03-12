import pytest
import json
from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Choose browser: chrome or edge")

@pytest.fixture(scope="function")
def driver(request):
    browser = request.config.getoption("--browser")

    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "edge":
        driver = webdriver.Edge()
    else:
        raise ValueError(f"Unsupported Browser {browser}")

    driver.maximize_window()
    yield driver
    driver.quit()


def load_config():
    with open("resources/config.json", "r") as file:
        return json.load(file)

@pytest.fixture(scope="session")
def configure():
    """Fixture to provide config data to tests."""
    return load_config()






