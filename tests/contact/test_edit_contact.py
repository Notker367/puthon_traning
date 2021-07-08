from model.contact import Contact
import random


def test_case_1_edit_rdm_contact(app, db, check_ui):
    app.contact.create_if_not_exist(db, Contact(firstname="new_contact_for_edit"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    index = old_contacts.index(contact)
    new_contact = Contact(firstname="New_fname_r", lastname="New_lname")
    app.contact.edit_by_id(id=contact.id, contact=new_contact)
    new_contacts = db.get_contact_list()
    old_contacts[index] = new_contact
    assert old_contacts == new_contacts
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)


