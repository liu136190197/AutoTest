#coding=utf-8
import unittest
from utils.HTMLTestRunner import HTMLTestRunner
import time
import os
from utils.send_mail import send_email

test_dir='./test/test_case'
#定义discover 方法的参数
discover = unittest.defaultTestLoader.discover(test_dir,pattern='test_*.py',top_level_dir=None)

if __name__ == "__main__":
    # 获取当前时间
    now = time.strftime("%Y-%m-%d %H_%M_%S", time.localtime(time.time()))
    # 定义个报告存放路径
    path = os.path.dirname(os.path.abspath(__file__))
    path1 = path.replace('\\', '/')
    filename = path1 + "/report/" + now + "result.html"
    print(filename)
    fp = open(filename, 'wb')
    # 定义测试报告
    runner = HTMLTestRunner(
        stream=fp,
        title=u'自动化测试报告',
        description=u'用例执行情况：')
    # 运行测试用例
    runner.run(discover)
    # 关闭报告文件
    fp.close()
    # 发送邮件
    send_email(filename)
