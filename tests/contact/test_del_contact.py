from model.contact import Contact


def test_case_1_delete_first_contact(app):
    app.contact.create_if_not_exist(Contact(firstname="new_contact_for_del"))
    odl_contacts = app.contact.get_contact_list()
    app.contact.delete_first()
    assert len(odl_contacts) - 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    odl_contacts[0:1] = []
    assert odl_contacts == new_contacts

