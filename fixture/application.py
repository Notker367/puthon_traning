from selenium import webdriver
from fixture.session import SessionHelper
from fixture.group import GroupHelper
from fixture.contact import ContactHelper


class Application:

    def __init__(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(1)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)

    def is_valid(self):
        try:
            self.driver.current_url
            return True
        except:
            return False

    def open_login_page(self):
        driver = self.driver
        if not len(driver.find_elements_by_name("LoginForm")) > 0:
            driver.get("http://localhost/addressbook/")

    def destroy(self):
        self.driver.quit()
