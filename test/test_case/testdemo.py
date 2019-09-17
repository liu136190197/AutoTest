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
    def testdemo10(self):
        '''数据库操作实例'''
        configall = ConfigAll()
        #删除账户信息：autotest
        configall.config_database("DELETE FROM sys_user WHERE user_name = '%s'" % ('autotest'))

    def testdemo22(self):
        '''接口测试实例'''
        driver = self.driver
        cookies = driver.cookie
        print(cookies)
        #get请求
        q = requests.get(
            url='http://192.168.1.1:8080/parking/cars',
            cookies=cookies
            )
        print(q.json())
        #post请求
        data1 = {"listProcurement": [
            {"ownDepartment": "50000094|50901408|50901802|50903738", "procurementAmt": 0, "businessType": "",
             "businessUnit": "BS4"}], "paidAssessList": [],
                 "payBank": {"collectionBankCity": "东莞市", "collectionBankName": "中国工商银行",
                             "collectionBankProvince": "广东省", "collectionBranch": "中国工商银行股份有限公司东莞南城支行",
                             "collectionName": "东莞市凯普建设工程有限公司", "collectionNum": "2010045009200010662",
                             "collectionBranchCode": "102602002118"}, "payInvoiceList": [],
                 "payManage": {"advance": "", "approved": "", "businessPeriod": "2019-05", "businessUnit": "BS4",
                               "orderType": "NCMS", "payMoney": 10, "currencyCode": "CNY", "payName": "",
                               "paymentEventCode": "", "paymentEvent": "", "payNum": "", "payWay": "",
                               "projectNum": "50903738", "supplierName": "东莞市凯普实业投资有限公司", "supplierNum": "7869",
                               "tax": 0, "borrowType": "", "rushAdvance": "", "invoiceCount": 0, "advanceCount": 0,
                               "assessCount": 10, "costCompanyCode": "50006294", "costCompanyName": "东莞物业（城市公司）",
                               "costDepartmentCode": "50000094|50901408|50901802|50903738",
                               "costDepartmentName": "物业发展|深圳万物云|数据与信息技术中心|研发中心", "split": "N"}, "payTypeFlag": "0101"}
        w = requests.post(url='http://192.168.1.1:8080/web/api',
                          json=data1,
                          cookies=cookies
                          )
        print(w.json())



if __name__ == "__main__":
    unittest.main()
