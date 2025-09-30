from selenium.webdriver.common.by import By

class Send_Password2:
    def __init__(self, driver):
        self.driver = driver
        
        self.view_profile_btn      = (By.XPATH, '//*[@id="citizenViewProfileBtn"]')
        self.send_password_btn2    = (By.XPATH, '//*[@id="citizenResetPasswordBtn"]')
        self.confirm               = (By.XPATH, '/html/body/div[5]/div[7]/div/button')
        
    def click_view_profile_btn(self):
        self.driver.find_element(*self.view_profile_btn).click
        
    def click_send_password(self):
        self.driver.find_element(*self.send_password_btn2).click()
        
    def click_confirm(self):
        self.driver.find_element(*self.confirm).click() 