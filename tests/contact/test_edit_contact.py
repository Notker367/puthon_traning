def test_case_2_edit_first_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit_first()
    app.session.logout()
