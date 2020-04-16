from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from utils import DriverUtil


class BasePage(object):

    def __init__(self):
        self.driver = DriverUtil.get_driver()

    def base_find(self, location, timeout=5, poll=.3):
        return WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll). \
            until(lambda x: x.find_element(location[0], location[1]))

    def base_click(self, ele):
        ele.click()

    def base_input_text(self, element, text):
        # 给某个元素输入指定内容
        element.clear()
        element.send_keys(text)

    def get_toast(self, text):
        xpath = By.XPATH, '//*[contains(@text, "{}")]'.format(text)
        # xpath = By.XPATH, '//*contains[@text,"{}"]'.format(text)
        return self.base_find(xpath,).text
