from model.group import Group
from random import randrange


def test_case_1_delete_some_group(app):
    if app.group.count() == 0:
        app.group.create_from_home(Group(name="new_group_for_del"))
    odl_groups = app.group.get_group_list()
    index = randrange(len(odl_groups))
    app.group.delete_by_index(index)
    assert len(odl_groups) - 1 == app.group.count()
    new_groups = app.group.get_group_list()
    odl_groups[index:index + 1] = []
    assert odl_groups == new_groups
