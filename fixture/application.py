from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

from fixture.group import GroupHelper
from fixture.session import SessionHelper


class Application:
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path='C:\Tools\drivers\chromedriver.exe')
        self.driver.implicitly_wait(10)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)

    def open_google(self):
        driver = self.driver
        driver.get("https://www.google.com/")


    def destroy(self):
        self.driver.quit()

