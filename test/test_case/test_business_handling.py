import unittest
import requests
from time import sleep
from selenium.webdriver.common.by import By
from test.models.driver import Browser, logger
from test.models.myTest import MyTest
from test.page_obj.basePage import BasePage
from test.page_obj.page_Obj import Page_Obj
from selenium.webdriver.common.action_chains import ActionChains

class Test_1(MyTest):

    def test_case01(self):
        '''添加月租车'''
        driver = self.driver
        driver.open_menu('业务管理', '业务办理')
        driver.click(By.XPATH, "//span[contains(text(),'月租车辆管理')]")
        driver.click(By.CSS_SELECTOR, "span#monthAdd.btn.addnew")
        driver.switch_to_frame("openDialogTarget")
        driver.find_element(By.XPATH, "//*[@id='carNo']")
        driver.execute_script("document.getElementById('carNo').value = '粤Z12314'")
        driver.click(By.XPATH, "//*[@id='addCust']")
        driver.switch_to_frame("openDialogTarget")
        driver.click(By.XPATH, "//*[@id='listTabBody']/tr[4]/td[1]/input")
        driver.click(By.XPATH, "//*[@id='listTabCustomer']/span")
        driver.click(By.XPATH, "//*[@id='okBtn']")
        driver.switch_to().parent_frame()
        # driver.switch_to.default_content()  返回主页面
        driver.send_keys(By.XPATH, "//*[@id='invoice']", text="111")
        driver.click(By.XPATH, "//*[@id='submitBtn']")
        driver.click(By.XPATH, "//*[@id='sure']")
        driver.send_keys(By.XPATH, "//input[@placeholder = '车牌号码']", text='粤Z12314')
        driver.click(By.XPATH, "//span/span[@name = 'queryBtn']")
        a = driver.find_element(By.XPATH, "//*[@id='listTabBody']//a[text()='粤Z12314']")
        self.assertTrue(a, '添加月租车辆失败')

    def test_case02(self):
        '''查询月租车'''
        driver = self.driver
        driver.open_menu('业务管理', '业务办理')
        driver.click(By.XPATH, "//span[contains(text(),'月租车辆管理')]")
        clientName = driver.gettext(By.XPATH, "//*[@id='listTabBody']/tr[1]/td[1]/a")
        address = driver.gettext(By.XPATH, "//*[@id='listTabBody']/tr[1]/td[2]/a")
        carNo = driver.gettext(By.XPATH, "//*[@id='listTabBody']/tr[1]/td[3]/a")
        endTime = driver.gettext(By.XPATH, "//*[@id='listTabBody']/tr[1]/td[5]")
        endDeta = endTime.split(" ")[0]
        monthlyType = driver.gettext(By.XPATH, "//*[@id='listTabBody']/tr[1]/td[6]")
        driver.send_keys(By.XPATH, "//input[@placeholder = '车牌号码']", text=carNo)
        driver.send_keys(By.XPATH, "//input[@placeholder = '客户姓名']", text=clientName)
        driver.send_keys(By.XPATH, "//input[@placeholder = '房屋地址']", text=address)
        driver.send_keys(By.XPATH, "//input[@placeholder = '到期开始时间']", text=endDeta)
        xpath1 = "// *[ @ id = 'searchSpan'] // select[ @ name = 'monthTypeId'] / option[text() = '" + monthlyType + "']"
        # print(xpath1)
        driver.click(By.XPATH, xpath1)
        driver.click(By.XPATH, "//span/span[@name = 'queryBtn']")
        a = driver.find_element(By.XPATH, "//*[@id='listTabBody']//a[text()='%s']" % carNo)
        self.assertTrue(a, '查询月租车辆失败')

    def test_case03(self):
        '''编辑月租车'''
        driver = self.driver
        driver.open_menu('业务管理', '业务办理')
        driver.click(By.XPATH, "//span[contains(text(),'月租车辆管理')]")
        driver.click(By.XPATH, "//*[@id='listTabBody']/tr[1]//a[text()='编辑']")
        driver.switch_to_frame("openDialogTarget")
        driver.clear(By.XPATH, "//*[@name='remarks']")
        driver.send_keys(By.XPATH, "//*[@name='remarks']", text="ceshi111")
        driver.click(By.XPATH, "//*[@id='submitBtn']")
        driver.click(By.XPATH, "//*[@id='sure']")
        driver.click(By.XPATH, "//*[@id='listTabBody']/tr[1]//a[text()='编辑']")
        driver.switch_to_frame("openDialogTarget")
        a = driver.gettext(By.XPATH, "//*[@name='remarks']")
        self.assertEqual(a, 'ceshi111')

    def test_case04(self):
        '''删除月租车'''
        driver = self.driver
        driver.open_menu('业务管理', '业务办理')
        driver.click(By.XPATH, "//span[contains(text(),'月租车辆管理')]")
        driver.send_keys(By.XPATH, "//input[@placeholder = '车牌号码']", text='粤Z12314')
        driver.click(By.XPATH, "//span/span[@name = 'queryBtn']")
        driver.click(By.XPATH, "//*[@id='listTabBody']/tr[1]//a[text()='删除']")
        driver.click(By.XPATH, "//*[@id='sure']")
        driver.send_keys(By.XPATH, "//input[@placeholder = '车牌号码']", text='粤Z12314')
        driver.click(By.XPATH, "//span/span[@name = 'queryBtn']")
        a = driver.find_element(By.XPATH, "//*[@id='listTabBody']/tr/td[text()='无记录']")
        self.assertTrue(a, '删除月租车辆失败')

    def test_case05(self):
        '''添加预约车'''
        driver = self.driver
        driver.open_menu('业务管理', '业务办理')
        driver.click(By.XPATH, "//span[contains(text(),'预约车辆管理')]")
        driver.click(By.CSS_SELECTOR, "span#reserveAdd.btn.addnew")
        driver.switch_to_frame("openDialogTarget")
        driver.find_element(By.XPATH, "//*[@id='carNo']")
        driver.execute_script("document.getElementById('carNo').value = '粤Z12315'")
        driver.send_keys(By.XPATH, "//input[@name = 'visitor' and @placeholder = '访客姓名']", text="autotest")
        driver.send_keys(By.XPATH, "//input[@name = 'mainMobile' and @placeholder = '手机号码']", text="13666666666")
        driver.click(By.XPATH, "//*[@id='addCust']")
        driver.switch_to_frame("openDialogTarget")
        driver.click(By.XPATH, "//*[@id='vistorContent']/div[2]//span[1]")
        driver.click(By.XPATH, "//*[@id='vistorContent']/div[2]//span[1]")
        driver.click(By.XPATH, "//*[@id='vistorContent']/div[2]//span[1]")
        driver.click(By.XPATH, "//*[@id='vistorContent']/div[2]//span[1]")
        driver.click(By.XPATH, "//*[@id='vistorContent']/div[2]//span[1]")
        driver.click(By.XPATH, "//*[@id='okBtn']")
        driver.switch_to().parent_frame()
        driver.click(By.XPATH, "//*[@id='submitBtn']")
        a = driver.find_element(By.XPATH, "//*[@id='listTabBody']//td[text()='粤Z12315']")
        self.assertTrue(a, '添加预约车辆失败')

    def test_case06(self):
        '''查询预约车'''
        driver = self.driver
        driver.open_menu('业务管理', '业务办理')
        driver.click(By.XPATH, "//span[contains(text(),'预约车辆管理')]")
        carNo = driver.gettext(By.XPATH, "//*[@id='listTabBody']/tr[1]/td[1]")
        statusStr = driver.gettext(By.XPATH, "//*[@id='listTabBody']/tr[1]/td[2]")
        isAlways = driver.gettext(By.XPATH, "//*[@id='listTabBody']/tr[1]/td[3]")
        driver.send_keys(By.XPATH, "//input[@placeholder = '车牌号码']", text=carNo)
        driver.click(By.XPATH,
                     "// *[ @ id = 'searchSpan'] // select[ @ name = 'statusStr'] / option[text() = '" + statusStr + "']")
        driver.click(By.XPATH,
                     "// *[ @ id = 'searchSpan'] // select[ @ name = 'isAlways'] / option[text() = '" + isAlways + "']")
        driver.click(By.XPATH, "//span/span[@name = 'queryBtn']")
        a = driver.find_element(By.XPATH, "//*[@id='listTabBody']//td[text()='" + carNo + "']")
        self.assertTrue(a, '查询预约车辆失败')

    def test_case07(self):
        '''编辑预约车'''
        driver = self.driver
        driver.open_menu('业务管理', '业务办理')
        driver.click(By.XPATH, "//span[contains(text(),'预约车辆管理')]")
        driver.click(By.XPATH, "//*[@id='listTabBody']/tr[1]//a[text()='编辑']")
        driver.switch_to_frame("openDialogTarget")
        driver.clear(By.XPATH, "//*[@name='remarks']")
        driver.send_keys(By.XPATH, "//*[@name='remarks']", text="ceshi111")
        driver.click(By.XPATH, "//*[@id='submitBtn']")
        driver.click(By.XPATH, "//*[@id='listTabBody']/tr[1]//a[text()='编辑']")
        driver.switch_to_frame("openDialogTarget")
        a = driver.gettext(By.XPATH, "//*[@name='remarks']")
        self.assertEqual(a, 'ceshi111')

    def test_case08(self):
        '''删除预约车'''
        driver = self.driver
        driver.open_menu('业务管理', '业务办理')
        driver.click(By.XPATH, "//span[contains(text(),'预约车辆管理')]")
        driver.send_keys(By.XPATH, "//input[@placeholder = '车牌号码']", text='粤Z12315')
        driver.click(By.XPATH, "//span/span[@name = 'queryBtn']")
        driver.click(By.XPATH, "//*[@id='listTabBody']/tr[1]//a[text()='删除']")
        driver.click(By.XPATH, "//*[@id='sure']")
        driver.send_keys(By.XPATH, "//input[@placeholder = '车牌号码']", text='粤Z12315')
        driver.click(By.XPATH, "//span/span[@name = 'queryBtn']")
        a = driver.find_element(By.XPATH, "//*[@id='listTabBody']/tr/td[text()='未查找到符合条件的数据，请更换查询条件。']")
        self.assertTrue(a, '删除月租车辆失败')


if __name__=="__main__":
    unittest.main()