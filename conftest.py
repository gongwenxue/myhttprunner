import pytest
from selenium import webdriver
import requests



@pytest.fixture(scope="session")
def driver(request):
    driver = webdriver.Chrome(
        executable_path='/Users/lindafang/PycharmProjects/testframework/excise/driver/chromedriver')

    def close_browser():
        driver.quit()

    request.addfinalizer(close_browser)
    return driver


python = "^3.6"
requests = "^2.22.0"
pytest = "^5.3.2"
selenium = "^3.141.0"