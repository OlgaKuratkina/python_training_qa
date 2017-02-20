# -*- coding: utf-8 -*-
from model.contact import Contact
import pytest
import random
import string


def random_string(prefix, maxlen):
    symb = string.ascii_letters + string.digits + " "*10
    digs = string.digits + " "*3
    return clear_extra_whitespaces(prefix + "".join([random.choice(symb) for i in range(random.randrange(maxlen))]))

def random_digit(maxlen):
    digs = string.digits + " "*3
    return "".join([random.choice(digs) for i in range(random.randrange(maxlen))])


def clear_extra_whitespaces(text):
    return ' '.join(text.split())


def symbol_remove(text):
    return text.replace("~", "")


# def random_string(prefix, maxlen):
#     symb = string.ascii_letters + string.digits + " "*10
#     return prefix + "".join([random.choice(symb) for i in range(random.randrange(maxlen))])

test_data = [Contact(name="", last_name="", address="")] + [Contact(name=random_string("name", 10), phone=random_digit(11),
                                                            second_name=random_string("second_name", 15),
                                                            last_name=random_string("last_name", 15), email=random_string("email", 13),
                                                            address=random_string("address", 15)) for i in range(3)]


@pytest.mark.parametrize("contact", test_data, ids=[repr(x) for x in test_data])
def test_test_add_contact(app, contact):
    old_conts = app.contact.get_contact_list()
    app.contact.add_contact(contact)
    assert len(old_conts) + 1 == app.contact.count()
    new_conts = app.contact.get_contact_list()
    old_conts.append(contact)
    print(sorted(old_conts, key=Contact.id_or_max))
    print("---")
    print(sorted(new_conts, key=Contact.id_or_max))
    assert sorted(old_conts, key=Contact.id_or_max) == sorted(new_conts, key=Contact.id_or_max)



