def test_case_1_add_new_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create_from_home()
    app.session.logout_from_homepage()


def test_case_2_edit_first_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit_first()
    app.session.logout_from_homepage()


def test_case_3_delete_first_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.delete_first()
    app.session.logout_from_homepage()
