from model.group import Group
from util import num_generator


def test_delete_first_group(app):
    app.group.open_groups_page()
    if app.group.count() == 0:
        app.group.create_group(Group(name="created on_" + num_generator.get_cur_time()))

    old_groups = app.group.get_group_list()
    app.group.delete_first_group()
    new_groups = app.group.get_group_list()

    assert len(old_groups)-1 == len(new_groups)

