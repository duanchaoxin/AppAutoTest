"""
搜索测试用例
"""
import os, sys

from page.page_factory import PageFactory

sys.path.append(os.getcwd())
import allure
import time
import pytest

from utils import DriverUtil, load_data


class TestLogin(object):
    """搜索测试类"""

    @pytest.fixture(autouse=True)
    def before_func(self):
        self.driver = DriverUtil.get_driver()  # 获取驱动对象
        self.factory = PageFactory()

        yield  # 结束操作
        time.sleep(3)
        DriverUtil.quit_driver()  # 退出驱动对象

    @allure.MASTER_HELPER.severity(allure.MASTER_HELPER.severity_level.CRITICAL)
    @allure.MASTER_HELPER.step(title="测试步骤1")
    @pytest.mark.parametrize('text', load_data('test_search_data.yaml'))
    def test_login(self, text):
        allure.MASTER_HELPER.attach("登录","1.进入我的 2.点击登录页入口 3.输入登录")
        self.factory.index_page().click_mine()
        self.factory.mine_page().click_login()
        self.factory.login_page().login('13157523435','lm123456')
