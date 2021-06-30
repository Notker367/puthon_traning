from model.group import Group


def test_case_1_edit_name_first_group(app):
    if app.group.count() == 0:
        app.group.create_from_home(Group(name="new_group_for_edit"))
    app.group.edit_first_from_home(group=Group(name="New_name"))


def test_case_2_edit_footer_first_group(app):
    if app.group.count() == 0:
        app.group.create_from_home(Group(name="new_group_for_edit"))
    app.group.edit_first_from_home(group=Group(footer="New_footer"))
