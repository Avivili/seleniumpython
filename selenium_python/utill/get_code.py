#coding=utf-8
from PIL import Image
from util.ShowapiRequest import ShowapiRequest
import time
import base64
from selenium import webdriver

class GetCode():
    def __init__(self,driver):
        self.driver=driver


    def get_code_image(self,file_name):
        self.driver.save_screenshot(file_name)
        # code_element = self.get_user_element('code_image')
        code_element=self.driver.find_element_by_id('getcode_num')
        print(code_element.location)
        left = code_element.location['x']
        top = code_element.location['y']
        right = code_element.size['width'] + left
        height = code_element.size['height'] + top
        im = Image.open(file_name)
        # print(dir(im))
        #
        img = im.crop((left, top, right, height))

        img.save(file_name)
        time.sleep(2)

    def getBase64Code(self,file_name):
        '''python生成图片的base64编码'''
        with open(file_name, 'rb') as f:
            base64_data = base64.b64encode(f.read())
            s = base64_data.decode()
            data = '%s' %s
            return data



    def code_online(self,file_name):
        self.get_code_image(file_name)
        data=self.getBase64Code(file_name)
        print(data)
        r = ShowapiRequest("http://route.showapi.com/2360-2", "1171374set", "247fa65f14b04f7089d2907e3240a685set")
        r.addBodyPara("typeId", "35")
        r.addBodyPara("convert_to_jpg", "0")
        r.addBodyPara("file_base64",data)
        # r.addBodyPara("needMorePrecise", "0")
        # r.addFilePara("image", file_name)  # 文件上传时设置
        res = r.post()
        print(res.json())
        text = res.json()['showapi_res_body']['pic_str']
        print(text)
        time.sleep(2)
        return text
if  __name__=='__main__':
    driver = webdriver.Chrome()
    driver.get("http://www.5itest.cn/register")
    file_name='D:/imooc.png'
    get_code=GetCode(driver)
    get_code.code_online(file_name)