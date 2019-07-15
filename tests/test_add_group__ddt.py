# -*- coding: utf-8 -*-
from time import sleep

import pytest
from model.group import Group


from util.num_generator import get_cur_time

testdata = [
    Group(name="ddt_" + get_cur_time(), footer="asd4"),
    Group(name="ddt__", footer="")
]

@pytest.mark.parametrize("group", testdata, ids=[repr(x) for x in testdata])
def test_add_group(app, group):
        app.group.open_groups_page()
        app.group.create_group(group)
        app.group.return_to_groups_page()
        app.session.logout()





