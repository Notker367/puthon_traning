from model.contact import Contact
from selenium.webdriver.support.ui import Select
import random


def next_num_test():
    x = random.randint(0, 100)
    return str(x)


class ContactHelper:
    def __init__(self, app):
        self.app = app

    default_contact_for_tests = Contact(
        firstname=f"test_text{next_num_test()}",
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
        bday=f"15",
        bmonth=f"October",
        byear=f"23",
        address2=f"test_text{next_num_test()}",
        phone2=f"test_text{next_num_test()}",
        notes=f"test_text{next_num_test()}"
    )

    def fill_form_contact(self, contact=Contact()):
        driver = self.app.driver
        self.cache_field_value("firstname", contact.firstname)
        self.cache_field_value("middlename", contact.middlename)
        self.cache_field_value("lastname", contact.lastname)
        self.cache_field_value("nickname", contact.nickname)
        self.cache_field_value("title", contact.title)
        self.cache_field_value("company", contact.company)
        self.cache_field_value("address", contact.address)
        self.cache_field_value("home", contact.home)
        self.cache_field_value("mobile", contact.mobile)
        self.cache_field_value("work", contact.work)
        self.cache_field_value("fax", contact.fax)
        self.cache_field_value("email", contact.email)
        self.cache_field_value("homepage", contact.homepage)
        self.cache_field_value("bday", contact.bday)
        self.cache_field_value("bmonth", contact.bmonth)
        self.cache_field_value("byear", contact.byear)
        self.cache_field_value("address2", contact.address2)
        self.cache_field_value("phone2", contact.phone2)
        self.cache_field_value("notes", contact.notes)

    def create_from_home(self, contact=default_contact_for_tests):
        driver = self.app.driver
        self.open_addnew_page()
        self.fill_form_contact(contact)
        driver.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        driver.find_element_by_link_text("home").click()

    def open_addnew_page(self):
        driver = self.app.driver
        if not (driver.current_url.endswith("/edit.php") and len(driver.find_elements_by_name("nickname")) > 0):
            driver.find_element_by_link_text("add new").click()

    def edit_first(self, contact):
        driver = self.app.driver
        self.open_edit_first()
        self.fill_form_contact(contact)
        driver.find_element_by_name("update").click()
        driver.find_element_by_link_text("home page").click()

    def open_edit_first(self):
        driver = self.app.driver
        self.open_home_page()
        driver.find_element_by_xpath("//img[@alt='Edit']").click()

    def delete_first(self):
        driver = self.app.driver
        self.open_edit_first()
        driver.find_element_by_xpath("//input[@value='Delete']").click()

    def cache_field_value(self, field_name, text):
        driver = self.app.driver
        if text is not None:
            if field_name in ("bday", "bmonth"):
                Select(driver.find_element_by_name(field_name)).select_by_visible_text(text)
            else:
                driver.find_element_by_name(field_name).click()
                driver.find_element_by_name(field_name).clear()
                driver.find_element_by_name(field_name).send_keys(text)

    def count(self):
        driver = self.app.driver
        self.open_home_page()
        return len(driver.find_elements_by_xpath("//img[@alt='Edit']"))

    def create_if_not_exist(self, contact=Contact(firstname="new_contact_for_tests")):
        driver = self.app.driver
        if self.count() == 0:
            self.create_from_home(contact)

    def open_home_page(self):
        driver = self.app.driver
        if not (driver.current_url == "http://localhost/addressbook/" and
                len(driver.find_elements_by_name("MainForm")) > 0):
            driver.find_element_by_link_text("home").click()
