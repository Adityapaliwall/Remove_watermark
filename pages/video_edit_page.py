from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class VideoEditPage(BasePage):

    login_button = (By.XPATH, '//button[contains(. , "Login")]')
    iframe = (By.XPATH, '//iframe[contains(@src,"accounts.wondershare.com")]')
    create_account = (By.XPATH, '//span[contains(., "Create account")]')
    email_input = (By.XPATH, '//input[@placeholder="Email address"]')
    password_input = (By.XPATH, '//input[@placeholder="Password"]')
    log_in_final = (By.XPATH, '//button[@name="Next_Login"]')
    final_create_button = (By.XPATH, '//span[contains(., " Create Account ")]')
    verification_boxes = (By.CSS_SELECTOR, "input.code-input")
    verify_code = (By.XPATH, '//button[@class="el-button full-button distance-top-24 el-button--primary"]')



    def __init__(self, driver):
        super().__init__(driver)

    def click_login(self):
        self.click(self.login_button)

    def change_to_iframe(self):
        self.switch_frame(self.iframe)

    def click_create_account(self):
        self.click(self.create_account)

    def enter_email(self, email):
        self.enter_text(self.email_input, email)

    def enter_password(self, password):
        self.enter_text(self.password_input, password)

    def click_log_in_final(self):
        self.click(self.log_in_final)

    def click_final_create_account_button(self):
        self.click(self.final_create_button)

    def enter_verification_code(self, code):
        boxes = self.get_elements(self.verification_boxes)

        for box, digit in zip(boxes, code):
            box.send_keys(digit)

    def click_verify_code(self):
        self.click(self.verify_code)

    def exit_iframe(self):
        self.exit_frame()