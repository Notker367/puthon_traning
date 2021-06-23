# -*- coding: utf-8 -*-
from group import Group
from application import Application
import unittest


class UntitledTestCase(unittest.TestCase):
    def setUp(self):
        self.app = Application

    def test_case_1_login_logout(self):
        self.app.open_home_page()
        self.app.login(username="admin", password="secret")
        self.app.logout_from_homepage()

    def test_case_2_add_new_group(self):
        self.app.open_home_page()
        self.app.login(username="admin", password="secret")
        self.app.add_new_group_from_home()
        self.app.logout_from_homepage()

    def test_case_3_add_new_contact(self):
        self.app.open_home_page()
        self.app.login(username="admin", password="secret")
        self.app.add_new_contact_from_home()
        self.app.logout_from_homepage()


    def tearDown(self):
        self.app.destroy()



if __name__ == "__main__":
    unittest.main()
