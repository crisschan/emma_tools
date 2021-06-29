# -*- encoding: utf-8 -*-
"""
@File    : analysis_openapi.py
@Time    : 2020/11/25 16:46
@Author  : Yu Tao
@Software: PyCharm
"""
import parse_tools
import yaml,sys

class OpenapiF(object):

    def __init__(self):
        self.path_list = parse_tools.Parse.find_file('temp', 'yaml')

    def source(self):
        try:
            for path in self.path_list:
                openapi = open(path, mode='r', encoding='utf-8')
                ojson = yaml.load(openapi, Loader=yaml.FullLoader)

                print (ojson)
                filename = path.split("\\")[-1].split('.')[0]
                data = {}
                data["request"] = {}
                print(ojson.get("servers")[0].get("url"))
                data["request"].update({"headers": []})
                data["request"].update({"bodySize":""})
                data["request"].update({"cookies":[]})
                for apath in ojson.get("paths").keys():
                    data["request"].update({"url": ojson.get("servers")[0].get("url") + apath})
                # data["request"].update({"method": ojson["request"]["method"]})
                data["request"].update({"httpVersion": ""})
                parse_tools.Parse.tmp(data, filename)
                openapi.close()
        except:
            print('获取openapi文件数据失败！')
            sys.exit()


# if __name__ == '__main__':
#
#     p = OpenapiF()
#     p.source()
#     Parse.source()
#     # tmp文件生成case
#     parse_tools.Parse.tmp_create_case()