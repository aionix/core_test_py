# -*- coding: utf-8 -*-
from time import sleep
from model.group import Group

# def test_open_smth(app):
#         app.driver.get("https://www.google.com/")
#         app.driver.find_element_by_xpath()
from util.num_generator import get_cur_time


def test_add_group(app):
        app.group.open_groups_page()
        old_groups = app.group.get_group_list()
        gr_to_add = Group(name="python-test" + get_cur_time(), header="asd2", footer="asd4")
        app.group.create_group(gr_to_add)
        app.group.return_to_groups_page()
        new_groups = app.group.get_group_list()
        old_groups.append(gr_to_add)

        assert len(old_groups) == len(new_groups)
        assert sorted(old_groups, key=Group.sort_by_id) == sorted(new_groups, key=Group.sort_by_id)

# def test_add_empty_group(app):
#         app.open_home_page()
#         app.login(username="admin", password="secret")
#         app.open_groups_page()
#         app.create_group(Group(name="", header="", footer=""))
#         app.return_to_groups_page()
#         app.logout()



