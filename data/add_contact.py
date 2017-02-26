from model.contact import Contact
import random
import string


def random_string(prefix, maxlen):
    symb = string.ascii_letters + string.digits + " "*10
    return clear_extra_whitespaces(prefix + "".join([random.choice(symb) for i in range(random.randrange(maxlen))]))


def random_digit(maxlen):
    digs = string.digits + " "*3
    return "".join([random.choice(digs) for i in range(random.randrange(maxlen))])


def clear_extra_whitespaces(text):
    return ' '.join(text.split())


def symbol_remove(text):
    return text.replace("~", "")


test_data = [Contact(name="", last_name="", address="")] + [Contact(name=random_string("name", 10), phone=random_digit(11),
                                                            second_name=random_string("second_name", 15),
                                                            last_name=random_string("last_name", 15), email=random_string("email", 13),
                                                            address=random_string("address", 15)) for i in range(3)]

