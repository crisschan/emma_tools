# -*- encoding: utf-8 -*-
import parse_tools
import sys


class DubboCase(object):

    def source(self, swagger_json):
        """
        生成测试用例
        :param swagger_json:
        :return:
        """
        try:
            parse_tools.Parse.tmp(swagger_json, 'a')
            parse_tools.Parse.tmp_create_case(type="1")
            # print("=============dubbo")
        except Exception as ex:
            print('获取dubbo文件数据失败！')
            print(ex)
            sys.exit()
