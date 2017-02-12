from model.group import Group
from random import randrange


def test_modify_group(app):
    if app.group.count() == 0:
        app.group.create_group(Group(name="test_group", header="HHH", footer="FFFF"))
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    group = Group(name="lalala", header="NEW header")
    group.id = old_groups[index].id
    app.group.modify_group_by_index(group, index)
    assert len(old_groups) == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)