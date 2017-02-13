from model.contact import Contact
from random import randrange

def test_modify_contact(app):
    if app.contact.count() == 0:
        app.contact.add_contact(Contact(name="John", second_name="J", last_name="Doe", nickname="BBBB", position="AQA", company="LvivIT", address="Lviv", phone="0979247672",
                                     ))
    old_conts = app.contact.get_contact_list()
    index = randrange(len(old_conts))
    contact = Contact(name="666", second_name="555", last_name="666", nickname="uoiuui", position="AQA", company="LvivIT", address="Lviv", phone="0979247672",
                                     email="olga.kuratkina@gmail.com")
    contact.id = old_conts[index].id
    app.contact.modify_contact_by_index(contact, index)
    assert len(old_conts) == app.contact.count()
    new_conts = app.contact.get_contact_list()
    old_conts[index] = contact
    assert sorted(old_conts, key=Contact.id_or_max) == sorted(new_conts, key=Contact.id_or_max)
