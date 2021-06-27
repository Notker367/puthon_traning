from model.group import Group


class GroupHelper:
    def __init__(self, app):
        self.app = app

    default_group_for_tests = Group(
        name="Name_test",
        header="Header_test",
        footer="Footer_test"
    )

    def create_from_home(self, group=default_group_for_tests):
        driver = self.app.driver
        self.open_page_group()
        driver.find_element_by_name("new").click()
        self.fill_form_group(group)
        driver.find_element_by_name("submit").click()
        driver.find_element_by_link_text("group page").click()
        driver.find_element_by_link_text("home").click()

    def fill_form_group(self, group=Group()):
        self.cache_field_value("group_name", group.name)
        self.cache_field_value("group_header", group.header)
        self.cache_field_value("group_footer", group.footer)

    def cache_field_value(self, field_name, text):
        driver = self.app.driver
        if text is not None:
            driver.find_element_by_name(field_name).click()
            driver.find_element_by_name(field_name).clear()
            driver.find_element_by_name(field_name).send_keys(text)

    def edit_first_from_home(self, group):
        driver = self.app.driver
        self.open_page_group()
        self.select_first_group()
        driver.find_element_by_name("edit").click()
        self.fill_form_group(group)
        driver.find_element_by_name("update").click()
        driver.find_element_by_link_text("group page").click()
        driver.find_element_by_link_text("home").click()

    def select_first_group(self):
        driver = self.app.driver
        driver.find_element_by_name("selected[]").click()

    def delete_first_from_home(self):
        driver = self.app.driver
        self.open_page_group()
        self.select_first_group()
        driver.find_element_by_name("delete").click()
        driver.find_element_by_link_text("group page").click()
        driver.find_element_by_link_text("home").click()

    def open_page_group(self):
        driver = self.app.driver
        driver.find_element_by_link_text("groups").click()
