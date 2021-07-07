from model.contact import Contact
import pytest
import random
import string








@pytest.mark.parametrize("contact", test_data, ids=[repr(x) for x in test_data])
def test_case_1_add_new_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.create_from_home(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(new_contacts, key=Contact.id_or_max) == \
           sorted(old_contacts, key=Contact.id_or_max)
