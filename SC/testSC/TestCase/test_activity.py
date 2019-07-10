import os
import time
import unittest
from time import sleep
from selenium.webdriver.support.ui import Select
from selenium import webdriver
from SC.testSC.handles.init_self import MyTestCase
from SC.testSC.handles.login import Login
from SC.testSC.handles.parameters import Parameters


class activity(MyTestCase):
    def test_activityAdd(self):
        lo = Login(self.driver)
        lo.activity_builder_login()
        p = Parameters(self.driver)
        p.test_accessToAccBasciInfo()

        acc_name = '活动ZH' + time.strftime('%m%d%H%M', time.localtime(time.time()))  # 活动名称
        p.test_activity_info_write(acc_name,3,3)
        # TODO 将活动名称写入一个txt文档，再在test_zp中读取出来.。。
        p.save_activity_name(acc_name)
        lo.shenhe_login()
        p.test_activityShenHe(acc_name)


if __name__ == '__main__':
    unittest.main()

# acc_start_time_row = 6  # tr[5]/td[2]  为20号，一天换一个，  (5为添加星期的行)
# acc_start_time_col = 6  # tr[5]/td[2]  为20号，一天换一个，  (2为添加日期控件的列)