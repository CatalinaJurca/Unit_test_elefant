from unittest import TestCase
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from base_data import Base_Data

class Test_Search(TestCase,Base_Data):
    def setUp(self):
        self.driver = self.setup_actions()

# - Test 2: Cautati "iphone", faceti filtrare dupa discount si verificati faptul ca toate produsele returnate au pretul in intervalul de filtrare
    def test_search_by_discount(self):
        input_box = self.driver.find_element(*self.INPUT_SEARCH_BOX)
        input_box.send_keys("iphone")
        input_box.send_keys(Keys.ENTER)
        self.driver.find_element(*self.DISCOUNT_BUTTON_15_30).click()

        price_list_new_price = self.driver.find_elements(*self.PRODUCT_NEW_PRICE)
        price_list_old_price = self.driver.find_elements(*self.PRODUCT_OLD_PRICE)

        for i in range(len(price_list_new_price)):
            current_item_price_new = price_list_new_price[i].text.replace(" lei", "").replace(",", ".")
            current_item_price_old = price_list_old_price[i].text.replace(" lei", "").replace(",", ".")
            discount_net = 100 - ((float(current_item_price_new) / float(current_item_price_old)) * 100)
            if 15 < discount_net < 30:
                print(f"Discount is {discount_net:.2f}%")
            else:
                print("Filter error")

    # - Test 3: Cautati un produs care nu exista si verifica faptul ca mesajul returnat este: "NE PARE RĂU, NU EXISTĂ PRODUSE ÎN ACEASTĂ CATEGORIE."

    def test_search_unexisting_product(self):
        input_box=self.driver.find_element(*self.INPUT_SEARCH_BOX_2)
        input_box.send_keys("lenovo")
        input_box.send_keys(Keys.ENTER)
        search_message = self.driver.find_element(By.CLASS_NAME, "no-search-result").text
        expected_message = ('NU A FOST GĂSIT NICI UN REZULTAT :\nCăutarea ta pentru "lenovo" returnat 0 rezultate.')
        assert search_message == expected_message, f'error: actual message: {search_message} , expected message : {expected_message} '

    def test_search_sort_ascending_by_price(self):
        input_box = self.driver.find_element(*self.INPUT_SEARCH_BOX_2)
        input_box.send_keys("samsung")
        input_box.send_keys(Keys.ENTER)
        sort_dropdown = Select(self.driver.find_element(*self.SEARCH_DROPDOWN))
        sort_dropdown.select_by_visible_text('Pret crescator')
        price_list= self.driver.find_elements(*self.PRODUCT_PRICE)
        price_values = [float(price.text.replace(" lei", "").replace(",", ".")) for price in price_list]
        is_price_list_sorted = True
        for i in range(len(price_list) - 1):
            if price_values[i] > price_values[i + 1]:
                is_price_list_sorted = False
        self.assertTrue(is_price_list_sorted, "Error, the price list is not sorted in ascending order")

    def test_search_sort_descending_by_price(self):
        input_box = self.driver.find_element(*self.INPUT_SEARCH_BOX_2)
        input_box.send_keys("samsung")
        input_box.send_keys(Keys.ENTER)
        sort_dropdown = Select(self.driver.find_element(*self.SEARCH_DROPDOWN))
        sort_dropdown.select_by_visible_text('Pret descrescator')
        price_list = self.driver.find_elements(*self.PRODUCT_PRICE)
        price_values = [float(price.text.replace(" lei", "").replace(",", ".")) for price in price_list]
        print("Extracted price values:", price_values)  # [115.99, 51.1, 42.55, 42.58, 16.99, 15.99, 9.99, 9.99, 8.99]

        is_price_list_sorted = True
        for i in range(len(price_values) - 1):
            if price_values[i] < price_values[i + 1]:
                is_price_list_sorted = False
                break
        self.assertTrue(is_price_list_sorted, "Error, the price list is not sorted in descending order")
        # print("Is price list sorted in descending order?", is_price_list_sorted)

    def tearDown(self):
        self.driver.quit()
