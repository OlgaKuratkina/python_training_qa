from model.contact import Contact
import random

def test_modify_contact(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.add_contact(Contact(name="John", second_name="J", last_name="Doe", nickname="BBBB", position="AQA", company="LvivIT", address="Lviv", phone="0979247672",
                                     ))
    old_conts = db.get_contact_list()
    contact = random.choice(old_conts)
    contact.name = "New name"
    contact.last_name = "modified lastname"
    app.contact.modify_contact_by_id(contact, contact.id)
    new_conts = db.get_contact_list()
    assert sorted(old_conts, key=Contact.id_or_max) == sorted(new_conts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_conts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
