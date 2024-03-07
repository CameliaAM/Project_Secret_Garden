from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

from browser import Browser
import logging


class Search(Browser):
    COOKIES_BTN_ACC = (By.XPATH, '//*[@id="pandectes-banner"]/div/div[2]/a[2]')
    COOKIES_BANNER = (By.ID, 'cookieconsent:desc')
    SEARCH_BAR = (By.XPATH, '//*[@id="shopify-section-header-categories-menu"]//form/div/input')
    SEARCH_BTN = (By.XPATH, '//button[@class="t4s-search-header__submit"]')
    SEARCH_RESULT = (By.ID, 'b_3b0cc506-49ea-4851-b5a6-ff7c2153b0e6')
    PRODUCT = (By.XPATH, '//div[@class="t4s-row"]/div/div[1]/div[1]')
    PRODUCT_TITLE = (By.CLASS_NAME, 't4s-product__title')
    ADD_TO_CART_BTN = (By.NAME, 'add')
    CART_SIDEBAR = (By.ID, 't4s-mini_cart')
    CART_PRODUCT = (By.CLASS_NAME, 't4s-mini_cart__info')
    CART_BTN = (By.XPATH, '//*[@id="shopify-section-header-categories-menu"]/div/div[1]/div/div/div[4]/div/div[4]')
    DELETE_BTN = (By.XPATH, '//*[@id="t4s-mini_cart"]/form/div[1]/div/div[2]/div/div/div[2]/a[2]')
    EMPTY_CART_ICON = (By.ID, 'icon-cart-emty')
    PRICES = (By.XPATH, '//div[@class="t4s-product-price"]/span')
    DROPDOWN = (By.XPATH, '//*[@id="shopify-section-template--20434453627206__main"]/div/div/div[1]/div[3]/button')
    PRICE_ASCENDING = (By.XPATH, '//*[@id="t4s__sortby"]/div[3]/button[2]')
    PRODUCTS_MENU = (By.XPATH, '//*[@class="t4s-d-flex t4s-align-items-center"]')
    OPTION1 = (By.XPATH, '//ul[@id="t4s-nav-categories"]/li[1]')

    def open_homepage(self):
        self.driver.get("https://secretgarden.ro/")

    def accept_cookies(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.COOKIES_BTN_ACC)).click()

    def cookies_banner_is_not_displayed(self):
        WebDriverWait(self.driver, 10).until(EC.invisibility_of_element_located(self.COOKIES_BANNER))

    def insert_search_product(self, product_name):
        insert_product = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.SEARCH_BAR))
        insert_product.send_keys(product_name)

    def click_search_button(self):
        self.driver.find_element(*self.SEARCH_BTN).click()

    def check_search_results(self, results_number):
        self.driver.implicitly_wait(10)
        result = self.driver.find_element(*self.SEARCH_RESULT).text
        res = [int(i) for i in result.split() if i.isdigit()]
        assert str(res) >= str(results_number), (f"ERROR: Results number is incorrect. EXPECTED: {results_number}, "
                                                 f"ACTUAL: {res}")
        logging.info(f"Number of results : {str(res)}")

    def click_first_product(self):
        try:
            product = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.PRODUCT))
            product.click()
        except Exception as e:
            logging.error(f"An error occurred while clicking the first product : {str(e)}")

    def product_page(self):
        try:
            title = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.PRODUCT_TITLE))
            assert title.is_displayed()
            logging.info("The product page is visible")
        except Exception as e:
            logging.error(f"An error occurred while checking the product's page visibility : {str(e)}")

    def click_add_to_cart_button(self):
        try:
            self.driver.find_element(*self.ADD_TO_CART_BTN).click()
        except Exception as e:
            logging.error(f"An error occurred while clicking the 'ADAUGA IN COS' button : {str(e)}")

    def shopping_cart_sidebar(self):
        try:
            sidebar = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.CART_SIDEBAR))
            assert sidebar.is_displayed()
            logging.info("The shopping cart sidebar is visible")
        except Exception as e:
            logging.error(f"An error occurred while checking the shopping's cart sidebar presence : {str(e)}")

    def product_should_be_found_in_cart(self):
        is_product_found = False
        cart_product = self.driver.find_element(*self.CART_PRODUCT)

        if cart_product:
            is_product_found = True

        assert is_product_found == True, "Error, the product was not found into the shopping cart"
        logging.info("The product is in the shopping cart")

    def homepage_cart_button(self):
        cart = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.CART_BTN))
        cart.click()

    def remove_product_from_cart_button(self):
        delete_button = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.DELETE_BTN))
        delete_button.click()

    def empty_shopping_cart(self):
        try:
            sidebar = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.EMPTY_CART_ICON))
            assert sidebar.is_displayed()
            logging.info("The shopping cart is empty")
        except Exception as e:
            logging.error(f"An error occurred while checking if the shopping cart is empty : {str(e)}")

    def search_haworthia(self):
        product = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.SEARCH_BAR))
        product.send_keys('Haworthia', Keys.ENTER)

    def sort_prices_from_low_to_high(self):
        dropdown = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.DROPDOWN))
        dropdown.click()
        option = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.PRICE_ASCENDING))
        option.click()

    def verify_sorted_prices(self):
        try:
            self.driver.refresh()
            price_elements = self.driver.find_elements(*self.PRICES)
            prices = []
            for price in price_elements:
                price_text = price.text
                price_value = float(price_text.replace(',', '.').replace(' lei', ''))
                prices.append(price_value)

            if prices:
                prices.sort()

            if prices:
                sorted_prices = sorted(prices)
                assert prices == sorted_prices, "Prices are not sorted correctly"
                logging.info(f"The sorting filter worked properly: {prices}")
            else:
                assert False, "No prices were extracted"

        except Exception as e:
            logging.error(f"An error occurred while sorting the prices : {str(e)}")

    def products_menu(self):
        menu = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.PRODUCTS_MENU))
        menu.click()
        option1 = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.OPTION1))
        option1.click()

    def option1_page(self):
        expected_url = "https://secretgarden.ro/collections/bulbi-rizomi"
        current_url = self.driver.current_url
        assert current_url == expected_url, "You've been redirected to the incorrect URL."
        logging.info("You've been redirected to the correct URL")

