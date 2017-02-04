from model.contact import Contact

def test_modify_contact(app):
    if app.contact.count() == 0:
        app.contact.add_contact(Contact(name="John", second_name="J", last_name="Doe", nickname="BBBB", position="AQA", company="LvivIT", address="Lviv", phone="0979247672",
                                     ))
    app.contact.modify_contact(Contact(name="SOME", second_name="J", last_name="Kuratkina",  position="AQA", company="NNN", address="DNIPRo"))
