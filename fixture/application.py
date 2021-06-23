from selenium import webdriver
from selenium.webdriver.support.ui import Select
from model.group import Group
from model.contact import Contact
import random


def next_num_test():
    x = random.randint(0, 100)
    return str(x)


class Application:

    def __init__(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)

    default_group_for_tests = Group(
        name="Name_test",
        header="Header_test",
        footer="Footer_test"
    )

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

    def login(self, username, password):
        driver = self.driver
        driver.find_element_by_name("user").clear()
        driver.find_element_by_name("user").send_keys(username)
        driver.find_element_by_name("pass").clear()
        driver.find_element_by_name("pass").send_keys(password)
        driver.find_element_by_xpath("//input[@value='Login']").click()

    def open_home_page(self):
        driver = self.driver
        driver.get("http://localhost/addressbook/")

    def logout_from_homepage(self):
        driver = self.driver
        driver.find_element_by_id("header").click()
        driver.find_element_by_link_text("home").click()
        driver.find_element_by_link_text("Logout").click()

    def add_new_group_from_home(self, group=default_group_for_tests):
        driver = self.driver
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

    def add_new_contact_from_home(self, contact=default_contact_for_tests):
        driver = self.driver
        driver.find_element_by_link_text("add new").click()
        driver.find_element_by_name("theform").click()
        driver.find_element_by_name("firstname").clear()
        driver.find_element_by_name("firstname").send_keys(contact.firstname)
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
        Select(driver.find_element_by_name("bday")).select_by_visible_text(contact.bday)
        Select(driver.find_element_by_name("bmonth")).select_by_visible_text(contact.bmonth)
        driver.find_element_by_name("byear").clear()
        driver.find_element_by_name("byear").send_keys(contact.byear)
        driver.find_element_by_name("address2").clear()
        driver.find_element_by_name("address2").send_keys(contact.address2)
        driver.find_element_by_name("phone2").clear()
        driver.find_element_by_name("phone2").send_keys(contact.phone2)
        driver.find_element_by_name("notes").clear()
        driver.find_element_by_name("notes").send_keys(contact.notes)
        driver.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        driver.find_element_by_link_text("home").click()

    def destroy(self):
        self.driver.quit()
