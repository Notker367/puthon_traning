from model.contact import Contact


def test_case_1_add_new_contact(app):
    odl_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="fname", lastname="lasdname")
    app.contact.create_from_home(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(odl_contacts) + 1 == len(new_contacts)
    odl_contacts.append(contact)
    assert sorted(new_contacts, key=Contact.id_or_max) == \
           sorted(odl_contacts, key=Contact.id_or_max)
