# -*- coding: utf-8 -*-
import pytest
from contact import Contact
from application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

    
def test_test_add_contact(app):
    app.login("admin", "secret")
    app.add_contact(Contact(name="Olga", second_name="J", last_name="Kuratkina", nickname="BlackCat", position="AQA", company="LvivIT", address="Lviv", phone="0979247672",
                                     email="olga.kuratkina@gmail.com"))
    app.logout()

