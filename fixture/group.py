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
        self.group_cache = None

    def fill_form_group(self, group=Group()):
        self.cache_field_value("group_name", group.name)
        self.cache_field_value("group_header", group.header)
        self.cache_field_value("group_footer", group.footer)

    def edit_first_from_home(self, group):
        driver = self.app.driver
        self.edit_by_index(0)

    def edit_by_index(self, index, group):
        driver = self.app.driver
        self.open_page_group()
        self.select_by_index(index)
        driver.find_element_by_name("edit").click()
        self.fill_form_group(group)
        driver.find_element_by_name("update").click()
        driver.find_element_by_link_text("group page").click()
        driver.find_element_by_link_text("home").click()
        self.group_cache = None

    def edit_by_id(self, id, group):
        driver = self.app.driver
        self.open_page_group()
        self.select_by_id(id=id)
        driver.find_element_by_name("edit").click()
        self.fill_form_group(group)
        driver.find_element_by_name("update").click()
        driver.find_element_by_link_text("group page").click()
        driver.find_element_by_link_text("home").click()
        self.group_cache = None

    def select_first_group(self):
        driver = self.app.driver
        self.select_by_index(0)

    def select_by_index(self, index):
        driver = self.app.driver
        driver.find_elements_by_name("selected[]")[index].click()

    def select_by_id(self, id):
        driver = self.app.driver
        driver.find_element_by_css_selector(f"input[value='{id}']").click()

    def delete_by_index(self, index):
        driver = self.app.driver
        self.open_page_group()
        self.select_by_index(index)
        driver.find_element_by_name("delete").click()
        driver.find_element_by_link_text("group page").click()
        driver.find_element_by_link_text("home").click()
        self.group_cache = None

    def delete_first_from_home(self):
        driver = self.app.driver
        self.delete_by_index(0)

    def delete_by_id(self, id):
        driver = self.app.driver
        self.open_page_group()
        self.select_by_id(id)
        driver.find_element_by_name("delete").click()
        driver.find_element_by_link_text("group page").click()
        driver.find_element_by_link_text("home").click()
        self.group_cache = None

    def open_page_group(self):
        driver = self.app.driver
        if not (driver.current_url.endswith("/group.php") and len(driver.find_elements_by_name("new")) > 0):
            driver.find_element_by_link_text("groups").click()

    def cache_field_value(self, field_name, text):
        driver = self.app.driver
        if text is not None:
            driver.find_element_by_name(field_name).click()
            driver.find_element_by_name(field_name).clear()
            driver.find_element_by_name(field_name).send_keys(text)

    def count(self):
        driver = self.app.driver
        self.open_page_group()
        return len(driver.find_elements_by_name("selected[]"))

    group_cache = None

    def get_group_list(self):
        driver = self.app.driver
        if self.group_cache is None:
            self.open_page_group()
            self.group_cache = []
            for element in driver.find_elements_by_css_selector("span.group"):
                text = element.text
                value = element.find_element_by_name("selected[]").get_attribute("value")
                self.group_cache.append(Group(name=text, id=value))
        return list(self.group_cache)

    def create_if_not_exist(self, db, group=Group(name="new_contact_for_tests")):
        driver = self.app.driver
        if len(db.get_group_list()) == 0:
            self.create_from_home(group)