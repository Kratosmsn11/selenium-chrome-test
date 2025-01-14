from selenium.webdriver.common.by import By

class SearchBox:
    def __init__(self, driver):
        self.driver = driver
        self.input_field = (By.ID, "APjFqb")

    def search_box(self):
        self.driver.find_element(self.input_field)