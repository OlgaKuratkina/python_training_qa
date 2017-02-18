def test_phones_on_home_page(app):
    contact_from_home_page = app.contact.get_contact_list()[0]
    contact_from_edit_page = app.contact.get_info_from_edit_page(0)
    assert contact_from_home_page.all_phones_from_home_page == app.contact.merge_phones_like_on_home_page(contact_from_edit_page)


def test_phones_on_view_page(app):
    contact_view_page = app.contact.get_contact_body_from_view_page(0)
    contact_edit_page = app.contact.get_info_from_edit_page(0)
    assert app.contact.merge_phones_like_on_view_page(contact_edit_page) in contact_view_page
    assert "P: {}".format(contact_edit_page.phone_second) in contact_view_page




