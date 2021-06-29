# -*- encoding: utf-8 -*-
"""
@File    : parse_tools.py
@Time    : 2020/10/19 11:22
@Author  : liyinlong
@Software: PyCharm
"""

import os
import sys
import base64
import codecs
import case_generate
from hi_api.common import config_file_parser
import re


class Parse(object):

    @staticmethod
    def find_file(folder, formats):
        """
        查找指定目录指定文件格式文件
        :param folder: 文件夹路径
        :param formats: 文件名后缀
        :return: 文件路径list
        """
        file_list = []
        # root_path = str(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)))
        root_path=Parse.get_rootpath()
        file_path = os.path.join(root_path, folder)
        if not os.path.exists(file_path):
            os.makedirs(file_path)

        path_list = []
        f_list = os.listdir(file_path)
        try:
            for i in f_list:
                if os.path.splitext(i)[1] == '.' + str(formats.lower()):
                    file_list.append(i)
            for f in file_list:
                path = file_path + '/'+str(f)
                path_list.append(path)
            return path_list
        except:
            print('请确认temp文件夹下是否存在.%s 后缀文件！' % str(formats.lower()))
            sys.exit()

    @staticmethod
    def headers(data):
        """
        数据转成字典格式
        :param data:
        :return:
        """
        headers = {}
        for each in data:
            k, v = each.values()
            if k in ['Cookie']:
                continue
            headers.setdefault(k, v)
        return headers

    @staticmethod
    def post_data(post_data):
        """
        数据转成字典格式
        :param post_data:
        :return:
        """
        data = {}
        for each in post_data:
            k, v = each.values()
            data.setdefault(k, v)
        return data

    @staticmethod
    def post_data_key(request, t):
        """
        提取postData中的key
        :param request: 请求
        :param t: 该请求在请求列表中的位置
        :return: key list
        """
        key_list = []
        if 'postData' in request:
            if 'text' in request.get('postData'):
                body = request.get('postData').get('text')
                try:
                    body = eval(body)
                    key_list = list(body.keys())
                except(SyntaxError, ValueError):
                    print('提取key失败，请确认第 '+str(t)+' 个请求的postData中text格式！')
            else:
                body = request.get('postData').get('params')
                if body is not None:
                    for i in body:
                        key = i.get('name')
                        if key is not None:
                            key_list.append(key)
        return key_list

    @staticmethod
    def base64decode(text):
        """
        base64格式转码
        :param text:
        :return:
        """
        missing_padding = 4 - len(text) % 4
        if missing_padding:
            text += '=' * missing_padding
        return base64.b64decode(text).decode("utf-8")

    @staticmethod
    def path(path):
        """
        提取path后两段
        :param path:
        :return:
        """
        path_res = '_'.join(path.split('/')[-3:])
        return path_res

    @staticmethod
    def tmp(data, filename):
        """
        生成tmp格式临时文件
        :param data: tmp文件内容
        :param filename: tmp文件名
        """
        # root_path = str(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)))
        root_path = os.path.join(os.getcwd())
        file_path = root_path + '/temp/Tempdata'

        if not os.path.exists(file_path):
            os.makedirs(file_path)
        file = os.path.join(root_path, "temp/Tempdata", filename+'.tmp')
        with open(file, 'w', encoding="utf-8") as outfile:
            outfile.write(str(data))

    @staticmethod
    def read_tmp(tmpfile):
        """
        读取tmp文件
        :param tmpfile: tmp文件路径
        :return:
        """
        file = codecs.open(tmpfile, mode='r', encoding='utf-8-sig')
        data = eval(file.read())
        file.close()
        return data

    @staticmethod
    def tmp_create_case(type="0", path_lists=None):
        """
        temp\\Tempdata目录下tmp文件生成case
        :param type:
        :return:
        """
        root=Parse.get_rootpath()
        rootpath=os.path.join(root, 'temp/Tempdata')
        tmp_path_list = Parse.find_file(rootpath, 'tmp')
        for tmpfile in tmp_path_list:
            data = Parse.read_tmp(tmpfile)
            if type=="0":
                case_generate.Generate(data).case(path_lists)
            else:
                case_generate.Generate(data).case_dubbo()
            new_name = tmpfile + '_over'
            try:
                os.rename(tmpfile, new_name)
            except FileExistsError:
                os.remove(new_name)
                os.rename(tmpfile, new_name)

    @staticmethod
    def find_casefile(folder, f_list):
        """
        查找TestCase目录下面指定文件格式的文件
        :param folder：文件路径:
        :param formats: 文件名前缀
        :return: 查找到文件list
        """
        try:
            file_list1 = []
            for i in f_list:
                if not i.find('test_'):
                    file_list1.append(i)

            return  file_list1
        except:
            print('请确认TestCase文件夹下是否存在test 前缀文件！')
            sys.exit()

    @staticmethod
    def extract_key(contents_str):
        """
        查找TestCase目录下面
        :param folder：文件路径:
        :param formats: 文件名前缀
        :return: 查找到文件list
        """

        try:
            # list_key_dict={}
            pramlist = re.findall(r'{.*}', contents_str)
            list_key_dict = eval(pramlist[0].replace(': ', ': "').replace(',', '",').replace('}', '"}'))

            # print(list_key_dict)
            return list_key_dict
        except:
            print('请确认TestCase文件夹下是否存在testcase文件！')
            sys.exit()

    @staticmethod
    def get_rootpath():
        return os.path.join(os.getcwd())

    @staticmethod
    def get_global_value(self, excel_value, global_file):
        print("excel_value:", excel_value)
        print("global_conf:", global_file)
        global_conf = config_file_parser.ConfigFileParser(global_file)
        # 通过正则表达式，获取匹配到全局变量${}
        find_re = re.compile(r'(\${.*?\})', re.S)
        re_find = re.findall(find_re, excel_value)
        # 将全局变量值替换掉${}格式的字符串
        for value in re_find:
            if 'int' in global_conf.get_value('global', value.replace('${', '').replace('}', '')).split('&')[1].strip():
                 excel_value=excel_value.replace(value, global_conf.get_value('global',value.replace('${','').replace('}','')).split('&')[0].strip()).replace('\'','').replace('\"','')
                 print("if获取到的是：",excel_value)
            else:
                 excel_value=excel_value.replace(value, global_conf.get_value('global',value.replace('${','').replace('}','')).split('&')[0].strip())
                 print("else获取到的是：", excel_value)
        print("要return的是：", excel_value)
        return excel_value


# if __name__ == '__main__':
#     Parse.tmp('aaaa', 'test')




