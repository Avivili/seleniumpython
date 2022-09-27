#coding=utf-8
import logging
import os
import datetime
class UserLog():
    def __init__(self):
        self.logger=logging.getLogger()
        self.logger.setLevel(logging.DEBUG)
        # consle=logging.StreamHandler()
        # logger.addHandler(consle)
        # logger.debug('console info')
        # consle.close()
        # logger.removeHandler(consle)
        #文件名字
        base_dir=os.path.dirname(os.path.abspath(__file__))
        log_dir=os.path.join(base_dir,'logs')
        log_file=datetime.datetime.now().strftime('%Y-%m-%d')+'.log'
        log_name=log_dir+'\\'+log_file
        # print(log_name)


        self.file_hand=logging.FileHandler(log_name)
        self.file_hand.setLevel(logging.INFO)
        formatter=logging.Formatter('%(asctime)s %(filename)s %(funcName)s--> %(levelno)s: %(levelname)s %(message)s')
        self.file_hand.setFormatter(formatter)
        self.logger.addHandler(self.file_hand)

        # self.logger.debug('teste1234')

    def get_log(self):
        return self.logger

    def close_handler(self):

        self.logger.removeHandler(file_hand)
        self.file_hand.close()
