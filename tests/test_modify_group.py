import time

import allure
import pytest
from allure_commons.types import AttachmentType
from selenium.common.exceptions import WebDriverException

from model.group import Group
from util.num_generator import get_cur_time


@pytest.mark.dependency()
def test_modify_group_name(app):
        app.group.open_groups_page()
        #check if gr exists
        if app.group.count() == 0:
            app.group.create_group(Group(name="created on_" + get_cur_time()))
        #prepare data
        group_data = Group(name='modif_python_' + get_cur_time())
        old_groups = app.group.get_group_list()
        group_data.id = old_groups[0].id
        # modify first group. Get new list. update old_groups list
        app.group.modify_first_group(group_data)
        new_groups = app.group.get_group_list()
        assert len(old_groups) == len(new_groups)+1
        ##
        old_groups[0] =  group_data
        assert sorted(old_groups, key=Group.sort_by_id) == sorted(new_groups, key=Group.sort_by_id)


# def test_do_screenshot(app):
#         app.driver.get("https://www.google.com/")
#         time.sleep(3)
#         a = app.driver.find_element_by_xpath("//input[@name='btnK']").text
#         #assert a == "Поиск в Google"
#         raise WebDriverException
#
# def test_logging(app):
#         app.driver.get("https://www.google.com/")





# @pytest.mark.dependency(depends=["test_modify_group_name"])
# def test_modify_group_header(app):
#         app.group.open_groups_page()
#         if app.group.count() == 0:
#             app.group.create_group(Group(name="created on_" + get_cur_time()))
#         app.group.modify_first_group(Group(name='dependent_1 ' + get_cur_time()))
#         app.session.logout()
#
#
# @pytest.mark.dependency()
# def test_b():
#     assert True
#
#
# @pytest.mark.dependency(depends=["test_b"])
# def test_modify_group_header2(app):
#         app.group.open_groups_page()
#         if app.group.count() == 0:
#             app.group.create_group(Group(name="created on_" + get_cur_time()))
#         app.group.modify_first_group(Group(name='dependent_2 ' + get_cur_time()))
#         app.session.logout()


