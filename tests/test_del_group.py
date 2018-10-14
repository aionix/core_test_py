

def test_delete_first_group(app):
    app.session.open_home_page()
    app.session.login(username="admin", password="secret")
    app.group.delete_first_group()
    app.session.logout()
