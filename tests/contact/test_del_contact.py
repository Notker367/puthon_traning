from model.contact import Contact


def test_case_1_delete_first_contact(app):
    app.contact.if_not_to_create(Contact(firstname="new_contact_for_del"))
    app.contact.delete_first()
