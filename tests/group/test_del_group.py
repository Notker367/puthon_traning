from model.group import Group


def test_case_1_delete_first_group(app):
    if app.group.count() == 0:
        app.group.create_from_home(Group(name="new_group_for_del"))
    app.group.delete_first_from_home()
