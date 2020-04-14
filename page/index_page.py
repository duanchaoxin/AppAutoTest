from base.base_page import BasePage
from page import mine


class IndexPage(BasePage):

    def click_mine(self):
        self.base_click(self.base_find(mine))
