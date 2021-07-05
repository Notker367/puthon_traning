from model.group import Group
from random import randrange


def test_case_1_edit_name_first_group(app):
    if app.group.count() == 0:
        app.group.create_from_home(Group(name="new_group_for_edit"))
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    group = Group(name="New_name")
    group.id = old_groups[index].id
    app.group.edit_by_index(index, group)
    assert len(old_groups) == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

# def test_case_2_edit_footer_first_group(app):
#    if app.group.count() == 0:
#        app.group.create_from_home(Group(name="new_group_for_edit"))
#    old_groups = app.group.get_group_list()
#    app.group.edit_first_from_home(group=Group(footer="New_footer"))
#    new_groups = app.group.get_group_list()
#    assert len(old_groups) == len(new_groups)
#
