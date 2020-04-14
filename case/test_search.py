"""
搜索测试用例
"""
import os, sys
sys.path.append(os.getcwd())
import allure
import time
import pytest

from utils import DriverUtil, load_data


class TestSearch(object):
    """搜索测试类"""

    @pytest.fixture(autouse=True)
    def before_func(self):
        self.driver = DriverUtil.get_driver()  # 获取驱动对象
        from page.page_factory import PageFactory
        self.factory = PageFactory()

        yield  # 结束操作
        time.sleep(3)
        DriverUtil.quit_driver()  # 退出驱动对象

    @allure.MASTER_HELPER.severity(allure.MASTER_HELPER.severity_level.CRITICAL)
    @allure.MASTER_HELPER.step(title="测试步骤1")
    @pytest.mark.parametrize('text', load_data('test_search_data.yaml'))
    def test_func(self, text):
        allure.MASTER_HELPER.attach("搜索","1.进入搜索页 2.输入搜索内容")
        """搜索测试方法"""
        # 点击搜索按钮跳转搜索页面
        self.factory.index_page().go_to_search()
        # 输入内容搜索结果
        self.factory.search_page().search(text)
