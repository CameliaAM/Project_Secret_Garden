from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from browser import Browser
import logging
from time import sleep


class HomePage(Browser):
    ACCOUNT_BTN = (By.XPATH, '//a[contains(@href,"/account") and @class="t4s-pr"]')
    LOGIN_FORM = (By.ID, 'customer_loginlogin-sidebar')
    EMAIL = (By.XPATH, '//*[@id="CustomerEmail"]')
    PASSWORD = (By.XPATH, '//*[@id="CustomerPassword"]')
    LOGIN_BTN = (By.XPATH, '//*[@id="customer_loginlogin-sidebar"]/div[3]/button')
    ERROR_MSG = (By.CLASS_NAME, 'errors')
    DASHBOARD = (By.CLASS_NAME, 't4s-account-nav')
    FORGOT_PASW = (By.LINK_TEXT, 'Ai uitat parola?')
    FORGOT_PASW_SECTION = (By.CLASS_NAME, 'is--recover')
    FORGOT_EMAIL = (By.CSS_SELECTOR, '#RecoverEmail')
    RESET_BTN = (By.XPATH, '//div[@id="recover_login-sidebar"]//div[2]/button')
    RESET_MSG = (By.CSS_SELECTOR, 'h3.form__message.t4s_mb_10')

    def open_home_page(self):
        self.driver.get("https://secretgarden.ro/")

    def click_account_button(self):
        try:
            account_button = self.driver.find_element(*self.ACCOUNT_BTN)
            account_button.click()
        except Exception as e:
            logging.error(f"An error occurred while clicking the account button : {str(e)}")

    def login_form_presence(self):
        try:
            login_form = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.LOGIN_FORM))
            assert login_form.is_displayed()
            logging.info("The login form is visible")
        except Exception as e:
            logging.error(f"An error occurred while checking the login form visibility : {str(e)}")

    def insert_valid_email(self):
        try:
            user_email = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.EMAIL))
            user_email.send_keys("melintekamikaze@gmail.com")
        except Exception as e:
            logging.error(f"An error occurred while inserting the email : {str(e)}")

    def insert_invalid_password(self):
        try:
            invalid_password = self.driver.find_element(*self.PASSWORD)
            invalid_password.send_keys("qwerty")
        except Exception as e:
            logging.error(f"An error occurred while inserting the password : {str(e)}")

    def login_button(self):
        try:
            login_button = self.driver.find_element(*self.LOGIN_BTN)
            login_button.click()
        except Exception as e:
            logging.error(f"An error occurred while clicking the login button : {str(e)}")

    def login_failed(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.ERROR_MSG))
        try:
            eroare = self.driver.find_element(*self.ERROR_MSG).text
            eroare_mesaj = "Adresă de e-mail sau parolă incorectă."
            assert eroare_mesaj in eroare
            logging.info("Login failed")
        except Exception as e:
            logging.error(f"Expected message not found : {str(e)}")

    def insert_invalid_email(self):
        try:
            user_email = self.driver.find_element(*self.EMAIL)
            user_email.send_keys("alabalaportocala@gmail.com")
        except Exception as e:
            logging.error(f"An error occurred while inserting the email : {str(e)}")

    def insert_valid_password(self):
        try:
            invalid_password = self.driver.find_element(*self.PASSWORD)
            invalid_password.send_keys("Secretgarden1.")
        except Exception as e:
            logging.error(f"An error occurred while inserting the password : {str(e)}")

    def my_account_page(self):
        try:
            self.driver.refresh()
            self.driver.find_element(*self.ACCOUNT_BTN).click()
            dashboard = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.DASHBOARD))
            assert dashboard.is_displayed()
            logging.info("I logged in my account successfully and the dashboard menu is visible.")
        except Exception as e:
            logging.error(f"An error occurred while logging in my account : {str(e)}")

    def forgot_password_link(self):
        forgot = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.FORGOT_PASW))
        forgot.click()

    def reset_password_section(self):
        try:
            reset = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.FORGOT_PASW_SECTION))
            assert reset.is_displayed()
            logging.info("The reset password section is visible")
        except Exception as e:
            logging.error(f"An error occurred while checking the visibility of the reset password section  : {str(e)}")

    def forgot_password_email(self):
        my_email = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.FORGOT_EMAIL))
        my_email.send_keys("melintekamikaze@gmail.com")

    def reset_password_button(self):
        try:
            reset_button = self.driver.find_element(*self.RESET_BTN)
            reset_button.click()
        except Exception as e:
            logging.error(f"An error occurred while clicking the reset password button : {str(e)}")
            sleep(2)

    def reset_password_message(self):
        try:
            message = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.RESET_MSG))
            actual_message = message.text.strip()
            expected_message = "Ti-a fost trimis email cu link pentru resetarea parolei."
            assert expected_message in actual_message, "Text not found."
            logging.info(f"The reset password message was found : {actual_message}")
        except Exception as e:
            logging.error(f"An error occurred: {e}")



