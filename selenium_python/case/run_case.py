#coding=utf-8
import unittest
import os
class RunCase(unittest.TestCase):

    def test_case(self):
        exec_path=os.getcwd()
        suite=unittest.defaultTestLoader.discover(exec_path,'unittest_*.py')
        unittest.TextTestRunner().run(suite)
if __name__=='__main__':
    unittest.main()

