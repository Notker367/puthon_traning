from model.group import Group


def test_case_1_delete_first_group(app):
    if app.group.count() == 0:
        app.group.create_from_home(Group(name="new_group_for_del"))
    odl_groups = app.group.get_group_list()
    app.group.delete_first_from_home()
    assert len(odl_groups) - 1 == app.group.count()
    new_groups = app.group.get_group_list()
    odl_groups[0:1] = []
    assert odl_groups == new_groups
