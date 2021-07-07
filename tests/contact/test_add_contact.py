from model.contact import Contact
import pytest
import random
import string


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " " * 10
    return prefix \
           + "".join(random.choice(symbols)
                     for i in range(random.randrange(maxlen)))


test_data = [Contact(firstname="", lastname="", middlename="")] + [
    Contact(firstname=random_string("firstname", 10),
            lastname=random_string("lastname", 20),
            middlename=random_string("middlename", 10))
    for i in range(5)
]


@pytest.mark.parametrize("contact", test_data, ids=[repr(x) for x in test_data])
def test_case_1_add_new_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.create_from_home(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(new_contacts, key=Contact.id_or_max) == \
           sorted(old_contacts, key=Contact.id_or_max)
