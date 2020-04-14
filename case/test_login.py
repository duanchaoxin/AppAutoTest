"""
搜索测试用例
"""
import os, sys
import time

sys.path.append(os.getcwd())
import pytest
from page.page_factory import PageFactory
from utils import DriverUtil


class TestLogin(object):
    """搜索测试类"""

    @pytest.fixture(autouse=True)
    def before_func(self):
        DriverUtil.get_driver()  # 获取驱动对象
        self.factory = PageFactory()

        yield  # 结束操作
        time.sleep(3)
        DriverUtil.quit_driver()  # 退出驱动对象

    def test_login(self):
        self.factory.index_page().click_mine()
        self.factory.mine_page().click_login()
        self.factory.login_page().login('13157523435', 'lm123456')
        self.factory.login_page().click_confirm()
        # 断言
        username_text = self.factory.mine_page().get_username_text()
        assert '3435' in username_text

        # self.factory.index_page().click_mine()
        # self.factory.mine_page().click_login()
        # self.factory.login_page().login('13157523435', 'lm123456')
        # username_text = self.factory.login_page().get_toast('账号还未注册')
        # assert '账号还未注册' in username_text