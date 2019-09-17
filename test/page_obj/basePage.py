import datetime
import os
from datetime import time
from time import sleep
#from selenium.webdriver.remote import webdriver
from selenium import webdriver
# from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from test.models.driver import logger, Browser


class BasePage(object):
    ''' 基本类，用于所页面的继承'''
    def __init__(self):
        self.driver = Browser().driver
    #打开网址
    def open(self,base_url):
        self.driver.get(base_url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
    #退出浏览器
    def quit_browser(self):
        self.driver.quit()
        logger.info("driver.quit")
    # 浏览器前进操作
    def forward(self):
        self.driver.forward()
        logger.info("Click forward on current page.")
    # 浏览器后退操作
    def back(self):
        self.driver.back()
        logger.info("Click back on current page.")
    # 显式等待
    def wait(self, *loc, seconds):
        try:
            wait_ = WebDriverWait(self.driver, seconds)
            wait_.until(self.driver.find_element(*loc))
            logger.info("wait for %d seconds." % seconds)
        except Exception as e:
            logger.error("Failed to load the element with %s" % e)
    #错误截图
    def get_windows_img(self):
        now = datetime.datetime.now()
        time_loc = now.strftime("%Y-%m-%d %H_%M_%S")
        base_dir = os.path.dirname(os.path.dirname(__file__))
        base_dir = str(base_dir)
        base_dir = base_dir.replace('\\', '/')
        base = base_dir.split('/test')[0]
        file_path = base + "/report/image/" + time_loc + ".png"
        try:
            self.driver.get_screenshot_as_file(file_path)
            logger.info("Had take screenshot and save to folder : /report/")
        except Exception as e:
            logger.error("Failed to take screenshot! %s" % e)
            self.get_windows_img()
    #iframe、页面弹框操作
    def switch_to(self):
        try:
            a = self.driver.switch_to
            logger.info("switch_to")
            return a
        except Exception as e:
            logger.error("Failed to switch_to %s" % e)
    #定位iframe（id、name）
    def switch_to_frame(self, *loc):
        try:
            self.driver.switch_to_frame(*loc)
            logger.info("switch_to_frame succeed: %s" % loc[0])
        except Exception as e:
            logger.error("Failed to switch_to_frame %s" % e)
    #查找网页元素
    def find_element(self, *loc):
        try:
            sleep(0.5)
            a = self.driver.find_element(*loc)
            sleep(0.5)
            logger.info("find_element succeed: %s, %s" % (loc[0], loc[1]))
            return a
        except Exception as e:
            logger.error("Failed to find_element %s" % e)
            self.get_windows_img()
    #查找网页元素集合
    def find_elements(self, *loc):
        try:
            sleep(0.5)
            a = self.driver.find_elements(*loc)
            sleep(0.5)
            logger.info("find_elements succeed:%s, %s" % (loc[0], loc[1]))
            return a
        except Exception as e:
            logger.error("Failed to find_element %s" % e)
            self.get_windows_img()
    # 获取元素文本
    def gettext(self, *selector):
        el = self.find_element(*selector)
        try:
            a = el.text
            logger.info("Get text in input box :%s" %a)
            return a
        except Exception as e:
            logger.error("Failed to get text %s" % e)
            self.get_windows_img()
    # 清除文本框
    def clear(self, *selector):
        el = self.find_element(*selector)
        try:
            el.clear()
            logger.info("Clear text in input box before typing.%s" %selector)
        except Exception as e:
            logger.error("Failed to clear in input box with %s" % e)
            self.get_windows_img()
    # 输入字符串
    def send_keys(self, *selector, text):
        el = self.find_element(*selector)
        el.clear()
        try:
            el.send_keys(text)
            logger.info("Had type \' %s \' in inputBox" % text)
        except Exception as e:
            logger.error("Failed to select in input box with %s" % e)
            self.get_windows_img()
    # 点击元素
    def click(self, *selector):
        el = self.find_element(*selector)
        try:
            el.click()
            logger.info("The element was clicked：%s" % el.text)
        except Exception as e:
            logger.error("Failed to click the element with %s" % e)
    # 鼠标事件（左键点击）
    def move_element_click(self, *loc):
        mouse = self.find_element(*loc)
        try:
            ActionChains(self.driver).move_to_element(mouse).perform()
            self.click(*loc)
            pass
        except Exception as e:
            logger.error("Failed to click move_element with %s" % e)
            self.get_windows_img()
    #执行js
    def execute_script(self, src):
        try:
            self.driver.execute_script(src)
            logger.info("execute_script %s" % src)
        except Exception as e:
            logger.error("Failed to execute_script %s" % e)
            self.get_windows_img()
    #获取cookie
    def get_cookie(self):
        try:
            a = self.driver.get_cookie("JSESSIONID")
            logger.info("get_cookies %s" % a)
            return {a['name']:a['value']}
        except Exception as e:
            logger.error("Failed to get_cookiet %s" % e)
            self.get_windows_img()
