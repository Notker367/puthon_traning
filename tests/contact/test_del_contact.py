from model.contact import Contact
from random import randrange


def test_case_1_delete_first_contact(app):
    app.contact.create_if_not_exist(Contact(firstname="new_contact_for_del"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    app.contact.delete_first()
    assert len(old_contacts) - 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[0:1] = []
    assert old_contacts == new_contacts

