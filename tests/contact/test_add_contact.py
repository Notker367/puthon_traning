def test_case_1_add_new_contact(app):
    app.contact.create_from_home()
    app.session.logout_from_homepage()
