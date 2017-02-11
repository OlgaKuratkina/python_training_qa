# -*- coding: utf-8 -*-
from model.contact import Contact


def test_test_add_contact(app):
    old_conts = app.contact.get_contact_list()
    contact = Contact(name="Olga", second_name="J", last_name="Kuratkina", nickname="BlackCat", position="AQA", company="LvivIT", address="Lviv", phone="0979247672",
                                     email="olga.kuratkina@gmail.com")
    app.contact.add_contact(contact)
    new_conts = app.contact.get_contact_list()
    assert len(old_conts) + 1 == len(new_conts)
    old_conts.append(contact)
    assert sorted(old_conts, key=Contact.id_or_max) == sorted(new_conts, key=Contact.id_or_max)


