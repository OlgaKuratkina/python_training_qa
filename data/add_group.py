from model.group import Group
import random
import string

constant = [
    Group(name="name1", header="header1", footer="footer1"),
    Group(name="name2", header="header2", footer="footer2")
]


def random_string(prefix, maxlen):
    symb = string.ascii_letters + string.digits + " "*10
    return prefix + "".join([random.choice(symb) for i in range(random.randrange(maxlen))])

test_data = [Group(name="", header="", footer="")] + [Group(name=random_string("name", 15),
                                                            header=random_string("header", 20),
                                                            footer=random_string("footer", 20)) for i in range(2)]