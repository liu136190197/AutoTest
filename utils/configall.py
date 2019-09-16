from configparser import ConfigParser
import os

import pymysql


class ConfigAll():
    def config_ini(self):
        config = ConfigParser()
        # file_path1 = os.path.dirname(os.path.abspath('.'))
        file_path1 = os.path.dirname(os.path.dirname(__file__))
        file_path2 = file_path1.replace('\\', '/')
        file_path3 = file_path2.split('/utils')[0]
        file_path = file_path3 + "/config/config.ini"
        config.read(file_path, encoding="utf-8")
        # print(file_path)
        return config
    def config_database(self,sql=None):
        db = pymysql.connect(host='10.39.131.201', port=3307, user='user',
                               password='password',
                               db='parking1', charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
        cursor = db.cursor()
        try:
            cursor.execute(sql)
            db.commit()
        except:
            # 发生错误时回滚
            db.rollback()
        data = cursor.fetchone()
        db.close()
if __name__ == '__main__':
    configall = ConfigAll()
    configall.config_database("DELETE FROM sys_user WHERE user_name = '%s'" %('autotest'))
