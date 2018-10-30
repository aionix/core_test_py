from selenium.common.exceptions import NoSuchElementException

from model.group import Group


class GroupHelper:
    def __init__(self, app):
        self.app = app


    def return_to_groups_page(self):
        driver = self.app.driver
        driver.find_element_by_link_text("group page").click()

    def create_group(self, group):
        driver = self.app.driver
        driver.find_element_by_name("new").click()
        self.fill_group_form(group)
        driver.find_element_by_name("submit").click()

    def fill_group_form(self, group):
        driver = self.app.driver
        self.update_field_value("group_name", group.name)
        self.update_field_value("group_header", group.header)
        self.update_field_value("group_footer", group.footer)

    def update_field_value(self, field_name, text):
        driver = self.app.driver
        if text is not None:
            driver.find_element_by_name(field_name).click()
            driver.find_element_by_name(field_name).clear()
            driver.find_element_by_name(field_name).send_keys(text)

    def open_groups_page(self):
        driver = self.app.driver
        driver.find_element_by_link_text("groups").click()

    def delete_first_group(self):
        driver = self.app.driver
        self.open_groups_page()
        self.select_first_group()
        driver.find_element_by_name("delete").click()
        self.return_to_groups_page()

    def select_first_group(self):
        driver = self.app.driver
        driver.find_element_by_name("selected[]").click()


    def modify_first_group(self, new_group_data):
        driver = self.app.driver
        self.open_groups_page()
        self.select_first_group()
        driver.find_element_by_name("edit").click()
        self.fill_group_form(new_group_data)
        # updating group
        driver.find_element_by_name("update").click()
        self.return_to_groups_page()

    def count(self):
        driver = self.app.driver
        self.open_groups_page()
        return len(driver.find_elements_by_name("selected[]"))

    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True

    def get_group_list(self):
        driver = self.app.driver
        self.open_groups_page()
        elements = driver.find_elements_by_css_selector("span[class='group']")
        groups = []
        for el in elements:
            text = el.text
            id = el.find_element_by_name("selected[]").get_attribute("value")
            groups.append(Group(name=text, id=id))
        return groups


