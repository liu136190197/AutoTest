from test.models.driver import Browser, logger
from test.page_obj.basePage import BasePage
from test.page_obj.page_Obj import Page_Obj
import unittest
from selenium import webdriver
#from selenium.webdriver.remote import webdriver
import os

class MyTest(unittest.TestCase):
    driver = None
    @classmethod
    def setUpClass(cls):
        cls.driver = Page_Obj()
        cls.driver.user_login()
        logger.info("登陆成功，开始测试")
    def setUp(self):
        pass
    def tearDown(self):
        self.driver.open("http://192.168.1.1:8080/home")
        logger.info("测试完成，返回主页")
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit_browser()
        logger.info("测试结束，关闭浏览器")

if __name__=="__main__":
    unittest.main()