import allure

from webdriver_wrapper import WebDriverWrapper


class SessionHelper(WebDriverWrapper):
    # def __init__(self, app):
    #     super().__init__(self.app.driver)
    def __init__(self, app):
        self.app = app


    @allure.step
    def open_home_page(self):
        driver = self.app.driver
        driver.get("http://localhost:8090/addressbook/group.php")

    @allure.step
    def login(self, username, password):
        driver = self.app.driver
        driver.find_element_by_name("user").click()
        driver.find_element_by_name("user").clear()
        driver.find_element_by_name("user").send_keys(username)
        driver.find_element_by_name("pass").clear()
        driver.find_element_by_name("pass").send_keys(password)
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Password:'])[1]/following::input[2]").click()

    def logout(self):
        driver = self.app.driver
        driver.find_element_by_xpath("//a[text()='Logout']").click()

    def asd(self):
        self.open_home_page()
        self.wait_for_element_by_css("input[name=searchstring]", 10)

