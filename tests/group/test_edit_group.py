from model.group import Group
import random


def test_case_1_edit_rdm_group(app, db, check_ui):
    app.group.create_if_not_exist(db=db, group=Group(name="new_group_for_edit"))
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    index = old_groups.index(group)
    new_group = Group(name="New_name")
    group.id = old_groups[index].id
    app.group.edit_by_id(id=group.id, group=new_group)
    new_groups = db.get_group_list()
    old_groups[index] = new_group
    assert old_groups == new_groups
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)

# def test_case_2_edit_footer_first_group(app):
#    if app.group.count() == 0:
#        app.group.create_from_home(Group(name="new_group_for_edit"))
#    old_groups = app.group.get_group_list()
#    app.group.edit_first_from_home(group=Group(footer="New_footer"))
#    new_groups = app.group.get_group_list()
#    assert len(old_groups) == len(new_groups)
#
