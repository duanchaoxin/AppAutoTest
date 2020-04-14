from base.base_page import BasePage
from page import login


class MinePage(BasePage):
    def click_login(self):
        self.base_click(self.base_find(login))
