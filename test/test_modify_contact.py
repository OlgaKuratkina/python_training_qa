from model.contact import Contact

def test_modify_contact(app):
    app.session.login("admin", "secret")
    app.contact.modify_contact(Contact(name="Olga", second_name="J", last_name="Kuratkina", nickname="BlackCat", position="AQA", company="LvivIT", address="Lviv", phone="0979247672",
                                     email="olga.kuratkina@gmail.com"))
    app.session.logout()
