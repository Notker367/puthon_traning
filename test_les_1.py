# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from group import Group
from contact import Contact
import unittest, datetime, re, random


def next_num_test():
    x = random.randint(0, 100)
    return str(x)


contact_for_test_3 = Contact(firstname=f"test_text{next_num_test()}",
                             middlename=f"test_text{next_num_test()}",
                             lastname=f"test_text{next_num_test()}",
                             nickname=f"test_text{next_num_test()}",
                             title=f"test_text{next_num_test()}",
                             company=f"test_text{next_num_test()}",
                             address=f"test_text{next_num_test()}",
                             home=f"test_text{next_num_test()}",
                             mobile=f"test_text{next_num_test()}",
                             work=f"test_text{next_num_test()}",
                             fax=f"test_text{next_num_test()}",
                             email=f"test_text{next_num_test()}",
                             homepage=f"test_text{next_num_test()}",
                             bday=f"14",
                             bmonth=f"October",
                             byear=f"33",
                             address2=f"test_text{next_num_test()}",
                             phone2=f"test_text{next_num_test()}",
                             notes=f"test_text{next_num_test()}"
                             )


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


def add_new_group_from_home(driver, group):
    driver.find_element_by_link_text("groups").click()
    driver.find_element_by_name("new").click()
    driver.find_element_by_name("group_name").click()
    driver.find_element_by_name("group_name").clear()
    driver.find_element_by_name("group_name").send_keys(group.name)
    driver.find_element_by_name("group_header").click()
    driver.find_element_by_name("group_header").clear()
    driver.find_element_by_name("group_header").send_keys(group.header)
    driver.find_element_by_name("group_footer").click()
    driver.find_element_by_name("group_footer").clear()
    driver.find_element_by_name("group_footer").send_keys(group.footer)
    driver.find_element_by_name("submit").click()
    driver.find_element_by_link_text("group page").click()
    driver.find_element_by_link_text("home").click()


def add_new_contact_from_home(driver, contact):
    driver.find_element_by_link_text("add new").click()
    driver.find_element_by_name("theform").click()
    driver.find_element_by_name("firstname").click()
    driver.find_element_by_name("firstname").clear()
    driver.find_element_by_name("firstname").send_keys(contact.firstname)
    driver.find_element_by_name("middlename").click()
    driver.find_element_by_name("middlename").clear()
    driver.find_element_by_name("middlename").send_keys(contact.middlename)
    driver.find_element_by_name("lastname").clear()
    driver.find_element_by_name("lastname").send_keys(contact.lastname)
    driver.find_element_by_name("nickname").clear()
    driver.find_element_by_name("nickname").send_keys(contact.nickname)
    driver.find_element_by_name("title").clear()
    driver.find_element_by_name("title").send_keys(contact.title)
    driver.find_element_by_name("company").clear()
    driver.find_element_by_name("company").send_keys(contact.company)
    driver.find_element_by_name("address").clear()
    driver.find_element_by_name("address").send_keys(contact.address)
    driver.find_element_by_name("home").clear()
    driver.find_element_by_name("home").send_keys(contact.home)
    driver.find_element_by_name("mobile").clear()
    driver.find_element_by_name("mobile").send_keys(contact.mobile)
    driver.find_element_by_name("work").clear()
    driver.find_element_by_name("work").send_keys(contact.work)
    driver.find_element_by_name("fax").clear()
    driver.find_element_by_name("fax").send_keys(contact.fax)
    driver.find_element_by_name("email").clear()
    driver.find_element_by_name("email").send_keys(contact.email)
    driver.find_element_by_name("homepage").clear()
    driver.find_element_by_name("homepage").send_keys(contact.homepage)
    driver.find_element_by_name("bday").click()
    Select(driver.find_element_by_name("bday")).select_by_visible_text(contact.bday)
    driver.find_element_by_xpath("//option[@value='14']").click()
    driver.find_element_by_name("bmonth").click()
    Select(driver.find_element_by_name("bmonth")).select_by_visible_text(contact.bmonth)
    driver.find_element_by_xpath("//option[@value='October']").click()
    driver.find_element_by_name("byear").click()
    driver.find_element_by_name("byear").clear()
    driver.find_element_by_name("byear").send_keys(contact.byear)
    driver.find_element_by_name("address2").click()
    driver.find_element_by_name("address2").clear()
    driver.find_element_by_name("address2").send_keys(contact.address2)
    driver.find_element_by_name("phone2").clear()
    driver.find_element_by_name("phone2").send_keys(contact.phone2)
    driver.find_element_by_name("notes").click()
    driver.find_element_by_name("notes").clear()
    driver.find_element_by_name("notes").send_keys(contact.notes)
    driver.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
    driver.find_element_by_link_text("home").click()


class UntitledTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_case_1_login_logout(self):
        driver = self.driver
        open_home_page(driver)
        login(driver, username="admin", password="secret")
        logout_from_homepage(driver)

    def test_case_2_add_new_group(self):
        driver: object = self.driver
        open_home_page(driver)
        login(driver, username="admin", password="secret")
        add_new_group_from_home(driver, Group(name="Name_test", header="Header_test", footer="Footer_test"))
        logout_from_homepage(driver)

    def test_case_3_add_new_contact(self):
        driver: object = self.driver
        open_home_page(driver)
        login(driver, username="admin", password="secret")
        add_new_contact_from_home(driver, contact_for_test_3)
        logout_from_homepage(driver)

    def is_alert_present(self):
        try:
            self.driver.switch_to_alert()
        except NoAlertPresentException as e:
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

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()
