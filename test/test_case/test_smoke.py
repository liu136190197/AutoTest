import datetime
import unittest
from time import sleep

from selenium.webdriver.common.by import By
from test.models.myTest import MyTest

from utils.configall import ConfigAll


class Test_Smoke(MyTest):
    def test_case10(self):
        '''自动化数据清理'''
        configall = ConfigAll()
        #删除账户信息：autotest
        configall.config_database("DELETE FROM sys_user WHERE user_name = '%s'" % ('autotest'))
        #删除车位信息：AUTO_001
        #删除设备：autotest设备
        #删除车道：autotest车道（入)、autotest车道（出)
        #删除出入口：autotest出入口
        #删除区域：autotest区域
        #删除月租车辆类型：月租(autotest)
        #删除储值车辆类型：储值(autotest)
        #删除白名单类型：白名单(autotest)
        #删除月租车：粤ZDH001
        #删除预约车：粤ZDH010
        #删除储值车：粤ZDH020
        #删除白名单：粤ZDH030
        #删除黑名单：粤ZDH040
        #删除灰名单：粤ZDH050

    def test_case11(self):
        '''添加账户'''
        driver=self.driver
        driver.open_menu('系统设置','系统权限 ')
        driver.click(By.XPATH, "//*[@id='userAdd']")
        driver.switch_to_frame("openDialogTarget")
        driver.click(By.XPATH, "//*[@id='formInputDiv']//select/option[text()='管理角色']")
        driver.send_keys(By.XPATH,"//input[@placeholder='真实姓名']",text ="AutoTestAccount")
        driver.send_keys(By.XPATH, "//input[@name = 'userName' and @placeholder = '登录账号']",text ="autotest")
        driver.send_keys(By.XPATH, "//input[@placeholder='密码']",text ="a123456")
        driver.send_keys(By.XPATH, "//input[@placeholder='手机号码']", text ="13656565656")
        driver.click(By.XPATH, "//*[@id='submitBtn']")
        a=driver.find_element(By.XPATH,"//*[@id='listTabBody']//td[text()='autotest']")
        self.assertTrue(a, '添加账户失败')

    def test_case12(self):
        '''添加区域'''
        driver=self.driver
        driver.open_menu('系统设置', '车场配置')
        driver.click(By.XPATH,"//span[text()='区域']")
        driver.click(By.XPATH, "//span[text()='新增']")
        driver.switch_to_frame("openDialogTarget")
        driver.send_keys(By.XPATH, "//input[@name = 'name' and @placeholder = '区域名称']", text="autotest区域")
        driver.send_keys(By.XPATH, "//input[@name = 'totalVirtualSpace' and @placeholder = '虚拟车位总数']", text="1000")
        driver.send_keys(By.XPATH, "//input[@name = 'maxVisitCount' and @placeholder = '最大临停准停数']", text="500")
        driver.click(By.XPATH, "//input[@id='monthC']")
        driver.click(By.XPATH, "//button[@id='submitBtn']")
        a = driver.find_element(By.XPATH, "//td[contains(text(),'autotest区域')]")
        self.assertTrue(a, '添加区域失败')

    def test_case13(self):
        '''添加出入口'''
        driver = self.driver
        driver.open_menu('系统设置', '车场配置')
        driver.click(By.XPATH, "//span[text()='出入口']")
        driver.click(By.XPATH, "//a[text()='新增']")
        driver.switch_to_frame("openDialogTarget")
        driver.send_keys(By.XPATH, "//input[@name = 'name' and @placeholder = '出入口名称']", text="autotest出入口")
        driver.click(By.XPATH, "//*[@id='formInputDiv']/div[2]//select/option[last()]")
        driver.execute_script("window.scrollTo(0,1000)")
        driver.click(By.XPATH, "//button[@id='submitBtn']")
        a = driver.find_element(By.XPATH, "//*[@id='listTabBody']//td[text()='autotest出入口']")
        self.assertTrue(a, '添加出入口失败')

    def test_case14(self):
        '''添加车道'''
        driver = self.driver
        driver.open_menu('系统设置', '车场配置')
        driver.click(By.XPATH, "//span[text()='车道']")
        driver.click(By.XPATH, "//span[text()='新增']")
        driver.switch_to_frame("openDialogTarget")
        driver.send_keys(By.XPATH, "//input[@name = 'name' and @placeholder = '车道名称']", text="autotest车道（入)")
        ele = driver.find_elements(By.XPATH, "//*[@id='formInputDiv']//select/option[last()]")
        ele[0].click()
        driver.click(By.XPATH, "//label[text()=' 入场车道']")
        driver.click(By.XPATH, "//*[@id='formInputDiv']/div[4]/div/label[1]")
        driver.click(By.XPATH, "//*[@id='formInputDiv']/div[4]/div/label[2]")
        driver.click(By.XPATH, "//*[@id='formInputDiv']/div[4]/div/label[3]")
        driver.click(By.XPATH, "//*[@id='formInputDiv']/div[4]/div/label[4]")
        driver.click(By.XPATH, "//*[@id='formInputDiv']/div[4]/div/label[5]")
        driver.click(By.XPATH, "//label[text()=' autotest区域']")
        driver.execute_script("window.scrollTo(0,1000)")
        ele[1].click()
        driver.click(By.XPATH, "//button[@id='submitBtn']")
        a = driver.find_element(By.XPATH, "//td[contains(text(),'autotest车道（入)')]")
        self.assertTrue(a, '添加车道失败')

        driver.click(By.XPATH, "//span[text()='新增']")
        driver.switch_to_frame("openDialogTarget")
        driver.send_keys(By.XPATH, "//input[@name = 'name' and @placeholder = '车道名称']", text="autotest车道（出)")
        ele1 = driver.find_elements(By.XPATH, "//*[@id='formInputDiv']//select/option[last()]")
        ele1[0].click()
        driver.click(By.XPATH, "//label[text()=' 出场车道']")
        driver.click(By.XPATH, "//*[@id='formInputDiv']/div[4]/div/label[1]")
        driver.click(By.XPATH, "//*[@id='formInputDiv']/div[4]/div/label[2]")
        driver.click(By.XPATH, "//*[@id='formInputDiv']/div[4]/div/label[3]")
        driver.click(By.XPATH, "//*[@id='formInputDiv']/div[4]/div/label[4]")
        driver.click(By.XPATH, "//*[@id='formInputDiv']/div[4]/div/label[5]")
        driver.execute_script("window.scrollTo(0,1000)")
        ele1[1].click()
        driver.click(By.XPATH, "//button[@id='submitBtn']")
        b = driver.find_element(By.XPATH, "//td[contains(text(),'autotest车道（出)')]")
        self.assertTrue(b, '添加车道失败')

    def test_case15(self):
        '''添加设备'''
        driver = self.driver
        driver.open_menu('系统设置', '车场配置')
        driver.click(By.XPATH, "//span[text()='设备']")
        driver.click(By.XPATH, "//span[contains(text(),'新增')]")
        driver.switch_to_frame("openDialogTarget")
        driver.send_keys(By.XPATH, "//input[@name = 'name' and @placeholder = '设备名称']", text="autotest设备")
        driver.click(By.XPATH, "//*[@id='formInputDiv']//select/option[text()='主摄像头']")
        driver.click(By.XPATH, "//*[@id='formInputDiv']//select/option[last()]")
        driver.send_keys(By.XPATH, "//input[@name = 'ipAddress' and @placeholder = 'IP地址']", text="0.0.0.0")
        driver.send_keys(By.XPATH, "//input[@name = 'port' and @placeholder = '端口号']", text="0.0.0.0")
        driver.execute_script("window.scrollTo(0,1000)")
        driver.click(By.XPATH, "//button[@id='submitBtn']")
        a = driver.find_element(By.XPATH, "//td[contains(text(),'autotest设备')]")
        self.assertTrue(a, '添加设备失败')

    def test_case16(self):
        '''添加车位'''
        driver = self.driver
        driver.open_menu('系统设置', '车场配置')
        driver.click(By.XPATH, "//span[text()='车位']")
        driver.click(By.XPATH, "//span[contains(text(),'新增')][1]")
        driver.switch_to_frame("openDialogTarget")
        driver.click(By.XPATH, "//*[@id='dataForm']//select/option[last()]")
        driver.send_keys(By.XPATH, "//label[text() = '车位编号']/../div/input[1]", text="AUTO_001")
        driver.click(By.XPATH, "//button[@id='submitBtn']")
        a = driver.find_element(By.XPATH, "//td[2][contains(text(),'AUTO_001')]")
        self.assertTrue(a, '添加车位失败')

    def test_case17(self):
        '''月租车辆类型设置'''
        driver = self.driver
        driver.open_menu('系统设置', '类型设置')
        driver.click(By.XPATH, "//span[contains(text(),'月租车辆类型')]")
        driver.click(By.XPATH, "//a[contains(text(),'新增')]")
        driver.switch_to_frame("openDialogTarget")
        driver.send_keys(By.XPATH, "//input[@name = 'name' and @placeholder = '月租类型名称']", text="月租(autotest)")
        driver.send_keys(By.XPATH, "//input[@name = 'fee' and @placeholder = '单价']", text="100")
        eles = driver.find_elements(By.XPATH, "//tbody[@id='listTabBody']/tr//input")
        for ele in eles:
            ele.click()
        driver.click(By.XPATH, "//button[@id='submitBtn']")
        driver.click(By.XPATH, "//*[@id='sure']")
        a = driver.find_element(By.XPATH, "//td[contains(text(),'月租(autotest)')]")
        self.assertTrue(a, '添加月租车辆类型失败')

    def test_case18(self):
        '''储值车辆类型设置'''
        driver = self.driver
        driver.open_menu('系统设置', '类型设置')
        driver.click(By.XPATH, "//span[contains(text(),'储值车辆类型')]")
        driver.click(By.XPATH, "//a[contains(text(),'新增')]")
        driver.switch_to_frame("openDialogTarget")
        driver.send_keys(By.XPATH, "//input[@name = 'name' and @placeholder = '储值类型名称']", text="储值(autotest)")
        driver.send_keys(By.XPATH, "//div/textarea", text="自动化测试")
        driver.click(By.XPATH, "//button[@id='submitBtn']")
        a = driver.find_element(By.XPATH, "//td[contains(text(),'储值(autotest)')]")
        self.assertTrue(a, '添加储值车辆类型失败')

    def test_case19(self):
        '''白名单类型设置'''
        driver = self.driver
        driver.open_menu('系统设置', '类型设置')
        driver.click(By.XPATH, "//span[contains(text(),'白名单类型')]")
        driver.click(By.XPATH, "//a[contains(text(),'新增')]")
        driver.switch_to_frame("openDialogTarget")
        driver.send_keys(By.XPATH, "//input[@name = 'name' and @placeholder = '白名单类型']", text="白名单(autotest)")
        driver.click(By.XPATH, "//div[@name='isCall']/span[2]")
        eles = driver.find_elements(By.XPATH, "//*[@id='dataForm']//ul/li[3]/div[2]//span")
        for ele in eles:
            ele.click()
        driver.click(By.XPATH, "//span[@id='submitBtn']")
        a = driver.find_element(By.XPATH, "//td[contains(text(),'白名单(autotest)')]")
        self.assertTrue(a, '添加白名单车辆类型失败')

    def test_case20(self):
        '''计费规则设置'''
        driver = self.driver
        driver.open_menu('系统设置', '费率管理')
        driver.click(By.XPATH, "//span[contains(text(),'计费规则')]")
        driver.click(By.XPATH, "//a[contains(text(),'新增')]")
        driver.switch_to_frame("openDialogTarget")
        driver.click(By.XPATH, "//span[@name='carType'][2]")
        driver.click(By.XPATH, "//*[@id='ruleContainer']//select/option[text()='标准模板3']")
        driver.send_keys(By.XPATH, "//*[@id='dataForm']/div[1]//input[@name='freeMin']", text="0")
        driver.send_keys(By.XPATH, "//*[@id='dataForm']/div[1]//input[@name='cycleGap']", text="24")
        driver.send_keys(By.XPATH, "//*[@id='dataForm']/div[1]//input[@name='loopMaxFee']", text="100")
        driver.click(By.XPATH, "//*[@id='dataForm']/div[2]/span//input")
        driver.send_keys(By.XPATH, "//*[@id='dataForm']/div[2]/div/span[2]/input[1]", text="5")
        driver.send_keys(By.XPATH, "//*[@id='dataForm']/div[2]/div/span[2]/input[2]", text="1")
        driver.send_keys(By.XPATH, "//*[@id='dataForm']/div[2]/div/span[3]/input[1]", text="100")
        driver.send_keys(By.XPATH, "//*[@id='dataForm']/div[2]/div/span[4]/input[1]", text="1440")
        driver.execute_script("window.scrollTo(0,1000)")
        driver.send_keys(By.XPATH, "//*[@id='dataForm']/div[6]/input", text="计费(autotest)")
        driver.click(By.XPATH, "//*[@id='dataForm']/div[6]/a[1]")
        a = driver.find_element(By.XPATH, "//td[contains(text(),'计费(autotest)')]")
        self.assertTrue(a, '添加计费规则失败')

    def test_case21(self):
        '''添加月租车'''
        driver = self.driver
        driver.open_menu('业务管理', '业务办理')
        driver.click(By.XPATH, "//span[contains(text(),'月租车辆管理')]")
        sleep(0.5)
        driver.click(By.CSS_SELECTOR, "span#monthAdd.btn.addnew")
        sleep(0.5)
        driver.switch_to_frame("openDialogTarget")
        driver.find_element(By.XPATH, "//*[@id='carNo']")
        driver.execute_script("document.getElementById('carNo').value = '粤ZDH001'")
        driver.click(By.XPATH, "//*[@id='addCust']")
        sleep(0.5)
        driver.switch_to_frame("openDialogTarget")
        driver.click(By.XPATH, "//*[@id='listTabBody']/tr[6]/td[1]/input")
        sleep(0.5)
        driver.click(By.XPATH, "//*[@id='listTabCustomer']/span")
        driver.click(By.XPATH, "//*[@id='okBtn']")
        sleep(0.5)
        driver.switch_to().parent_frame()
        driver.send_keys(By.XPATH, "//*[@id='invoice']", text="111")
        driver.click(By.XPATH, "//*[@id='submitBtn']")
        driver.click(By.XPATH, "//*[@id='sure']")
        a = driver.find_element(By.XPATH, "//*[@id='listTabBody']//a[text()='粤ZDH001']")
        self.assertTrue(a, '添加月租车辆失败')

    def test_case22(self):
        '''添加预约车'''
        driver = self.driver
        driver.open_menu('业务管理', '业务办理')
        driver.click(By.XPATH, "//span[contains(text(),'预约车辆管理')]")
        sleep(0.5)
        driver.click(By.CSS_SELECTOR, "span#reserveAdd.btn.addnew")
        sleep(0.5)
        driver.switch_to_frame("openDialogTarget")
        driver.find_element(By.XPATH, "//*[@id='carNo']")
        driver.execute_script("document.getElementById('carNo').value = '粤ZDH010'")
        driver.send_keys(By.XPATH, "//input[@name = 'visitor' and @placeholder = '访客姓名']", text="autotest")
        driver.send_keys(By.XPATH, "//input[@name = 'mainMobile' and @placeholder = '手机号码']", text="13666666666")
        driver.click(By.XPATH, "//*[@id='addCust']")
        sleep(0.5)
        driver.switch_to_frame("openDialogTarget")
        driver.click(By.XPATH, "//*[@id='vistorContent']/div[2]//span[1]")
        driver.click(By.XPATH, "//*[@id='vistorContent']/div[2]//span[1]")
        driver.click(By.XPATH, "//*[@id='vistorContent']/div[2]//span[1]")
        driver.click(By.XPATH, "//*[@id='vistorContent']/div[2]//span[1]")
        driver.click(By.XPATH, "//*[@id='vistorContent']/div[2]//span[1]")
        driver.click(By.XPATH, "//*[@id='okBtn']")
        sleep(0.5)
        driver.switch_to().parent_frame()
        driver.click(By.XPATH, "//*[@id='submitBtn']")
        a = driver.find_element(By.XPATH, "//*[@id='listTabBody']//td[text()='粤ZDH010']")
        self.assertTrue(a, '添加预约车辆失败')

    def test_case23(self):
        '''添加储值车'''
        driver = self.driver
        driver.open_menu('业务管理', '业务办理')
        driver.click(By.XPATH, "//span[contains(text(),'储值车辆管理')]")
        sleep(0.5)
        driver.click(By.XPATH, "//span[contains(text(),'新增')]")
        sleep(0.5)
        driver.switch_to_frame("openDialogTarget")
        driver.find_element(By.XPATH, "//*[@id='carNo']")
        driver.execute_script("document.getElementById('carNo').value = '粤ZDH020'")
        driver.send_keys(By.XPATH, "//textarea[@name = 'remarks' and @placeholder = '备注']", text="autotest")
        driver.click(By.XPATH, "//*[@id='addCust']")
        sleep(0.5)
        driver.switch_to_frame("openDialogTarget")
        driver.click(By.XPATH, "//*[@id='listTabBody']/tr[6]/td[1]/input")
        sleep(0.5)
        driver.click(By.XPATH, "//*[@id='listTabCustomer']/span")
        driver.click(By.XPATH, "//*[@id='okBtn']")
        sleep(0.5)
        driver.switch_to().parent_frame()
        driver.click(By.XPATH, "//*[@id='submitBtn']")
        a = driver.find_element(By.XPATH, "//*[@id='listTabBody']//td[text()='粤ZDH020']")
        self.assertTrue(a, '添加储值车辆失败')

    def test_case24(self):
        '''添加白名单'''
        driver = self.driver
        driver.open_menu('业务管理', '业务办理')
        driver.click(By.XPATH, "//span[contains(text(),'白名单管理')]")
        sleep(0.5)
        driver.click(By.XPATH, "//span[contains(text(),'新增')]")
        sleep(0.5)
        driver.switch_to_frame("openDialogTarget")
        driver.find_element(By.XPATH, "//*[@id='carNo']")
        driver.execute_script("document.getElementById('carNo').value = '粤ZDH030'")
        now = datetime.datetime.now()
        endnow = now + datetime.timedelta(days=30)
        nowdate = now.strftime("%Y-%m-%d")
        enddate = endnow.strftime("%Y-%m-%d")
        driver.send_keys(By.XPATH, "//input[@name = 'startTimeStr' and @placeholder = '有效起始时间']", text=nowdate)
        driver.send_keys(By.XPATH, "//input[@name = 'endTimeStr' and @placeholder = '有效起始时间']", text=enddate)
        driver.send_keys(By.XPATH, "//input[@name = 'visitor' and @placeholder = '车主姓名']", text="autotestname")
        driver.send_keys(By.XPATH, "//input[@name = 'mainMobile' and @placeholder = '手机号码']", text="13558585858")
        driver.send_keys(By.XPATH, "//input[@name = 'station' and @placeholder = '岗位']", text="自动化岗位")
        driver.send_keys(By.XPATH, "//input[@name = 'processCode' and @placeholder = '审批单号']", text="123456")
        driver.click(By.XPATH, "//*[@id='submitBtn']")
        a = driver.find_element(By.XPATH, "//*[@id='listTabBody']//td[text()='粤ZDH030']")
        self.assertTrue(a, '添加白名单失败')

    def test_case25(self):
        '''添加黑名单'''
        driver = self.driver
        driver.open_menu('业务管理', '业务办理')
        driver.click(By.XPATH, "//span[contains(text(),'黑名单管理')]")
        sleep(0.5)
        driver.click(By.XPATH, "//span[contains(text(),'新增')]")
        sleep(0.5)
        driver.switch_to_frame("openDialogTarget")
        driver.find_element(By.XPATH, "//*[@id='carNo']")
        driver.execute_script("document.getElementById('carNo').value = '粤ZDH040'")
        driver.send_keys(By.XPATH, "//textarea[@name = 'blackDescription' and @placeholder = '黑名单描述']", text="自动化测试黑名单")
        driver.click(By.XPATH, "//*[@id='submitBtn']")
        a = driver.find_element(By.XPATH, "//*[@id='listTabBody']//td[text()='粤ZDH040']")
        self.assertTrue(a, '添加黑名单失败')

    def test_case26(self):
        '''添加灰名单'''
        driver = self.driver
        driver.open_menu('业务管理', '业务办理')
        driver.click(By.XPATH, "//span[contains(text(),'灰名单列表管理')]")
        driver.execute_script("document.getElementById('addCarNo').value = '粤ZDH050'")
        driver.click(By.XPATH, "//*[@id='grayAdd']")
        a = driver.find_element(By.XPATH, "//*[@id='grayListContent']//span[text()='粤ZDH050']")
        self.assertTrue(a, '添加灰名单失败')

if __name__ == "__main__":
    unittest.main()