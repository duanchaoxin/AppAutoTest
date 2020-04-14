from base.base_page import BasePage
from page import login, username


class MinePage(BasePage):
    def click_login(self):
        self.base_click(self.base_find(login))

    def get_username_text(self):
        """获取用户昵称信息"""
        return self.base_find(username).text