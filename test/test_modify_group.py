from model.group import Group


def test_modify_group(app):
    if app.group.count() == 0:
        app.group.create_group(Group(name="test_group", header="HHH", footer="FFFF"))
    app.group.modify_group(Group(name="lalala", header="NEW header"))