import yaml
from appium import webdriver
from config import BASE_DIR


class DriverUtil(object):
    driver = None

    @classmethod
    def get_driver(cls):
        if cls.driver is None:
            capabilities = {
                "platformName": "Android",  # 设备类型(Android / iOS)
                "platformVersion": "5.1.1",  # 系统版本
                "deviceName": "模拟器",  # 设备名称
                "appPackage": "com.bjcsxq.chat.carfriend",  # 待测应用的包名
                "appActivity": ".MainActivity",  # 待测应用的启动名
                # 解决中文无法输入问题
                'resetKeyboard': True,
                'unicodeKeyboard': True
            }
            cls.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities=capabilities)
        return cls.driver

    # 销毁
    @classmethod
    def quit_driver(cls):
        if cls.driver is not None:
            cls.driver.quit()
            cls.driver = None


def load_data(file_name):
    with open(BASE_DIR + "/data/{}".format(file_name), "r", encoding="utf-8") as f:
        python_data = yaml.safe_load(f)
        return python_data
