from model.group import Group
from random import randrange
import random


def test_modify_group(app, db, check_ui):
    if app.group.count() == 0:
        app.group.create_group(Group(name="test_group", header="HHH", footer="FFFF"))
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    group.name="lalala new"
    group.header="NEW header"
    app.group.modify_group_by_id(group, group.id)
    new_groups = db.get_group_list()
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)