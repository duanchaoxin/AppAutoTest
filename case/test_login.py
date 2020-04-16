"""
搜索测试用例
"""
import os, sys
sys.path.append(os.getcwd())
import time
import allure
import pytest
from page.page_factory import PageFactory
from utils import DriverUtil, jietu


class TestLogin(object):
    """搜索测试类"""

    @pytest.fixture(autouse=True)
    def before_func(self):
         # 获取驱动对象
        self.factory = PageFactory()

        yield  # 结束操作
        time.sleep(3)
        DriverUtil.quit_driver()  # 退出驱动对象

    def test_login(self):
        # self.factory.index_page().click_mine()
        # self.factory.mine_page().click_login()
        # self.factory.login_page().login('13157523435', 'lm123456')
        # self.factory.login_page().click_confirm()
        # # 断言
        # username_text = self.factory.mine_page().get_username_text()
        # assert '3435' in username_text

        self.factory.index_page().click_mine()
        self.factory.mine_page().click_login()
        self.factory.login_page().login('13800001111', 'lm123456')
        try:
            text = self.factory.login_page().get_toast('账号还未注册')
            assert "账号还未注册" in text
        except AssertionError as e:
            with open(jietu(), 'rb') as f:
                # allure.MASTER_HELPER.attach('文件名称', 文件内容, 文件类型)
                allure.MASTER_HELPER.attach('my_info', f.read(), allure.MASTER_HELPER.attach_type.PNG)
            raise e  # 当截图操作完成后, 应该还原测试用例的真实结果, 因此需要再主动抛出异常
