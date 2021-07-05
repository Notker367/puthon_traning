from model.group import Group


def test_case_1_add_new_group(app):
    odl_groups = app.group.get_group_list()
    group = Group(name="asdqe", header="asdqeadd", footer="asdfasqe", )
    app.group.create_from_home(group)
    assert len(odl_groups) + 1 == app.group.count()
    new_groups = app.group.get_group_list()
    odl_groups.append(group)
    assert sorted(odl_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


def test_case_2_add_empty_group(app):
    odl_groups = app.group.get_group_list()
    group = Group(name="", header="", footer="", )
    app.group.create_from_home(group)
    new_groups = app.group.get_group_list()
    assert len(odl_groups) + 1 == len(new_groups)
    odl_groups.append(group)
    assert sorted(odl_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)