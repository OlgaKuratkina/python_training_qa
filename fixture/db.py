import pymysql.cursors
from fixture.group import Group
from fixture.contact import Contact


class DBfixture():
    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = pymysql.connect(host=host, database=name, user=user, password=password)
        self.connection.autocommit(True)


    def get_group_list(self):
        l = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select group_id, group_name, group_header, group_footer from group_list")
            for row in cursor.fetchall():
                (id, name, header, footer) = row
                l.append(Group(str(id), name, header, footer))
        finally:
            cursor.close()
        return l

    def get_contact_list(self):
        l = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, firstname, lastname, address, home, mobile, work, phone2, email, email2, email3 from addressbook where deprecated='0000-00-00 00:00:00'")
            for row in cursor.fetchall():
                (id, firstname, lastname, address, phone, phone_mobile, phone_work, phone_second, email,
                 email_second, email_third) = row
                l.append(Contact(str(id), name=firstname, last_name=lastname, address=address, phone=phone,
                                 phone_mobile=phone_mobile, phone_work=phone_work, phone_second=phone_second,
                                 email=email, email_second=email_second, email_third=email_third))
        finally:
            cursor.close()
        return l

    def destroy(self):
        self.connection.close()

