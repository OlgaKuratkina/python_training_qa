from model.contact import Contact
import random
import string
import os.path
import jsonpickle
import getopt
import sys


try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/contacts.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


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

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)
with open(file, "w") as ff:
    jsonpickle.set_encoder_options("json", indent=2)
    ff.write(jsonpickle.encode(test_data))
