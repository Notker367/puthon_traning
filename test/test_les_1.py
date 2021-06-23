# -*- coding: utf-8 -*-
import pytest
from fixture.application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_case_1_login_logout(app):
    app.session.login(username="admin", password="secret")
    app.session.logout_from_homepage()


def test_case_2_add_new_group(app):
    app.session.login(username="admin", password="secret")
    app.add_new_group_from_home()
    app.session.logout_from_homepage()


def test_case_3_add_new_contact(app):
    app.session.login(username="admin", password="secret")
    app.add_new_contact_from_home()
    app.session.logout_from_homepage()

