from model.group import Group


def test_case_1_edit_name_first_group(app):
    if app.group.count() == 0:
        app.group.create_from_home(Group(name="new_group_for_edit"))
    odl_groups = app.group.get_group_list()
    group = Group(name="New_name")
    group.id = odl_groups[0].id
    app.group.edit_first_from_home(group)
    new_groups = app.group.get_group_list()
    assert len(odl_groups) == len(new_groups)
    odl_groups[0] = group
    assert sorted(odl_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

# def test_case_2_edit_footer_first_group(app):
#    if app.group.count() == 0:
#        app.group.create_from_home(Group(name="new_group_for_edit"))
#    odl_groups = app.group.get_group_list()
#    app.group.edit_first_from_home(group=Group(footer="New_footer"))
#    new_groups = app.group.get_group_list()
#    assert len(odl_groups) == len(new_groups)
#
