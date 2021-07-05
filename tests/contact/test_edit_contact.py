from model.contact import Contact


def test_case_1_edit_first_contact(app):
    app.contact.create_if_not_exist(Contact(firstname="new_contact_for_edit"))
    app.contact.edit_first(Contact())
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="New_fname", lastname="New_lname")
    contact.id = old_contacts[0].id
    app.contact.edit_first(contact)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == \
           sorted(new_contacts, key=Contact.id_or_max)


def test_case_2_edit_firstname_first_contact(app):
    app.contact.create_if_not_exist(Contact(firstname="new_contact_for_edit"))
    app.contact.edit_first(contact=Contact(firstname="My_new_fName"))


def test_case_3_edit_nickname_home_first_contact(app):
    app.contact.create_if_not_exist(Contact(firstname="new_contact_for_edit"))
    app.contact.edit_first(contact=Contact(nickname="new_nickname", home="My_new_home"))


def test_case_4_edit_bday_address2_first_contact(app):
    app.contact.create_if_not_exist(Contact(firstname="new_contact_for_edit"))
    app.contact.edit_first(contact=Contact(bday="17", address2="new_addres2"))
