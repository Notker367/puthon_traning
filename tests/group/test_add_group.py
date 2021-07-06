from model.group import Group
import pytest

test_data = [
    Group(name="asdqe", header="asdqeadd", footer="asdfasqe"),
    Group(name=" ", header=" ", footer=" ")
]


@pytest.mark.parametrize("group", test_data)
def test_case_1_add_new_group(app, group):
    old_groups = app.group.get_group_list()
    # group = Group(name="asdqe", header="asdqeadd", footer="asdfasqe", )
    app.group.create_from_home(group)
    assert len(old_groups) + 1 == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


@pytest.mark.parametrize("group", test_data)
def test_case_2_add_empty_group(app, group):
    pass
#    old_groups = app.group.get_group_list()
#    group = Group(name="", header="", footer="", )
#    app.group.create_from_home(group)
#    new_groups = app.group.get_group_list()
#    assert len(old_groups) + 1 == len(new_groups)
#    old_groups.append(group)
#    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
