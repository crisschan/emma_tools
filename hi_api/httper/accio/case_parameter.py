# -*- encoding: utf-8 -*-
"""
@File    : case_parameter.py
@Time    : 2020/10/16 10:43
@Author  : liyinlong
@Software: PyCharm
"""

import json
import os
import xlwt
from accio import parse_tools


class Parameter(object):

    def __init__(self, data, excel_path=None):
        self.__data = data
        # self.root_path = str(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)))
        self.root_path = os.path.dirname(os.path.join(os.getcwd()))
        if excel_path is None:
            excel_path = self.root_path + '\\test_case.xls'
        self.excel_path = excel_path

    '''
    获取request的参数生成excel
    参数：url，method，headers，postData
    调用时需要传入excel保存路径
    '''

    def make_case_excel(self):
        # url_list = []
        request_list = []
        requests_list = []
        for each in self.__data:
            request = each.get('request')
            url = request.get('url')
            # if url in url_list:
            #     continue
            # url_list.append(url)
            request_list.append(url)
            method = request.get('method').lower()
            request_list.append(method)

            post_data = {}
            if method == "post":
                if 'params' in request['postData']:
                    post_data = parse_tools.Parse.post_data(request['postData']['params'])
                elif 'text' in request['postData']:
                    text = request['postData']['text']
                    try:
                        post_data = json.loads(text)
                    except:
                        post_data = text
            request_list.append(str(post_data))
            request_list = ['项目名称', '用例描述'] + request_list
            requests_list.append(request_list)
            headers = parse_tools.Parse.headers(request['headers'])
            request_list.append(str(headers))
            request_list = []
        excel_title = ['case_project', 'case_description', 'case_url', 'case_method', 'case_params', 'case_headers',
                          'real_key', 'expect_value', 'other']

        style = xlwt.XFStyle()
        alignment = xlwt.Alignment()
        alignment.wrap = 1
        alignment.vert = 0x01
        font = xlwt.Font()
        font.name = 'Times New Roman'
        font.bold = True
        font.color_index = 4
        font.height = 250
        style.font = font
        style2 = xlwt.XFStyle()
        style2.alignment = alignment

        f = xlwt.Workbook()
        sheet1 = f.add_sheet('case', cell_overwrite_ok=True)
        for wid in range(len(excel_title)):
            sheet1.col(wid).width = 7999

        for t in range(len(excel_title)):
            sheet1.write(0, t, excel_title[t], style)

        i = 1
        for data in requests_list:
            for j in range(len(data)):
                sheet1.write(i, j, data[j], style2)
            i = i + 1
        f.save(self.excel_path)


# if __name__ == '__main__':
#     from accio import har_analysis
#     data = har_analysis.Har().source()
#     Parse = Parameter(data)
#     Parse.make_case_excel()
