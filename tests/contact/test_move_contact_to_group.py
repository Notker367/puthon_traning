import random
from model.group import Group


def test_case_1_add_rdm_contact_to_rdm_group(app, orm):
    app.group.create_if_not_exist(orm)
    app.contact.create_if_not_exist(orm)
    contacts = orm.get_contact_list()
    contact = random.choice(contacts)
    groups = orm.get_group_list()
    group = random.choice(groups)
    app.contact.add_to_group_by_id(contact.id, group.name)
    contacts_in_group = list(orm.get_contacts_in_group(group))
    assert contact in contacts_in_group


def test_case_2_del_contact_from_group(app, orm):
    app.group.create_if_not_exist(orm)
    app.contact.create_if_not_exist(orm)
    groups_with_contacts = orm.get_not_empty_groups()
    if len(groups_with_contacts) == 0:
        new_group = random.choice(orm.get_group_list())
        new_contact = random.choice(orm.get_contact_list())
        app.contact.add_to_group_by_id(new_contact.id, new_group.name)
        groups_with_contacts = orm.get_not_empty_groups()
    group = random.choice(groups_with_contacts)
    contacts = orm.get_contacts_in_group(group)
    contact = random.choice(contacts)
    app.contact.delete_from_group_by_id(contact.id, group.name)
    contacts_in_group = list(orm.get_contacts_in_group(Group(id=group.id)))
    assert contact not in contacts_in_group
