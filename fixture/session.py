class SessionHelper:

    def __init__(self, app):
        self.app = app

    def login(self, username, password):
        driver = self.app.driver
        self.app.open_home_page()
        driver.find_element_by_name("user").clear()
        driver.find_element_by_name("user").send_keys(username)
        driver.find_element_by_name("pass").clear()
        driver.find_element_by_name("pass").send_keys(password)
        driver.find_element_by_xpath("//input[@value='Login']").click()

    def logout_from_homepage(self):
        driver = self.app.driver
        driver.find_element_by_id("header").click()
        driver.find_element_by_link_text("home").click()
        driver.find_element_by_link_text("Logout").click()
