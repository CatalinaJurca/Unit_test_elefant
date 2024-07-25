from unittest import TestCase
from selenium.webdriver.support.select import Select

from base_data import Base_Data

class Test_Contact_Form(TestCase,Base_Data):
    def setUp(self):
        self.driver = self.setup_actions()

    def test_contact_form(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        self.driver.find_element(*self.CONTACT_BUTTON).click()
        self.driver.find_element(*self.EMAIL_CONTACT_FORM).send_keys("natalia@gmail.com")
        Select(self.driver.find_element(*self.QUERY_LIST)).select_by_visible_text("Retur")
        Select(self.driver.find_element(*self.REASON_LIST)).select_by_visible_text("Returnare produs")
        self.driver.find_element(*self.SEND_BUTTON).click()
        assert self.driver.current_url == "https://www.elefant.ro/helpdesk/contact-us"

    def tearDown(self):
        self.driver.quit()