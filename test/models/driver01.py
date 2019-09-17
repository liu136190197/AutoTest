import os
from configparser import ConfigParser
from selenium.webdriver import Remote
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from utils.logger import Logger

logger = Logger(logger="Browser").logger
#浏览器驱动配置
class Browser(object):
    #dir1 = os.path.dirname(os.path.abspath('.'))  # 注意相对路径获取方法
    dir1 = os.path.dirname(os.path.dirname(__file__))
    dir1 = dir1.replace('\\', '/')
    dir = dir1.split('/test_case')[0]
    chrome_driver_path = dir + "/driver/chromedriver.exe"
    ie_driver_path = dir + "/driver/IEDriverServer.exe"
    firefox_driver_path = dir + "/driver/geckodriver.exe"

    def __init__(self):
        config = ConfigParser()
        # file_path1 = os.path.dirname(os.path.abspath('.'))
        file_path1 = os.path.dirname(os.path.dirname(__file__))
        file_path2 = file_path1.replace('\\', '/')
        file_path3 = file_path2.split('/test_case')[0]
        file_path = file_path3 + "/config/config.ini"
        config.read(file_path, encoding="utf-8")
        print(file_path)
        browser = config.get("browserType", "browserName")
        logger.info("You had select %s browser." % browser)

        if browser == "Firefox":
            self.driver = webdriver.Firefox(self.firefox_driver_path)
            logger.info("Starting firefox browser.")
        elif browser == "Chrome":
            self.driver = webdriver.Chrome(self.chrome_driver_path)
            logger.info("Starting Chrome browser.")
        elif browser == "IE":
            self.driver = webdriver.Ie(self.ie_driver_path)
            logger.info("Starting IE browser.")

        # host = '127.0.0.1:4444'
        # dc = {'browserName': 'chrome'}
        # driver = Remote(
        #     command_executor='http://'+host + '/wd/hub',
        #     desired_capabilities=dc
        # )

if __name__ == '__main__':
    dr = Browser.driver
    dr.get('http://www.baidu.com')
    dr.quit()