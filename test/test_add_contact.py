# -*- coding: utf-8 -*-
from model.contact import Contact
import pytest
import data.add_contact


#@pytest.mark.parametrize("contact", data.add_contact.test_data, ids=[repr(x) for x in data.add_contact.test_data])
def test_test_add_contact(app, json_contacts):
    contact = json_contacts
    old_conts = app.contact.get_contact_list()
    app.contact.add_contact(contact)
    assert len(old_conts) + 1 == app.contact.count()
    new_conts = app.contact.get_contact_list()
    old_conts.append(contact)
    assert sorted(old_conts, key=Contact.id_or_max) == sorted(new_conts, key=Contact.id_or_max)



