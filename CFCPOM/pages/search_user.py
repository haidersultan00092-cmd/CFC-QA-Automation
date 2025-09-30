from selenium.webdriver.common.by import By

class Search_User:
    def __init__(self, driver):
        self.driver = driver
        self.CNIC_input     = (By.XPATH, '//*[@id="CitizenCNIC"]')
        self.search_button  = (By.XPATH, '//*[@id="BtnCitizenSearchCfcDashboard"]')
        
    def set_CNIC(self, CNIC):
        self.driver.find_element(*self.CNIC_input).send_keys(CNIC)
        
    def click_Search(self):
        self.driver.find_element(*self.search_button).click()
        