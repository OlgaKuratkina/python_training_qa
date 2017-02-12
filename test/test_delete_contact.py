from model.contact import Contact
from random import randrange


def test_delete_contact(app):
    if app.contact.count() == 0:
        app.contact.add_contact(Contact(name="John", second_name="J", last_name="Doe", nickname="BBBB", position="AQA", company="LvivIT", address="Lviv", phone="0979247672",
                                     ))
    old_conts = app.contact.get_contact_list()
    index = randrange(len(old_conts))
    app.contact.delete_contact_by_index(index)
    assert len(old_conts) - 1 == app.contact.count()
    new_conts = app.contact.get_contact_list()
    old_conts[index:index+1] = []
    assert sorted(old_conts, key=Contact.id_or_max) == sorted(new_conts, key=Contact.id_or_max)
