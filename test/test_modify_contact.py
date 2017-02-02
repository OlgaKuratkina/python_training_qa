from model.contact import Contact

def test_modify_contact(app):
    app.session.login("admin", "secret")
    app.contact.modify_contact(Contact(name="SOME", second_name="J", last_name="Kuratkina",  position="AQA", company="NNN", address="DNIPRo"))
    app.session.logout()
