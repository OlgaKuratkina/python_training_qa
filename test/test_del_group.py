from model.group import Group


def test_del_group(app):
    if app.group.count() == 0:
        app.group.create_group(Group(name="test_group", header="HHH", footer="FFFF"))
    app.group.delete_first_group()