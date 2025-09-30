# import time

# from pages.login_page import my_login

# def test_valid_login(driver):   # driver comes from fixture
#     driver.get("http://172.16.7.99:42381/Login/Index")
    
#     login_page = my_login(driver)
#     login_page.set_username("cfcadmin")     # ✅ use real test credentials
#     login_page.set_password("123") # ✅ correct password from site
#     login_page.click_login()
    
#     time.sleep(3)
    
#     login_page.click_cfc_center()
#     login_page.click_proceed_btn()

#     time.sleep(3)   # later replace with WebDriverWait

#     assert "Citizen Facilitation Center Dashboard" in driver.page_source

