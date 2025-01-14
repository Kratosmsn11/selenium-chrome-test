from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

class BrowserManager:
    def __init__(self):
        self.driver = None
        self.url = "https://www.google.com/"

    def start_driver(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    def close_driver(self):
        if self.driver:
            self.driver.quit()

    def get_website(self):
        self.driver.get(self.url)