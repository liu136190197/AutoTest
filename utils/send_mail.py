#coding=utf-8
import os
import smtplib
from email.header import Header
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.utils import formataddr

def send_email(new_report):
    #发送邮件服务器
    smtpserver = 'mail.163.com'
    #发送邮箱
    sender = 'lxy@163.com'
    user = 'lxy'
    password = 'password'
    #接收邮箱
    receiver = 'lxy01@163.com，lxy02@163.com'
    # 读取测试报告中的内容作为邮件的内容
    with open(new_report, 'r', encoding='utf8') as f:
        mail_body = f.read()
    #发送邮件主题
    subject = 'UI自动化邮件测试'
    #编写html 类型的邮件正文
    msg = MIMEMultipart()
    msg1 = MIMEText(mail_body, 'html', 'utf8')
    msg.attach(msg1)
    msg['Subject'] = Header(subject, 'utf-8')
    msg['From'] = formataddr([user, sender])
    msg['To'] = receiver
    #添加附件
    sendfile1 = open(new_report, 'rb').read()
    att1 = MIMEApplication(sendfile1)
    att1.add_header('Content-Disposition', 'attachment', filename="自动化测试报告.html")
    msg.attach(att1)

    # #发送的附件
    # sendfile1 = open('./time.txt','rb').read()
    # att1 = MIMEText(sendfile1, 'base64','utf-8')
    # att1["Content-Type"] = 'application/octet-stream'
    # att1["Content-Disposition"] = 'attachment; filename="time.txt"'
    #
    # sendfile2 = open('./test.jpg','rb').read()
    # att2 = MIMEImage(sendfile2)
    # att2["Content-Type"] = 'application/octet-stream'
    # att2["Content-Disposition"] = 'attachment; filename="test.jpg"'
    #
    # zipFile = 'test.rar'
    # zipApart = MIMEApplication(open(zipFile, 'rb').read())
    # zipApart.add_header('Content-Disposition', 'attachment', filename=zipFile)

    # msgroot = MIMEMultipart('related')
    # msgroot['Subject'] = Header(subject, 'utf-8')
    # msgroot['From'] = sender
    # msgroot['To'] = receiver
    # msgroot.attach(textApart)
    # msgroot.attach(att1)
    # msgroot.attach(att2)
    # msgroot.attach(zipApart)

    #连接发送邮件
    # 连接发送邮件
    try:
        smtp = smtplib.SMTP(smtpserver, 25)
        smtp.login(user, password)
    except smtplib.SMTPException:
        pass
    smtp.sendmail(sender, receiver.split(','), msg.as_string())
    smtp.quit()

#获取最新报告的地址
def acquire_report_address(reports_address):
    # 测试报告文件夹中的所有文件加入到列表
    test_reports_list = os.listdir(reports_address)
    # 按照升序排序生成新的列表
    new_test_reports_list = sorted(test_reports_list)
    # 获取最新的测试报告
    the_last_report = new_test_reports_list[-1]
    # 最新的测试报告的地址
    the_last_report_address = os.path.join(reports_address, the_last_report)
    path = the_last_report_address.replace('\\', '/')
    print(path)
    return path

if __name__=="__main__":
    # acquire_report_address("D:/VKParting/report")
    send_email("D:/VKParting/report/2019-08-21 result.html")