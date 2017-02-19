from random import randrange


def test_phones_on_home_page(app):
    index = randrange(app.contact.count())
    contact_from_home_page = app.contact.get_contact_list()[index]
    contact_from_edit_page = app.contact.get_info_from_edit_page(index)
    assert contact_from_home_page.name == contact_from_edit_page.name
    assert contact_from_home_page.last_name == contact_from_edit_page.last_name
    assert contact_from_home_page.address == contact_from_edit_page.address
    assert contact_from_home_page.all_phones_from_home_page == app.contact.merge_phones_like_on_home_page(
        contact_from_edit_page)
    assert contact_from_home_page.all_mails_from_home_page == app.contact.merge_mails_like_on_home_page(
        contact_from_edit_page)


