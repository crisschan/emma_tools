# @Time : 2020/11/4 10:09 

# @Author : Cuiluming

# @File : locust_read_parameterfile.py

# @Software: PyCharm
# 读取表
from xlrd import xldate_as_tuple
from datetime import datetime
import xlrd
import os
import accio.locust_run


class file_analysis(object):
    @staticmethod
    def creatparm(project_name,loadfile):
            root_path = os.path.join(os.getcwd())
            book = xlrd.open_workbook(os.path.join(str(root_path),'projects',project_name,'Params', 'Excel',loadfile))
            # 获取第一个sheet页
            sheet1 = book.sheets()[0]
            # 获取总行数
            rows = sheet1.nrows
            # 获取总列数
            cols = sheet1.ncols
            col_dict = {}
            for i in range(sheet1.ncols):
                col_dict[sheet1.cell_value(0, i)] = i
            # print(col_dict.keys())
            # 输出每一列数据
            all_content = []
            for i in range(cols):
                col_content = []
                j = 1
                for j in range(rows):
                    ctype = sheet1.cell(j, i).ctype  # 表格的数据类型
                    # ctype = sheet1.cell(i, j).ctype
                    cell = sheet1.cell_value(j, i)  # 取第i列第j行数据
                    if ctype == 2 and cell % 1 == 0:  # 如果是整形
                        cell = int(cell)
                    elif ctype == 3:  # 如果是日期型
                        # 转成datetime对象
                        date = datetime(*xldate_as_tuple(cell, 0))
                        cell = date.strftime('%Y/%d/%m %H:%M:%S')
                    elif ctype == 4:  # 如果是boolean型
                        cell = True if cell == 1 else False
                    elif ctype==1:# 如果是str
                        cell=cell
                    col_content.append(cell)
                all_content.append(col_content)
            # print(all_content)
            new_dict = {}
            listkey = []
            for key in col_dict.items():
                listkey.append(list(key))
            count = 0
            for i in all_content:
                tem_list = []
                for j in i[1:]:
                    tem_list.append(j)
                new_dict[listkey[count][0]] = tem_list
                count += 1
            return new_dict


# if __name__ == '__main__':
#     f=file_analysis()
#     f.creatparm(loadfile="loadfile.xlsx")