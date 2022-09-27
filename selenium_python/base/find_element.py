#coding=utf-8
from utill.read_ini import  ReadIni

class FindElement():
    def __init__(self,driver):
        self.driver=driver
    def get_element(self,key):
        read_ini=ReadIni()
        data=read_ini.get_value(key)
        # print('data',data)
        by=data.split('>')[0]
        value=data.split('>')[1]
        try:
            if by=='id':
                # print(self.driver.find_element_by_id(value))
                return self.driver.find_element_by_id(value)
            if by=='name':
                return self.driver.find_element_by_name(value)
            if by=='className':
                return self.driver.find_element_by_class_name(value)
            else:
                return self.driver.find_element_by_xpath(value)
        except:
            # self.driver.save_screenshot('D:\software\python\selenium_python\Image\%s.png' %value)
            return None
