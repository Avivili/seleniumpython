#coding=utf-8
from utill.excel_unil import ExcelUntil
# import sys
# sys.path.append()
from keywordselenium.actionMethod import ActionMethod
class KeywordCase():
    def run_main(self):
        self.action_method = ActionMethod()
        handle_excel=ExcelUntil(r'D:\software\python\selenium_python\config\keyword.xls')
        case_lines=handle_excel.get_lines()
        if case_lines:
            for i in range(1,case_lines):
                handle_excel.write_value(i,'test')
                is_run=handle_excel.get_col_value(i,3)
                if is_run=='yes':
                    method = handle_excel.get_col_value(i, 4)
                    send_value = handle_excel.get_col_value(i, 5)
                    hand_value = handle_excel.get_col_value(i, 6)
                    expect_result_method=handle_excel.get_col_value(i,7)
                    expect_result=handle_excel.get_col_value(i,8)
                    # if send_value:
                    self.run_method(method,send_value,hand_value)
                    if expect_result!='':

                        expect_value=self.get_expect_result_value(expect_result)
                        print(expect_value)
                        if expect_value[0]=='text':
                            result=self.run_method(expect_result_method)
                            print(result)
                            if expect_value[1] in result:
                                handle_excel.write_value(i,'pass')
                            else:
                                handle_excel.write_value(i, 'fail')
                        elif expect_value[0]=='element':

                            result=self.run_method(expect_result_method,expect_value[1])
                            if result:
                                handle_excel.write_value(i,'pass')
                            else:
                                handle_excel.write_value(i,'fail')
                        else:
                            print('没有else')

                    else:
                        print('预期结果为空')



    #获取预期结果值
    def get_expect_result_value(self,data):
        return data.split('=')

    def run_method(self,method,send_value='',handle_value=''):

        method_value=getattr(self.action_method,method)
        print(method_value)
        if send_value !='' and handle_value!='':
           result= method_value(send_value,handle_value)

        elif send_value=='' and handle_value!='':
            result=method_value(handle_value)
        elif send_value!='' and handle_value=='':
            result=method_value(send_value)
        else:
            result=method_value()
        # print(result,'run_method')
        return result




        #拿到行数
        #循环行数，执行
        #是否执行
            #拿到执行方法
            #拿到操作值
        #拿到输入数据
if __name__=='__main__':
    keywds=KeywordCase()
    keywds.run_main()

