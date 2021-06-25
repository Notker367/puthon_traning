

def test_case_1_login_logout(app):
    app.session.login(username="admin", password="secret")
    app.session.logout_from_homepage()
