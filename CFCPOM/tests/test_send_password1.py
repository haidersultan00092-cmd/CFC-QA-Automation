# import time

# from pages.search_user import Search_User
# from pages.send_password1 import Send_Password1

# def test_send_password1(logged_in_driver):
#     driver = logged_in_driver
    
#     search_user = Search_User(driver)
#     search_user.set_CNIC("3520113367979")
#     search_user.click_Search()
#     time.sleep(3)
    
#     send_password1 = Send_Password1(driver)
#     send_password1.click_send_password()
#     send_password1.click_confirm()
#     assert "Password sent successfully" in driver.page_source  