

def test_modify_contact(app):
    app.session.login("admin", "secret")
    app.contact.delete_contact()
    app.session.logout()
