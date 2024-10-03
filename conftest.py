import pytest
from selenium import webdriver

@pytest.fixture(scope='function')
def driver():
    chrome_driver=webdriver.Chrome()
    chrome_driver.implicitly_wait(10)
    yield chrome_driver
    chrome_driver.quit()
