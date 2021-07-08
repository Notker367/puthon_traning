from model.contact import Contact
import random


def test_case_1_rdm_contact_data_from_homepage(app, db):
    app.contact.create_if_not_exist(db=db, contact=Contact(firstname="new_contact_for_edit"))
    old_contacts = app.contact.get_contact_list()
    index = random.randrange(len(old_contacts))
    contact_from_home_page = old_contacts[index]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert contact_from_home_page.all_phones_from_home_page \
           == app.contact.merge_for_contact_it_attributes(
        attributes=all_phones(contact_from_edit_page), map_clearing=app.contact.clear_merge_attributes)
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


def test_case_2_all_contact_data_from_homepage(app, db):
    ids = db.get_all_contact_ids()
    for id in ids:
        contact_from_home_page = app.contact.get_contact_by_id(id)
        contact_from_db = db.get_contact_by_id(id)
        assert contact_from_home_page.firstname == contact_from_db.firstname
        assert contact_from_home_page.lastname == contact_from_db.lastname.strip(" ")
        assert contact_from_home_page.address == contact_from_db.address
        assert contact_from_home_page.all_emails_from_home_page == contact_from_db.all_emails_from_home_page
        assert contact_from_home_page.all_phones_from_home_page == contact_from_db.all_phones_from_home_page


