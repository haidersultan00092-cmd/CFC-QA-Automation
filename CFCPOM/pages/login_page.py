from selenium.webdriver.common.by import By

class my_login:
    def __init__(self, driver):
        self.driver = driver
        self.username_input     = (By.XPATH, '//*[@id="input_userName"]')
        self.password_input     = (By.XPATH, '//*[@id="input_password"]')
        self.login_button       = (By.XPATH, '//*[@id="login_btn"]')
        self.select_cfc         = (By.XPATH, '//*[@id="SelectedCfcId"]/option[1]')
        self.proceed_login_btn  = (By.XPATH, '//*[@id="btnModalClose"]')
        
    def set_username(self, username):
        """Type the username"""
        self.driver.find_element(*self.username_input).send_keys(username)

    def set_password(self, password):
        """Type the password"""
        self.driver.find_element(*self.password_input).send_keys(password)

    def click_login(self):
        """Click on the login button"""
        self.driver.find_element(*self.login_button).click()
        
    def click_cfc_center(self):
        self.driver.find_element(*self.select_cfc).click()
        
    def click_proceed_btn(self):
        self.driver.find_element(*self.proceed_login_btn).click()