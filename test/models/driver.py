from selenium import webdriver
from utils.logger import Logger

logger = Logger(logger="Browser").logger
#浏览器驱动配置
class Browser(object):
    def __init__(self):
        self.driver =webdriver.Chrome()
        logger.info("Starting browser:%s" %self.driver)

if __name__ == '__main__':
    dr1 = Browser()
    dr = dr1.driver
    dr.get('http://www.baidu.com')
    dr.quit()


