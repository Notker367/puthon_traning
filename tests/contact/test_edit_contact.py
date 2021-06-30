from model.contact import Contact


def test_case_1_edit_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create_from_home(Contact(firstname="new_contact_for_edit"))
    app.contact.edit_first(Contact())


def test_case_2_edit_firstname_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create_from_home(Contact(firstname="new_contact_for_edit"))
    app.contact.edit_first(contact=Contact(firstname="My_new_fName"))


def test_case_3_edit_nickname_home_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create_from_home(Contact(firstname="new_contact_for_edit"))
    app.contact.edit_first(contact=Contact(nickname="new_nickname", home="My_new_home"))


def test_case_4_edit_bday_address2_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create_from_home(Contact(firstname="new_contact_for_edit"))
    app.contact.edit_first(contact=Contact(bday="17", address2="new_addres2"))
