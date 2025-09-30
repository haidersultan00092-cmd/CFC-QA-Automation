import time

from pages.search_user import Search_User
from pages.send_password2 import Send_Password2

def test_send_password2(logged_in_driver):   # driver comes from fixture
    driver = logged_in_driver
    
    search_user = Search_User(driver)
    search_user.set_CNIC("3520113367979")
    search_user.click_Search()
    time.sleep(3)
    
    sendpassword2 = Send_Password2(driver)
    sendpassword2.click_view_profile_btn()
    time.sleep(2)
    sendpassword2.click_send_password()
    sendpassword2.click_confirm()
    
    
    assert "Haider Sultan" in driver.page_source