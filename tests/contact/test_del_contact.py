from model.contact import Contact


def test_case_1_delete_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create_from_home(Contact(firstname="new_contact_for_del"))
    app.contact.delete_first()
