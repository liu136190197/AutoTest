from time import sleep

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from test.page_obj.basePage import BasePage


class Page_Obj(BasePage):
    def __init__(self,cookie = None):
        super().__init__()
        self.cookie = cookie

    # 统一定义登陆入口
    def user_login(self, username="user", password="password"):
        loginurl = "http://192.168.1.1:8080/parking/index"
        self.open(loginurl)
        self.find_element(By.XPATH, "//*[@id='dataForm']/div[1]/input").send_keys(username)
        self.find_element(By.XPATH, "//*[@id='dataForm']/div[2]/input").send_keys(password)
        self.find_element(By.XPATH, "//div[2]/span[text()='登录']").click()
        self.cookie = self.get_cookie()
    #定位菜单页面.
    def open_menu(self,a1,a2):
        driver = self.driver
        xpath1 = "//span[contains(string(),'"+a1+"')]"
        xpath2 = "//*[text()='"+a2+"']"
        a = self.find_element(By.XPATH, xpath1)
        ActionChains(driver).move_to_element(a).perform()
        self.click(By.XPATH, xpath2)