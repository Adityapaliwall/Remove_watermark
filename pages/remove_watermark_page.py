from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import BasePage


class RemoveWatermarkPage(BasePage):

    plan_ad_remove = (By.XPATH, '//span[@class="xmi-icon cursor-pointer text-[#ffffff8f] max-md:mt-[12px] max-md:mr-2 max-md:mb-6"]')
    basic_model = (By.XPATH, '(//div[. = "Basic Model "])[1]')
    upload = (By.XPATH, "//input[@type='file']")
    upload_box = (By.XPATH, '//span[contains(.,"Drag File Here or Click To Upload")]')
    hand_sign = (By.XPATH,'//span[contains(@class,"hand-hover") or contains(@class,"hand-active-hover")]')
    zoom_plus_sign = (By.XPATH, '(//div[contains(@class, "hover-zoom-rate-btn hover-zoom")])[2]')
    canvas = (By.CSS_SELECTOR, "canvas.upper-canvas")
    generate_button = (By.XPATH, '//button[contains(@class, "xmi-button xmi-button--primary ")]')
    download_button = (By.XPATH, "//span[contains(@class,'action-btn-icon')]")
    edit_button = (By.XPATH, '//button[. = "Edit"]')
    video_eraser = (By.XPATH, '//div[.="Video Eraser"]')

    def __init__(self, driver):
        super().__init__(driver)

    def remove_plan_ads(self):
        self.click(self.plan_ad_remove)

    def select_model_for_watermark(self):
        self.click(self.basic_model)

    def scroll_to_upload(self):
        self.scroll_to_element(self.upload_box)

    def upload_video(self, path):
        self.driver.find_element(*self.upload).send_keys(path)

    # def click_hand_sign(self):
    #     self.click(self.hand_sign)

    def click_hand_sign(self):
        element = self.wait.until(EC.visibility_of_element_located(self.hand_sign))
        ActionChains(self.driver).move_to_element(element).click().perform()

    def click_zoom_button(self):
        self.click(self.zoom_plus_sign)

    def drag_image_upward(self):
        self.drag_canvas(self.canvas, 0, -150)

    def click_first_point(self):
        self.click_canvas_offset(self.canvas, 134, 135)

    def click_second_point(self):
        self.click_canvas_offset(self.canvas, 131, 130)

    def click_generate_button(self):
        self.click(self.generate_button)

    def click_download_button(self):
        button = WebDriverWait(self.driver, 180).until(
            EC.element_to_be_clickable(self.download_button)
        )

        print("Button Enabled :", button.is_enabled())
        print("Button Display :", button.is_displayed())

        try:
            button.click()
            print("Normal click executed")
        except:
            self.driver.execute_script("arguments[0].click();", button)
            print("JavaScript click executed")

    def scroll_to_edit(self):
        self.scroll_to_element(self.edit_button)

    def wait_for_video_eraser(self):
        WebDriverWait(self.driver, 300).until(
            EC.visibility_of_element_located(self.video_eraser)
        )

        print("Video Eraser appeared.")
