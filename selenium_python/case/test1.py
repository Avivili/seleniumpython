import ddt
import unittest
@ddt.ddt
class DdtTest(unittest.TestCase):

    def setUp(self):
        print('这是测试开始')
    def tearDown(self):
        print('这是测试结束')

    data=[(1,2,3),(4,5,6)]

    @ddt.data(*data)
    # @ddt.unpack
    def test_case1(self,value):
        v1,v2,v3=value
        print(f'v1 {v1},v2 {v2},v3 {v3}')
        print('another output format\nv1 {0},v2 {1},v3 {2}'.format(v1,v2,v3))


if __name__=='__main__':
    unittest.main()

