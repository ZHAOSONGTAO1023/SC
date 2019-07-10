import os
import random
import time
import unittest
from threading import Thread
from time import sleep
from selenium import webdriver

from SC.testSC.handles.init_self import MyTestCase
from SC.testSC.handles.login import Login
from SC.testSC.handles.parameters import Parameters


class ZP_Test(MyTestCase):

    def testAddZP(self):
        lo = Login(self.driver)
        lo.activity_participant_login()
        p = Parameters(self.driver)
         #需要添加作品的活动
        acc_name=p.get_activity_name()
        print("参加的活动名称为：" + acc_name)
        p.test_activityAccessPage(acc_name)
        p.ZPAdd("3")

# suite = unittest.TestSuite()
# suite.addTest(test_zp.ZP_Test('testAddZP'))

if __name__ == '__main__':
    unittest.main()
    # runner = unittest.TextTestRunner()
    # runner.run(suite)

    # unittest.main()

    # thread_01 = Thread(target=createZP)
    # thread_01.start()

    # for i in range(100):
    #     createZP()
    #     time.sleep(1)
