from model.group import Group
import random


def test_case_1_delete_some_group(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create_from_home(Group(name="new_group_for_del"))
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    app.group.delete_by_id(group.id)
    new_groups = db.get_group_list()
    assert len(old_groups) - 1 == app.group.count()
    old_groups.remove(group)
    assert old_groups == new_groups
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)