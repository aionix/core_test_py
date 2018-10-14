# -*- coding: utf-8 -*-
from time import sleep
from model.group import Group

# def test_open_smth(app):
#         app.driver.get("https://www.google.com/")
#         app.driver.find_element_by_xpath()


def test_add_group(app):
        app.session.open_home_page()
        sleep(1)
        app.session.login(username="admin", password="secret")
        app.group.open_groups_page()
        app.group.create_group(Group(name="python-test", header="asd2", footer="asd4"))
        app.group.return_to_groups_page()
        app.session.logout()

# def test_add_empty_group(app):
#         app.open_home_page()
#         app.login(username="admin", password="secret")
#         app.open_groups_page()
#         app.create_group(Group(name="", header="", footer=""))
#         app.return_to_groups_page()
#         app.logout()



