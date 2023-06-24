from selenium import webdriver
import os
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.chrome.options import Options
import Access.constant as const

class Access(webdriver.Chrome):
    def __init__(self, driver_path=r"C:\Selenium", teardown=False):
        self.driver_path = driver_path
        self.teardown = teardown
        os.environ['PATH'] += self.driver_path
        options = Options()
        options.add_experimental_option("detach", True)
        super(Access, self).__init__(options=options)
        self.implicitly_wait(15)
        self.maximize_window()

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()
        else:
            print("Browser will remain open.")

    def land_first_page(self):
        self.get(const.BASE_URL)

    def join_now(self):
        try:
            self.remove_target_blank_attribute(By.LINK_TEXT, "Join now")
            # Get the register URL
            register_url = const.Register_URL
            # Navigate to the register URL
            self.get(register_url)
            # Get the current page URL after navigating to the register URL
            current_url = self.current_url
            print("Current URL after navigating to register:", current_url)
        except WebDriverException as e:
            print(f"An error occurred: {e}")

    def back_homepage(self):
        try:
            self.find_element(By.LINK_TEXT, "Back to homepage").click()
        except WebDriverException as e:
            print(f"An error occurred: {e}")

    def input_affiliate_details(self):
        try:
            self.find_element(By.ID, 'firstname').send_keys("Marie")
            self.find_element(By.ID, 'lastname').send_keys("Kurdapya")
            self.find_element(By.ID, 'email').send_keys("marie@gmail.com")
            phone_field = self.find_element(By.ID, 'phone_3')
            self.execute_script("arguments[0].removeAttribute('onkeypress')", phone_field)
            phone_field.send_keys("905 103 5698")
            self.find_element(By.ID, 'username').send_keys("marie360")
            self.find_element(By.ID, 'password').send_keys("marie360")
            self.find_element(By.ID, 'cpassword').send_keys("marie360")
        except WebDriverException as e:
            print(f"An error occurred: {e}")

    def login(self):
        try:
            self.find_element(By.LINK_TEXT, 'Log In').click()
        except WebDriverException as e:
            print(f"An error occurred: {e}")

    def input_login_credentials(self):
        try:
            self.find_element(By.NAME, 'username').send_keys("marie360")
            self.find_element(By.NAME, 'password').send_keys("marie360")
        except WebDriverException as e:
            print(f"An error occurred: {e}")

    def submit(self):
        try:
            self.find_element(By.CSS_SELECTOR, 'input[type="submit"]').click()
        except WebDriverException as e:
            print(f"An error occurred: {e}")

    def remove_target_blank_attribute(self, by, locator):
        element = self.find_element(by, locator)
        self.execute_script("arguments[0].removeAttribute('target')", element)
        element.click()