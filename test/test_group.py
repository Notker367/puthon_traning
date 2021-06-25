# -*- coding: utf-8 -*-
import pytest
from fixture.application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_case_1_add_new_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create_from_home()
    app.session.logout_from_homepage()
