from selenium.webdriver.support.wait import WebDriverWait

from utils import DriverUtil


class BasePage(object):

    def __init__(self):
        self.driver = DriverUtil.get_driver()

    def base_find(self, location, timeout=5, poll=0.5):
         return WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll). \
            until(self, lambda x: x.find_element(location[0], location[1]))

    def base_click(self,ele):
        ele.click()

    def base_input_text(self, element, text):
        # 给某个元素输入指定内容
        element.clear()
        element.send_keys(text)
