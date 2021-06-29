#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    : case_generate.py
@Time    : 2020/10/16 10:39
@Author  : liyinlong
@Software: PyCharm
"""

import time
import os, re


class Generate(object):

    def __init__(self, data, case_name=None):
        self.data = data
        self.case_name = case_name

        #self.root_path = str(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)))
        self.root_path = os.path.join(os.getcwd())
        if not os.path.exists(str(self.root_path) + '\\temp\\Testcase'):
            os.makedirs(str(self.root_path) + '\\temp\\Testcase')

    '''
    依据har文件method信息生成对应case
    如果传入文件名以传入文件名+数据在entries中的位置命名
    不传入文件名默认以path路径命名，截取path后两段命名
    如果没有path路径，以域名命名
    '''

    def case(self, path_lists=None):
        list = []
        method = ''
        keys = ''
        dump = ''
        print(self.data)
        base_path = ""
        bk = 4 * " "
        for t, each in enumerate(self.data):
            print("*********************each:**********************:", each)
            print("*********************self.data.get(each):**********************:", self.data.get(each))
            # 取出basePath
            if each == "basePath":
                if self.data.get(each) != "/":
                    base_path = self.data.get(each)
            print("------base_path------:", base_path)
            list.append(each)
        paths = self.data.get('paths')
        local_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        print("****************self.data.get('paths')*****************",self.data.get('paths'))
        for t, each in enumerate(paths):
            print("**********************each:*********************:", each)
            if path_lists and each not in path_lists:
                continue
            else:
                for n, m in enumerate(paths.get(each)):
                    method = m          # 取出请求方法
                    for c, cons in enumerate(paths.get(each).get(m)):
                        if cons == 'consumes':
                            if 'application/json' in str(paths.get(each).get(m).get('consumes')):
                                dump = 'params = json.dumps(params)'
                            else:
                                dump = ''
                parameters = paths.get(each).get(method).get('parameters')
                each = base_path + each
                # print("=========================拼接basePath后的path:========================", each)
                if '{' in each and each[-1]=='}':    # 判断路径里是否有大括号，来拼接response内容
                    req = method.lower() + '(host+\"' + each.replace('{', '\"+ ').replace('}', ' +\"')[:-2] + ', params, header)'
                elif '{' in each and each[-1]!='}':
                    req = method.lower() + '(host+\"' + each.replace('{', '\"+ ').replace('}', ' +\"') + '/\", params, header)'
                else:
                    req = method.lower() + '(host+\"' + each + '\", params, header)'

                each = each.replace('{', '').replace('}', '')
                case_file_name = 'test' + each.replace('/', '_') + '.py'
                print("----------------case_generate-------------case_file_name:", case_file_name)
                key = []
                param_in_paths = []
                param_in_paths_value = []
                param_in_header = []
                param_in_header_value = []
                if 'securityDefinitions' in list:     # 判断securityDefinitions里是否有参数
                    if self.data.get('securityDefinitions'):
                        for a, b in enumerate(self.data.get('securityDefinitions')):
                            if self.data.get('securityDefinitions').get(b).get('name'):
                                in_where = self.data.get('securityDefinitions').get(b).get('in')
                                if in_where == 'body':
                                    param_in_paths.append(self.data.get('securityDefinitions').get(b).get('name'))
                                    key.append(re.sub(' +', '_',self.data.get('securityDefinitions').get(b).get('name').replace('-', '_')))
                                elif in_where == 'header':
                                    param_in_header.append(self.data.get('securityDefinitions').get(b).get('name'))
                                    key.append(re.sub(' +', '_',self.data.get('securityDefinitions').get(b).get('name').replace('-', '_')))
                                else:
                                    print("securityDefinitions类型异常")
                dict_param_inpath = ''
                dict_param_inheader = ''
                print("parameters-----------------------:", parameters)
                if parameters:
                    for num, param in enumerate(parameters):    # 将参数分别放进 params 和 header
                        name = ''
                        if param.get('name'):
                            name = param.get('name')
                            key.append(re.sub(' +', '_', name.replace('-', '_')))
                            keys = ', '.join(key)
                        if param.get('in'):
                            in_wh = param.get('in')
                        if in_wh == 'body':
                            param_in_paths.append(name)
                            param_in_paths_value.append(re.sub(' +', '_',name.replace('-', '_')))
                            dict_param_inpath = str(dict(zip(param_in_paths, param_in_paths_value))).replace(': \'',': ').replace('\',',',').replace('\'}','}')
                            if dict_param_inpath == "{'': }":
                                dict_param_inpath = "{}"
                        elif in_wh == 'header':
                            param_in_header.append(name)
                            param_in_header_value.append(re.sub(' +', '_',name.replace('-', '_')))
                            dict_param_inheader = "header.update(" + str(dict(zip(param_in_header, param_in_header_value))).replace(': \'',': ').replace('\',',',').replace('\'}','}') + ')'
                            if dict_param_inheader == "header.update({'': })":
                                dict_param_inheader = "header.update({})"
                        else:
                            pass
                else:
                    pass
                if dict_param_inpath == '':
                    dict_param_inpath = '{}'
                if keys:
                    keys = ', ' + keys + ','
                else:
                    keys = ','
                file_write = os.path.join(self.root_path, "TestCase", case_file_name)
                print("------------file_write----------------:", file_write)
                with open(file_write, 'w', encoding="utf-8") as outfile:
                    outfile.write("\"\"\"" + "\r")
                    outfile.write("@File    : %s" % case_file_name + "\r")
                    outfile.write("@Time    : %s" % local_time + "\r")
                    outfile.write("@Author  : Automatic generation" + "\r")
                    outfile.write("\"\"\"" + "\r")
                    outfile.write("#--别名占位" + "\r\r")
                    outfile.write("from accio import Http" + "\r\r\r")
                    outfile.write("import json" + "\r")
                    outfile.write("class Case:" + "\r\r")
                    outfile.write(bk + "def __init__(self):" + "\r")
                    outfile.write(2*bk + "self.request = Http.Request()" + "\r\r")
                    outfile.write(bk + "def request_method(self, host%s headers):" % keys + "\r")
                    outfile.write(2*bk + "\"\"\"")
                    outfile.write(3*bk + "用例描述：数据源文件中第 %s 个request" % str(t + 1) + "\r")
                    outfile.write(2*bk + "\"\"\"" + "\r")
                    outfile.write(2*bk + "params = %s" % dict_param_inpath + "\r")
                    outfile.write(2*bk + dump + "\r")
                    outfile.write(2*bk + "if not headers:" + "\r")
                    outfile.write(3*bk + "headers='{}'" + "\r")
                    outfile.write(2*bk + "header = eval(headers)" + "\r")
                    outfile.write(2*bk + "%s" % dict_param_inheader + "\r")
                    outfile.write(2*bk + "response = self.request.%s" % req + "\r")
                    outfile.write(2*bk + "return response" + "\r")
                    keys = ''

    def case_dubbo(self):
        """
        生成dubbo测试步骤文件
        :return:
        """
        lista = ["1"]
        bk = 4*" "
        for a in lista:
            local_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            # case_file_name = 'test' + each.replace('/', '_') + '.py'
            case_file_name = 'test001' + '.py'
            file_write = os.path.join(self.root_path, "TestCase", case_file_name)
            with open(file_write, 'w', encoding="utf-8") as outfile:
                outfile.write("\"\"\"" + "\r")
                outfile.write("@File    : %s" % case_file_name + "\r")
                outfile.write("@Time    : %s" % local_time + "\r")
                outfile.write("@Author  : Automatic generation" + "\r")
                outfile.write("\"\"\"" + "\r")
                outfile.write("#--别名占位" + "\r\r")
                outfile.write("from pyhessian.client import HessianProxy" + "\r")
                outfile.write("from pyhessian import protocol" + "\r\r\r")
                outfile.write("class Case(object):" + "\r\r")
                outfile.write(bk + "def request_method(url, interface, method, param_obj, **kwargs):" + "\r")
                outfile.write(2*bk + "req_param = protocol.object_factory(param_obj, **kwargs)" + "\r")
                outfile.write(2*bk + "req_obj = HessianProxy(url + interface)" + "\r")
                outfile.write(2*bk + "res = getattr(req_obj, method)(req_param)" + "\r")
                outfile.write(2*bk + "return res" + "\r")



# if __name__ == '__main__':
#     Generate("data").case_dubbo()