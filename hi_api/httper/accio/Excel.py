# -*- coding: utf-8 -*-


'''
关于Excel表的操作
'''

import xlrd
from accio import logger


class Excel(object):
    def __init__(self):
        self.log = logger.MyLog()

    def get_excel_data(self, path, sheet_num=0):
        """
        :param path: Excel文件路径
        :param sheet_num: Sheet页码，默认值为0
        :return:
        """
        try:
            # 获取到book对象
            book = xlrd.open_workbook(path)
            # 获取sheet对象
            sheet = book.sheet_by_index(sheet_num)
            rows, cols = sheet.nrows, sheet.ncols
            l = []
            title = sheet.row_values(0)
        except:
            self.log.error('请检查Excel文件路径或Sheet页码是否正确！')
            print('请检查Excel文件路径或Sheet页码是否正确！')

        # 获取其他行
        for i in range(1, rows):
            # print(sheet.row_values(i))
            l.append(dict(zip(title, sheet.row_values(i))))
        return l
