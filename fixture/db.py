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
            cursor.execute("select id, firstname, lastname from addressbook where deprecated='0000-00-00 00:00:00'")
            for row in cursor.fetchall():
                (id, firstname, lastname) = row
                l.append(Contact(str(id), name=firstname, last_name=lastname))
        finally:
            cursor.close()
        return l

    def destroy(self):
        self.connection.close()

