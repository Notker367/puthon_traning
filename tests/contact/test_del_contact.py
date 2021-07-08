from model.contact import Contact
import random


def test_case_1_delete_rdm_contact(app, db, check_ui):
    app.contact.create_if_not_exist(db=db, contact=Contact(firstname="new_contact_for_del"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    app.contact.delete_contact_by_id(contact.id)
    new_contacts = db.get_contact_list()
    old_contacts.remove(contact)
    assert old_contacts == new_contacts
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == \
               sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
