import pytest
import json
from selenium import webdriver

"""This is the driver fixture"""
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


"""This loads the configurations and provide config data to the tests"""
def load_config():
    with open("resources/config.json", "r") as file:
        return json.load(file)
@pytest.fixture(scope="session")
def configure():
    return load_config()






