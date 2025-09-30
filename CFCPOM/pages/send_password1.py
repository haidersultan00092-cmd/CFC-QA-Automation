from selenium.webdriver.common.by import By

class Send_Password1:
    def __init__(self, driver):
        self.driver = driver
        self.send_password_btn1    = (By.XPATH, '//*[@id="citizenResetPasswordBtn"]')
        self.confirm               = (By.XPATH, '/html/body/div[4]/div[2]/p[2]/button[2]')
        
    def click_send_password(self):
        self.driver.find_element(*self.send_password_btn1).click()
        
    def click_confirm(self):
        self.driver.find_element(*self.confirm).click() 