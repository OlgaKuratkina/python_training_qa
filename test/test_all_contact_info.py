from fixture.contact import Contact

def test_phones_on_home_page(app, db):
    contact_from_home_page = sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
    contact_from_db = sorted(db.get_contact_list(), key=Contact.id_or_max)
    assert len(contact_from_db) == len(contact_from_home_page)
    for ind in range(len(contact_from_db)):
        assert contact_from_home_page[ind].name == contact_from_db[ind].name
        assert contact_from_home_page[ind].last_name == contact_from_db[ind].last_name
        assert contact_from_home_page[ind].address == contact_from_db[ind].address
        assert contact_from_home_page[ind].all_phones_from_home_page == app.contact.merge_phones_like_on_home_page(
        contact_from_db[ind])
        assert contact_from_home_page[ind].all_mails_from_home_page == app.contact.merge_mails_like_on_home_page(
        contact_from_db[ind])


