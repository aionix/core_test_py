from model.group import Group
from util.num_generator import get_cur_time

def test_modify_group_name(app):
        app.group.open_groups_page()
        group_data = Group(name='modif_python_' + get_cur_time())
        old_groups = app.group.get_group_list()
        group_data.id = old_groups[0].id
        # Check if there's a group to edit
        if app.group.count() == 0:
            app.group.create_group(Group(name="created on_" + get_cur_time()))
            old_groups = app.group.get_group_list()
        # modify first group. Get new list. update old_groups list
        app.group.modify_first_group(group_data)
        new_groups = app.group.get_group_list()
        assert len(old_groups) == len(new_groups)

        old_groups[0] =  group_data
        assert sorted(old_groups, key=Group.sort_by_id) == sorted(new_groups, key=Group.sort_by_id)

# def test_modify_group_header(app):
#         app.group.open_groups_page()
#         if app.group.count() == 0:
#             app.group.create_group(Group(name="created on_" + get_cur_time()))
#         app.group.modify_first_group(Group(footer='modif_python_' + get_cur_time()))
#         app.session.logout()


