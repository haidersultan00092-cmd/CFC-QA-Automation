import pytest
import time
from selenium import webdriver
from pages.login_page import my_login

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture
def logged_in_driver(driver):
    """Reusable login fixture"""
    driver.get("http://172.16.7.99:42381/Login/Index")
    
    login_page = my_login(driver)
    login_page.set_username("cfcadmin")
    login_page.set_password("123")
    login_page.click_login()
    
    time.sleep(3)
    
    login_page.click_cfc_center()
    login_page.click_proceed_btn()
    
    time.sleep(3)
    return driver
