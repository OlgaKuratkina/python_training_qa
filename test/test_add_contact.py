# -*- coding: utf-8 -*-
from model.contact import Contact
import pytest
import data.add_contact


#@pytest.mark.parametrize("contact", data.add_contact.test_data, ids=[repr(x) for x in data.add_contact.test_data])
def test_test_add_contact(app, db, check_ui, json_contacts):
    contact = json_contacts
    old_conts = db.get_contact_list()
    app.contact.add_contact(contact)
    new_conts = db.get_contact_list()
    old_conts.append(contact)
    assert sorted(old_conts, key=Contact.id_or_max) == sorted(new_conts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_conts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)



