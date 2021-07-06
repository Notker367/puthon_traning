from model.contact import Contact
import random


def test_case_1_rdm_contact_data_from_homepage(app):
    app.contact.create_if_not_exist(Contact(firstname="new_contact_for_edit"))
    old_contacts = app.contact.get_contact_list()
    # index = random.randrange(len(old_contacts))
    index = 9
    contact_from_home_page = old_contacts[index]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert contact_from_home_page.all_phones_from_home_page \
           == app.contact.merge_for_contact_it_attributes(
        attributes=all_phones(contact_from_edit_page))
    assert contact_from_home_page.all_emails_from_home_page \
           == app.contact.merge_for_contact_it_attributes(
        attributes=all_email(contact_from_edit_page))
    assert contact_from_home_page.firstname == contact_from_edit_page.firstname
    assert contact_from_home_page.lastname == contact_from_edit_page.lastname
    assert contact_from_home_page.address == contact_from_edit_page.address


def all_email(contact):
    return [contact.email,
            contact.email2,
            contact.email3]


def all_phones(contact):
    return [contact.home,
            contact.mobile,
            contact.work,
            contact.phone2]
