from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage


class EmailPage(BasePage):

    remove_add =(By.XPATH, '//button[@id="close-banner"]')
    change_email = (By.XPATH, '//p[contains(. , "Change email")]')
    email_content = (By.XPATH, '(//button/p)[2]')
    refresh_button = (By.XPATH, '(//button)[10]')
    recent_email = (By.XPATH, '//div[contains(@class , "flex w-full max-w-[224px] flex-col border-b border-gray-10 py-4")]')
    verification_code = (By.XPATH, '//div[contains(text(),"Your verification code is:")]/following-sibling::div[1]')


    def __init__(self, driver):
        super().__init__(driver)

    def click_remove_add(self):
        self.click(self.remove_add)

    def click_change_email(self):
        self.click(self.change_email)

    def get_email_text(self):
        return self.get_text(self.email_content)

    def click_refresh_button(self):
        self.click(self.refresh_button)

    def open_new_window(self):
        self.open_new_tab()

    def latest_window(self):
        self.switch_latest_window()

    def switch_old_first_window(self):
        self.switch_to_fisrt_window()

    def check_recent_email(self):
        self.click(self.recent_email)

    def get_verification_code(self):
        return self.get_text(self.verification_code)

    def close_banner_if_present(self):
        try:
            self.wait.until(
                EC.element_to_be_clickable(self.remove_add)
            ).click()

            print("Banner closed")

        except TimeoutException:
            print("Banner not present")

