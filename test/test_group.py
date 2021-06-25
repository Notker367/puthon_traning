def test_case_1_add_new_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create_from_home()
    app.session.logout_from_homepage()


def test_case_2_edit_first_group(app):
    app.session.login(username="admin", password="secret")
    app.group.edit_first_from_home()
    app.session.logout_from_homepage()


def test_case_3_delete_first_group(app):
    app.session.login(username="admin", password="secret")
    app.group.delete_first_from_home()
    app.session.logout_from_homepage()
