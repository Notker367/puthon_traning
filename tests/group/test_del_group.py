from model.group import Group
import random


def test_case_1_delete_some_group(app, db, check_ui):
    app.group.create_if_not_exist(db=db, group=Group(name="new_group_for_del"))
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    app.group.delete_by_id(group.id)
    new_groups = db.get_group_list()
    old_groups.remove(group)
    assert old_groups == new_groups
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)