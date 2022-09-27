#coding=utf-8
import unittest
import sys
sys.path.append('D:\software\python\selenium_python')
from business.register_business import  RegisterBusiness
from selenium import webdriver
import os
import HTMLTestRunner
import time
from log.user_log import UserLog

class FirstCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.log = UserLog()
        cls.logger = cls.log.get_log()
        cls.file_name='D:\software\python\selenium_python\Image\\test001.png'

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.log.close_handler()

    def setUp(self):
        self.driver=webdriver.Chrome()
        self.driver.get('http://www.5itest.cn/register')
        self.driver.maximize_window()
        self.logger.info('this is setup log')

        self.login=RegisterBusiness(self.driver)
        print('这是case初始设置')

    def tearDown(self):
        time.sleep(2)
        #if sys.exc_info()[0]:
        for method_name,error in self._outcome.errors:
                print('erros',self._outcome.errors,error)
                if error:

                    case_name=self._testMethodName
                    file_path = os.path.join(os.path.dirname(os.getcwd()), 'report', \
                                             case_name+time.strftime('%H%M%S',time.localtime())+'.png')
                    print(file_path)
                    self.driver.save_screenshot(file_path)


        print('这是case后置设置')


    def test_login_email_error(self):
        email_error=self.login.login_email_error('34','user111','1111',self.file_name)
        return self.assertFalse(email_error,'测试失败')
        # if email_error==True:
        #     print('注册成功了,此条case执行失败')

    def test_login_username_error(self):
        name_error=self.login.login_name_error('34@qq.com','user111','1111',self.file_name)
        self.assertFalse(name_error)
        # if name_error==True:
        #     print('注册成功了,此条case执行失败')

    def test_login_password_error(self):
        password_error=self.login.login_password_error('34@qq.com','user111','1111',self.file_name)
        self.assertFalse(password_error)
        # if password_error==True:
        #     print('注册成功了,此条case执行失败')
    def test_login_code_error(self):
        code_error=self.login.login_code_error('34@qq.com','user111','1111',self.file_name)
        self.assertFalse(code_error)
        # if code_error==True:
        #     print('注册成功了,此条case执行失败')
    def test_login_success(self):
        success = self.login.user_base('34@qq.com', 'use111', '11117', self.file_name)
        self.assertFalse(success)
        # if self.login.register_success()==True:
        #     print('注册成功')

# def main():
#     first=FirstCase()
#     # first.test_login_code_error()
#     first.test_login_email_error()
    # first.test_login_password_error()
    # first.test_login_username_error()
    # first.test_login_success()

if __name__=='__main__':
    file_path=os.path.join(os.path.dirname(os.getcwd()),'report','first_case.html')
    #
    # print(os.path.dirname(os.getcwd()))
    # print(file_path)
    f=open(file_path,'wb')
    suite=unittest.TestSuite()
    suite.addTest(FirstCase('test_login_success'))
    # unittest.TextTestRunner().run(suite)
    runner=HTMLTestRunner.HTMLTestRunner(stream=f,title='this is first report',description=u'这个是我们第一次测试报告',verbosity=2)
    runner.run(suite)