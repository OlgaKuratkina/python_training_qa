from model.contact import Contact
from model.group import Group
import random


def test_delete_contact_from_group(app, db, orm):
    if len(db.get_contact_list()) == 0:
        app.contact.add_contact(
            Contact(name="John", second_name="J", last_name="Doe", nickname="BBBB", position="AQA", company="LvivIT",
                    address="Lviv", phone="0979247672",
                    ))
    if len(db.get_group_list()) == 0:
        app.group.create_group(Group(name="test_group", header="HHH", footer="FFFF"))
    conts = db.get_contact_list()
    groups = db.get_group_list()
    contact = random.choice(conts)
    group = random.choice(groups)
    if contact in orm.get_contacts_not_in_groups(group):
        app.contact.add_contact_to_group_by_id(contact.id, group.id)  # part of precondition
    app.contact.remove_contact_from_group_by_id(contact.id, group.id)
    app.contact.waiting()
    assert contact not in orm.get_contacts_in_groups(group)
    assert contact in orm.get_contacts_not_in_groups(group)

