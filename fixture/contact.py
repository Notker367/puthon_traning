from model.contact import Contact
from selenium.webdriver.support.ui import Select
import random, re


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
        phone2=f"test_text{next_num_test()}",
        email=f"test_text{next_num_test()}",
        homepage=f"test_text{next_num_test()}",
        bday=f"15",
        bmonth=f"October",
        byear=f"23",
        address2=f"test_text{next_num_test()}",
        fax=f"test_text{next_num_test()}",
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
        self.cache_field_value("phone2", contact.phone2)
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
        self.contact_cache = None

    def open_addnew_page(self):
        driver = self.app.driver
        if not (driver.current_url.endswith("/edit.php") and len(driver.find_elements_by_name("nickname")) > 0):
            driver.find_element_by_link_text("add new").click()

    def edit_first(self, contact):
        driver = self.app.driver
        self.edit_by_index(0, contact)

    def edit_by_index(self, index, contact):
        driver = self.app.driver
        self.open_editor_by_index(index)
        self.fill_form_contact(contact)
        driver.find_element_by_name("update").click()
        driver.find_element_by_link_text("home page").click()
        self.contact_cache = None

    def open_editor_first(self):
        driver = self.app.driver
        self.open_editor_by_index(0)

    def open_editor_by_index(self, index):
        driver = self.app.driver
        self.open_home_page()
        driver.find_elements_by_xpath("//img[@alt='Edit']")[index].click()

    def delete_first(self):
        driver = self.app.driver
        self.delete_by_index(0)

    def delete_by_index(self, index):
        driver = self.app.driver
        self.open_editor_by_index(index)
        driver.find_element_by_xpath("//input[@value='Delete']").click()
        self.contact_cache = None

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

    contact_cache = None

    def get_contact_list(self):
        driver = self.app.driver
        if self.contact_cache is None:
            self.open_home_page()
            self.contact_cache = []
            for element in driver.find_elements_by_name("entry"):
                td = element.find_elements_by_tag_name("td")
                text2 = td[1].text
                text1 = td[2].text
                value = element.find_element_by_name("selected[]").get_attribute("value")
                all_phones = td[5].text.splitlines()
                while len(all_phones) < 4:
                    all_phones.append("")
                self.contact_cache.append(Contact(firstname=text1, lastname=text2, id=value,
                                                  home=all_phones[0], mobile=all_phones[1],
                                                  work=all_phones[2], phone2=all_phones[3]))
        return list(self.contact_cache)

    def open_view_by_index(self, index):
        driver = self.app.driver
        self.open_home_page()
        row = driver.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[6]
        cell.find_element_by_tag_name("a").click()

    def get_contact_info_from_edit_page(self, index=0):
        driver = self.app.driver
        self.open_editor_by_index(index)
        firstname = driver.find_element_by_name("firstname").get_attribute("value")
        lastname = driver.find_element_by_name("lastname").get_attribute("value")
        id = driver.find_element_by_name("id").get_attribute("value")
        home = driver.find_element_by_name("home").get_attribute("value")
        mobile = driver.find_element_by_name("mobile").get_attribute("value")
        work = driver.find_element_by_name("work").get_attribute("value")
        phone2 = driver.find_element_by_name("phone2").get_attribute("value")
        return Contact(firstname=firstname, lastname=lastname, id=id,
                       home=home, mobile=mobile, work=work, phone2=phone2)

    def get_contact_from_view_page(self, index=0):
        driver = self.app.driver
        self.open_view_by_index(index)
        text = driver.find_element_by_id("content").text
        home = re.search("H: (.*)", text).group(1)
        mobile = re.search("M: (.*)", text).group(1)
        work = re.search("W: (.*)", text).group(1)
        phone2 = re.search("P: (.*)", text).group(1)
        return Contact(home=home, mobile=mobile, work=work, phone2=phone2)
