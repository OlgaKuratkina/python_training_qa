from model.contact import Contact
import random
from model.group import Group


def test_add_contact_to_group(app, db, orm):
    if len(db.get_contact_list()) == 0:
        app.contact.add_contact(
            Contact(name="John", second_name="J", last_name="Doe", nickname="BBBB", position="AQA", company="LvivIT",
                    address="Lviv", phone="0979247672",
                    ))
    if len(db.get_group_list()) == 0:
        app.group.create_group(Group(name="test_group", header="HHH", footer="FFFF"))
    old_conts = db.get_contact_list()
    groups = db.get_group_list()
    contact = random.choice(old_conts)
    group = random.choice(groups)
    if contact in orm.get_contacts_in_groups(group):
        app.contact.remove_contact_from_group_by_id(contact.id, group.id)
    app.contact.add_contact_to_group_by_id(contact.id, group.id)
    assert contact in orm.get_contacts_in_groups(group)
    assert contact not in orm.get_contacts_not_in_groups(group)

