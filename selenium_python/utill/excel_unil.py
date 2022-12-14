#coding=utf-8
import xlrd
from xlutils.copy import copy

class  ExcelUntil():
    def __init__(self,excel_path=None,index=None):
        if excel_path==None:
            self.excel_path=r'D:\software\python\selenium_python\config\casedata.xls'
        else:
            self.excel_path=excel_path
        if index==None:
            index=0
        self.data=xlrd.open_workbook( self.excel_path)
        self.table=self.data.sheets()[index]
        #行数

    def get_data(self):
        result = []
        rows=self.get_lines()
        if rows!=None:
            for i in range():
                col=self.table.row_values(i)
                result.append(col)
            return result
        return None
            # print(col)
    #获取exxcel行数
    def get_lines(self):
        rows = self.table.nrows
        if rows>=1:
            return rows
        return None
    #获取单元格数据
    def get_col_value(self,row,col):
        if self.get_lines()>row:
            data = self.table.cell(row,col).value
            # print(data)
            return data
        return None
    #判断行数
    def has_next(self):
        pass

    #写入数据
    def write_value(self,row,value):
        read_value=xlrd.open_workbook(self.excel_path)
        write_data=copy(read_value)
        write_data.get_sheet(0).write(row,9,value)
        write_data.save(self.excel_path)





if __name__=='__main__':
    ex=ExcelUntil(r'D:\software\python\selenium_python\config\keyword.xls')
    ex.write_value(5,'test')
    print(ex.get_col_value(5,7))



