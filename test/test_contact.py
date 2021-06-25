
def test_case_1_add_new_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create_from_home()
    app.session.logout_from_homepage()
