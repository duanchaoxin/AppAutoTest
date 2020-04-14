from base.base_page import BasePage
from page import user, pwd, login_btn, confirm_btn


class LoginPage(BasePage):

    def input_username(self, user_name):
        self.base_input_text(self.base_find(user), user_name)

    def input_password(self, password):
        self.base_input_text(self.base_find(pwd), password)

    def click_login(self):
        self.base_click(self.base_find(login_btn))

    def click_confirm(self):
        self.base_click(self.base_find(confirm_btn))

    def login(self, user_name, password):
        self.input_username(user_name)
        self.input_password(password)
        self.click_login()
        self.click_confirm()
