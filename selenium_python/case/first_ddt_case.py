#coding=utf-8
import ddt
import unittest
import sys
sys.path.append('D:\software\python\selenium_python')
from business.register_business import  RegisterBusiness
from selenium import webdriver
import os
import HTMLTestRunner
from utill.excel_unil import  ExcelUntil
import time
#邮箱,用户名，密码，验证码，错误信息定位元素，错误提示信息
ex=ExcelUntil()
data=ex.get_data()
@ddt.ddt
class FirstDdtCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://www.5itest.cn/register')
        self.driver.maximize_window()
        self.login = RegisterBusiness(self.driver)
        # print('这是case初始设置')


    def tearDown(self):
        time.sleep(2)
        # if sys.exc_info()[0]:
        for method_name, error in self._outcome.errors:
            print('erros', self._outcome.errors, error)
            if error:
                case_name = self._testMethodName
                file_path = os.path.join(os.path.dirname(os.getcwd()), 'report', \
                                         case_name + time.strftime('%H%M%S', time.localtime()) + '.png')
                print(file_path)
                self.driver.save_screenshot(file_path)

        # print('这是case后置设置')
        self.driver.close()
    '''@ddt.data(
        ['123','limoumou','123455','code','user_email_error','请输入有效的电子邮件地址'],
        ['@123.com', 'liou', '12455', 'code', 'user_name_error', '字符长度必须小于等于18，一个中文字算2个字符'],
        ['hello@123.com', 'li000你好你好好你好啊', '12455', 'code', 'user_name_error', '字符长度必须小于等于18，一个中文字算2个字符']

    )
    @ddt.unpack
    '''
    @ddt.data(*data)
    def test_register_case(self,data):
        email, username, password, code, assertCode, assertText=data
        email_error=self.login.register_function(email,username,password,code,assertCode,assertText)
        self.assertFalse(email_error,'测试失败')
        # if email_error==True:
        #     print('注册成功了,此条case执行失败')
if __name__=="__main__":
    # unittest.main()
    file_path=os.path.join(os.path.dirname(os.getcwd()),'report','first_case1.html')
    #
    # print(os.path.dirname(os.getcwd()))
    # print(file_path)
    f = open(file_path, 'wb')
    suite=unittest.TestLoader().loadTestsFromTestCase(FirstDdtCase)

    # suite=unittest.TestSuite()
    # suite.addTest(FirstCase('test_login_success'))
    # unittest.TextTestRunner().run(suite)
    runner=HTMLTestRunner.HTMLTestRunner(stream=f,title='this is first report1',description=u'这个是我们第一次测试报告1',verbosity=2)
    runner.run(suite)