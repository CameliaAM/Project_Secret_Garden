from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import logging


class Browser:
    s = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=s)
    driver.maximize_window()
    logging.basicConfig(level=logging.INFO)

    def maximise_window(self):
        self.driver.maximize_window()

    def close_browser(self):
        self.driver.quit()