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

    def test_case1(self):
        '''添加月租车'''
        driver = self.driver
        driver.open_menu('业务管理', '业务办理')
        driver.click(By.XPATH, "//span[contains(text(),'月租车辆管理')]")
        sleep(0.5)
        driver.click(By.CSS_SELECTOR, "span#monthAdd.btn.addnew")
        sleep(0.5)
        driver.switch_to_frame("openDialogTarget")
        driver.find_element(By.XPATH, "//*[@id='carNo']")
        driver.execute_script("document.getElementById('carNo').value = '粤Z12306'")
        driver.click(By.XPATH, "//*[@id='addCust']")
        sleep(0.5)
        driver.switch_to_frame("openDialogTarget")
        driver.click(By.XPATH, "//*[@id='listTabBody']/tr[6]/td[1]/input")
        sleep(0.5)
        driver.click(By.XPATH, "//*[@id='listTabCustomer']/span")
        driver.click(By.XPATH, "//*[@id='okBtn']")
        sleep(0.5)
        driver.switch_to().parent_frame()
        # driver.switch_to.default_content()  返回主页面
        driver.send_keys(By.XPATH, "//*[@id='invoice']", text="111")
        driver.click(By.XPATH, "//*[@id='submitBtn']")
        driver.click(By.XPATH, "//*[@id='sure']")
        driver.send_keys(By.XPATH, "//input[@placeholder = '车牌号码']", text='粤Z12306')
        driver.click(By.XPATH, "//span/span[@name = 'queryBtn']")
        a = driver.find_element(By.XPATH, "//*[@id='listTabBody']//a[text()='粤Z12306']")
        self.assertTrue(a, '添加月租车辆失败')

    def test_case2(self):
        '''查询月租车'''
        driver = self.driver
        driver.open_menu('业务管理', '业务办理')
        driver.click(By.XPATH, "//span[contains(text(),'月租车辆管理')]")
        sleep(0.5)
        clientName = driver.gettext(By.XPATH,"//*[@id='listTabBody']/tr[1]/td[1]/a")
        address = driver.gettext(By.XPATH, "//*[@id='listTabBody']/tr[1]/td[2]/a")
        carNo = driver.gettext(By.XPATH, "//*[@id='listTabBody']/tr[1]/td[3]/a")
        endTime = driver.gettext(By.XPATH, "//*[@id='listTabBody']/tr[1]/td[5]")
        endDeta = endTime.split(" ")[0]
        monthlyType = driver.gettext(By.XPATH, "//*[@id='listTabBody']/tr[1]/td[6]")
        driver.send_keys(By.XPATH, "//input[@placeholder = '车牌号码']",text=carNo)
        driver.send_keys(By.XPATH, "//input[@placeholder = '客户姓名']", text=clientName)
        driver.send_keys(By.XPATH, "//input[@placeholder = '房屋地址']", text=address)
        driver.send_keys(By.XPATH, "//input[@placeholder = '到期开始时间']", text=endDeta)
        xpath1 = "// *[ @ id = 'searchSpan'] // select[ @ name = 'monthTypeId'] / option[text() = '"+monthlyType+"']"
        print(xpath1)
        driver.click(By.XPATH, xpath1)
        driver.click(By.XPATH, "//span/span[@name = 'queryBtn']")
        sleep(1)
        a = driver.find_element(By.XPATH, "//*[@id='listTabBody']//a[text()='%s']" %carNo)
        self.assertTrue(a, '查询月租车辆失败')

    def test_case3(self):
        '''编辑月租车'''

    def test_case4(self):
        '''删除月租车'''



if __name__=="__main__":
    unittest.main()