import os
import time
import unittest

#构造测试集
from SC.testSC.TestCase import test_activity, test_zp

if __name__=='__main__':
    # default Test Loader 默认测试用例加载器
    #discover 发现, 查找所有符合条件的测试用例
    # *Test.py中*星号代表通配符,可以表示任何string
    # Test.py 是我们自己起的文件名的规则
    # 我们所有的测试用例都是以Test.py结尾的
    base_path = os.path.dirname(os.path.abspath(__file__))
    print(base_path)
    suite = unittest.defaultTestLoader.discover(base_path, pattern='test_*.py')
    # 文本的测试用例运行器, 通过这个运行器,运行suite中所有的测试用例
    unittest.TextTestRunner().run(suite)
