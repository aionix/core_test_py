from selenium import webdriver


from fixture.group import GroupHelper
from fixture.session import SessionHelper


class Application:

    def __init__(self, browser, base_url):
        if browser == "firefox":
            self.driver = webdriver.Firefox(executable_path='C:\Tools\drivers\geckodriver.exe')
        elif browser == "chrome":
            self.driver = webdriver.Chrome(executable_path='C:\Tools\drivers\chromedriver.exe')
        elif browser == "ie":
            self.driver = webdriver.Ie(executable_path='C:\Tools\drivers\IEDriverServer')
        else:
            raise ValueError("Unknown browser %s" %browser)
        self.driver.implicitly_wait(5)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)


    def open_google(self):
        driver = self.driver
        driver.get("https://www.google.com/")

    def finish(self):
        #self.driver.delete_all_cookies()
        self.driver.quit()

    def is_valid(self):
        try:
            self.driver.current_url()
            return True
        except:
            return False

