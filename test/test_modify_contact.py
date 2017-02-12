from model.contact import Contact

def test_modify_contact(app):
    if app.contact.count() == 0:
        app.contact.add_contact(Contact(name="John", second_name="J", last_name="Doe", nickname="BBBB", position="AQA", company="LvivIT", address="Lviv", phone="0979247672",
                                     ))
    old_conts = app.contact.get_contact_list()
    contact = Contact(name="MMM", second_name="ghj", last_name="llll", nickname="uoiuui", position="AQA", company="LvivIT", address="Lviv", phone="0979247672",
                                     email="olga.kuratkina@gmail.com")
    contact.id = old_conts[0].id
    app.contact.modify_contact(contact)
    assert len(old_conts) == app.contact.count()
    new_conts = app.contact.get_contact_list()
    old_conts[0] = contact
    assert sorted(old_conts, key=Contact.id_or_max) == sorted(new_conts, key=Contact.id_or_max)
