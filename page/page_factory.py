from page.index_page import IndexPage
from page.login_page import LoginPage
from page.mine_page import MinePage


class PageFactory(object):

    def index_page(self):
        return IndexPage()

    def mine_page(self):
        return MinePage()

    def login_page(self):
        return LoginPage()