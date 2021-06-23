# -*- coding: utf-8 -*-
import pytest
from application import Application


@pytest.fixture
def app(request):
    fixture = Application
    request.addfinalizer(fixture.destroy)
    return fixture


def test_case_1_login_logout(app):
    app.open_home_page()
    app.login(username="admin", password="secret")
    app.logout_from_homepage()


def test_case_2_add_new_group(app):
    app.open_home_page()
    app.login(username="admin", password="secret")
    app.add_new_group_from_home()
    app.logout_from_homepage()


def test_case_3_add_new_contact(app):
    app.open_home_page()
    app.login(username="admin", password="secret")
    app.add_new_contact_from_home()
    app.logout_from_homepage()

