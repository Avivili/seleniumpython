#coding=utf-8
import unittest
from selenium import webdriver
class FirstCase01(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('所有case执行之前的前置')
    @classmethod
    def tearDownClass(cls):
        print('所有case执行之后的后置')

    def setUp(self):
        # self.driver=webdriver.Chrome()
        # self.driver.get('http://www.5itest.cn/register')
        # self.login=Re
        print('这个是case的前置条件')
    def tearDown(self):
        print('这个是case的后置条件')
    @unittest.skip
    def testfirst01(self):
        print("这是第一条case")
    def testfirst02(self):
        print('这是第二条case')

    def testfirst03(self):
        print('这是第san条case')

if __name__=='__main__':
    # unittest.main()
    suite=unittest.TestSuite()
    suite.addTest(FirstCase01('testfirst02'))
    # suite.addTest(FirstCase01('testfirst01'))
    unittest.TextTestRunner().run(suite)