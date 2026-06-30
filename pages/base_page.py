from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)   ## waiting time for element

    ## element to be clickable
    def click(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def direct_click(self, locator):
        self.driver.find_element(*locator).click()

    ## click at o,o coordiante of the page
    def random_click(self):
        ActionChains(self.driver).move_by_offset(10, 10).click().perform()

    ## ENter text and clear
    def enter_text(self, locator,text):
        self.wait.until(EC.visibility_of_element_located(locator)).clear()
        self.wait.until(EC.visibility_of_element_located(locator)).send_keys(text)

    ## get text from the element
    def get_text(self,locator):
        return self.wait.until(EC.visibility_of_element_located(locator)).text

    ## hovering over the element
    def hovering(self, locator):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        ActionChains(self.driver).move_to_element(element).perform()

    def action_enter_text(self, locator, text):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        ActionChains(self.driver).move_to_element(element).click().send_keys(text).perform()

    def switch_latest_window(self):
        self.driver.switch_to.window(self.driver.window_handles[-1])

    def switch_to_fisrt_window(self):
        self.driver.switch_to.window(self.driver.window_handles[0])

    def open_new_tab(self):
        self.driver.switch_to.new_window('tab')


    def switch_frame(self, locator):
        frame = self.wait.until(EC.presence_of_element_located(locator))
        self.driver.switch_to.frame(frame)

    def switch_window(self, index):
        self.driver.switch_to.window(self.driver.window_handles[index])

    def get_elements(self, locator):
        return self.wait.until(EC.presence_of_all_elements_located(locator))

    def exit_frame(self):
        self.driver.switch_to.default_content()

    def scroll_to_element(self, locator):
        element = self.wait.until(EC.presence_of_element_located(locator))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});",element)

    def drag_canvas(self, locator, x_offset, y_offset):
        canvas = self.wait.until(EC.visibility_of_element_located(locator))
        ActionChains(self.driver).move_to_element(canvas).click_and_hold().move_by_offset(x_offset,y_offset).release().perform()

    # def click_canvas_offset(self, locator, x_offset, y_offset):
    #     canvas = self.wait.until(EC.visibility_of_element_located(locator))
    #     ActionChains(self.driver).move_to_element(canvas).move_by_offset(x_offset, y_offset).click().perform()

    def click_canvas_offset(self, locator, x_offset, y_offset):
        canvas = self.wait.until(
            EC.visibility_of_element_located(locator)
        )

        ActionChains(self.driver) \
            .move_to_element_with_offset(canvas, x_offset, y_offset) \
            .click() \
            .perform()

    def move_to_element(self, locator):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        ActionChains(self.driver).move_to_element(element).perform()

    def wait_and_click(self, locator, timeout=180):
        WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        ).click()