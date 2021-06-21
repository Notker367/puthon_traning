# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from group import Group
import unittest, time, re


def login(driver, username, password):
    driver.find_element_by_name("user").clear()
    driver.find_element_by_name("user").send_keys(username)
    driver.find_element_by_name("pass").clear()
    driver.find_element_by_name("pass").send_keys(password)
    driver.find_element_by_xpath("//input[@value='Login']").click()


def open_home_page(driver):
    driver.get("http://localhost/addressbook/")


def logout_from_homepage(driver):
    driver.find_element_by_id("header").click()
    driver.find_element_by_link_text("home").click()
    driver.find_element_by_link_text("Logout").click()


class UntitledTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_untitled_test_case(self):
        driver = self.driver
        open_home_page(driver)
        login(driver, username="admin", password="secret")
        logout_from_homepage(driver)

    def is_alert_present(self):
        try:
            self.driver.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True

    def test_untitled_test_case_2(self):
        driver: object = self.driver
        open_home_page(driver)
        login(driver, username="admin", password="secret")
        logout_from_homepage(driver)

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()
