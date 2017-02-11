from sys import maxsize


class Contact:

    def __init__(self, id = None, name=None, second_name=None, last_name=None, nickname=None, position=None, company=None, address=None, phone=None, email=None):
        self.name = name
        self.second_name = second_name
        self.last_name = last_name
        self.nickname = nickname
        self.position = position
        self.company = company
        self.address = address
        self.phone = phone
        self.email = email
        self.id = id

    def __eq__(self, other):
        return (self.id == other.id or self.id is None or other.id is None) and (self.name == other.name)

    def __repr__(self):
        return "Contact Id: %s, Name: %s, Last Name: %s" % (self.id, self.name, self.last_name)

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
