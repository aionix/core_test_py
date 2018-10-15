from model.group import Group


def test_modify_group_name(app):
    app.group.open_groups_page()
    app.group.modify_first_group(Group(name='modified_python_group3'))
    app.session.logout()

# def test_modify_group_header(app):
#     app.session.open_home_page()
#     app.session.login(username="admin", password="secret")
#     app.group.modify_first_group(Group(footer="modif python footer"))
#     app.session.logout()
