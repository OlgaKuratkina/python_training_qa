from sys import maxsize


class Contact:

    def __init__(self, id = None, name=None, second_name=None, last_name=None, nickname=None, position=None,
                 company=None, address=None, phone=None, email=None, phone_mobile=None, phone_work=None,
                 email_second=None, email_third=None,
                 phone_second=None, all_phones_from_home_page=None, all_mails_from_home_page=None):
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
        self.phone_mobile = phone_mobile
        self.phone_work = phone_work
        self.phone_second = phone_second
        self.all_phones_from_home_page = all_phones_from_home_page
        self.all_mails_from_home_page = all_mails_from_home_page
        self.email_second = email_second
        self.email_third = email_third

    def __eq__(self, other):
        return (self.id == other.id or self.id is None or other.id is None) and (self.name == other.name) and (self.last_name == other.last_name)

    def __repr__(self):
        return "Contact Id: %s, Name: %s, Last Name: %s" % (self.id, self.name, self.last_name)

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
