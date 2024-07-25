from selenium.webdriver.common.by import By
from seleniumbase import Driver

class Base_Data():
    INPUT_SEARCH_BOX = (By.XPATH, '//input[@type="text"]')
    DISCOUNT_BUTTON_15_30 = (By.XPATH, '//a[@data-testing-id="filter-link-[15.0 TO 30.0]"]')
    PRODUCT_NEW_PRICE=(By.XPATH,'//div[@class="price-container product-price vendor-offer-data"]//div[@data-price-currencymnemonic="RON"]')
    PRODUCT_OLD_PRICE=(By.XPATH, '//div[@class="was-price old-price"]')
    INPUT_SEARCH_BOX_2 = (By.XPATH,'//div[@class="col-md-7 col-lg-8 search-container header-search-container hidden-xs hidden-sm"]//input[@class="form-control searchTerm js-has-overlay"]')
    SEARCH_DROPDOWN=(By.ID, "SortingAttribute")
    PRODUCT_PRICE=(By.XPATH,'//div[@class="price-container product-price vendor-offer-data"]//div[@data-price-currencymnemonic="RON"]')
    CONTACT_BUTTON=(By.LINK_TEXT, "Contact")
    EMAIL_CONTACT_FORM=(By.NAME, "email")
    QUERY_LIST=(By.NAME, "selected_category")
    REASON_LIST=(By.NAME, "selected_reason")
    SEND_BUTTON= (By.CLASS_NAME, "o-btn-send")

    def setup_actions(self):
        self.driver = Driver(browser="edge")
        self.driver.get("https://www.elefant.ro/")
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)
        self.driver.find_element(By.ID, "CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll").click()
        return self.driver