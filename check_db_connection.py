import pymysql.cursors
from fixture.db import DBfixture
from fixture.orm import ORMfixture


connection = pymysql.connect(host="127.0.0.1", database="addressbook", user="root", password="")
orm_db = ORMfixture(host="127.0.0.1", name="addressbook", user="root", password="")

try:
    cursor = connection.cursor()
    cursor.execute("select group_id, group_name, group_header, group_footer from group_list")
    for row in cursor.fetchall():
        print(row)
finally:
    connection.close()

db = DBfixture("127.0.0.1", "addressbook", "root", "")
print(orm_db.get_group_list())
print(orm_db.get_contact_list())
