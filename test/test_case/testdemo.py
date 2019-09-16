import unittest
import requests
from time import sleep
from selenium.webdriver.common.by import By
from test.models.driver import Browser, logger
from test.models.myTest import MyTest
from test.page_obj.basePage import BasePage
from test.page_obj.page_Obj import Page_Obj
from selenium.webdriver.common.action_chains import ActionChains

from utils.configall import ConfigAll


class TestDemo(MyTest):
    '''本类中的方法只做示例，不在用例集中执行'''
    def testdemo0(self):
        '''数据库操作实例'''
        configall = ConfigAll()
        #删除账户信息：autotest
        configall.config_database("DELETE FROM sys_user WHERE user_name = '%s'" % ('autotest'))

    def testdemo22(self):
        '''接口测试实例'''
        driver = self.driver
        cookies = driver.cookie
        print(cookies)
        #月租车列表
        q = requests.get(
            url='http://10.39.131.201:8080/parking/cars/api/list/month?pageNo=0&pageSize=15&orderBy=&orderType=&carNo=&custName=&propertyName=&parkingSpaceCode=&remarks=&endTimeStart=&endTimeEnd=&monthTypeId=&overdue=&cuttingStatus=&isSend=&_=1565843549659',
            cookies=cookies
            )
        print(q.json())
