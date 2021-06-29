import parse_tools
import sys


class Swagger(object):

    def source(self, swagger_json, path_lists=None):
        """
        生成测试用例
        :param swagger_json:
        :return:
        """
        try:
            parse_tools.Parse.tmp(swagger_json, 'a')
            parse_tools.Parse.tmp_create_case(type="0", path_lists=path_lists)
        except Exception as ex:
            print('获取swagger文件数据失败！')
            print(ex)
            sys.exit()
