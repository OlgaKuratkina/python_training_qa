from model.group import Group


def test_modify_group(app):
    if app.group.count() == 0:
        app.group.create_group(Group(name="test_group", header="HHH", footer="FFFF"))
    old_groups = app.group.get_group_list()
    group = Group(name="lalala", header="NEW header")
    group.id = old_groups[0].id
    app.group.modify_group(group)
    assert len(old_groups) == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups[0] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)