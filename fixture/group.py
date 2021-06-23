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
