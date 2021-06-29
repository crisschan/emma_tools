#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    : analysis_jmx.py
@Time    : 2020/11/25 16:46
@Author  : Yu Tao
@Software: PyCharm
"""
import xml.etree.ElementTree as ET
from urllib.parse import urlparse
import parse_tools
import sys


class Jxm(object):

    def source(self, jmx_content):
        """
        生成测试用例
        :param jmx_content:
        :return:
        """
        try:
            swagger_json, path_list = self.format_data(jmx_content=jmx_content)
            parse_tools.Parse.tmp(swagger_json, 'a')
            parse_tools.Parse.tmp_create_case()
            # swagger_json参数表入参
            return path_list, swagger_json
        except Exception as ex:
            print('获取jmx文件数据失败！')
            print(ex)
            sys.exit()

    def format_data(self, jmx_content):
        """
        格式化数据，使其满足“用例生成”的调用要求
        :param jmx_content: 读出的jmx文件数据
        :return:
        """
        root = ET.fromstring(jmx_content)
        template_data = {"swagger": "2.0"}
        template_data.update({"basePath": ""})
        template_data.update({"paths": {}})
        path_list = []
        path = ""
        method = ""
        consumes_json = 0
        #更新json格式的情况：consumes字段赋值
        for HeaderManager in root.iter("HeaderManager"):
            content_type = 0
            for stringProp in HeaderManager.iter("stringProp"):
                if stringProp.attrib['name'] == 'Header.name' and stringProp.text == "Content-Type":
                    content_type = 1
                if content_type and stringProp.attrib['name'] == 'Header.value' and stringProp.text.find("application/json") != -1:
                    consumes_json = 1
        for HTTPSamplerProxy in root.iter("HTTPSamplerProxy"):
            consumes = []
            parameters = []
            boolProp_postBodyRaw = 0
            #获取接口中的path、method等
            for stringProp in HTTPSamplerProxy.iter("stringProp"):
                print(stringProp.tag, ":", stringProp.attrib)
                if stringProp.attrib['name'] == 'HTTPSampler.path' and stringProp.text is not None:
                    url = stringProp.text
                    path = urlparse(url).path
                    path_list.append(path)
                if stringProp.attrib['name'] == 'HTTPSampler.method' and stringProp.text is not None:
                    method = stringProp.text.lower()
            #解析jmeter的入参为：body data格式（<stringProp name="Argument.value">{&quot;username&quot;:&quot;yytest033&quot;,&quot;password&quot;:&quot;12345678&quot;}</stringProp>）
            if HTTPSamplerProxy.iter("boolProp"):
                for boolProp in HTTPSamplerProxy.iter("boolProp"):
                    if boolProp.attrib.get("name") == "HTTPSampler.postBodyRaw":
                        boolProp_postBodyRaw = 1
            if boolProp_postBodyRaw:
                for stringProp in HTTPSamplerProxy.iter("stringProp"):
                    if stringProp.attrib['name'] == 'Argument.value':
                        param_dict = eval(stringProp.text)
                        for param_key in param_dict.keys():
                            parameters.append({"name": param_key, "in": "body"})
            else:
                #解析jmeter的入参为：parameter格式
                for elementProp in HTTPSamplerProxy.iter("elementProp"):
                    if elementProp.attrib.get("elementType") == "HTTPArgument":
                        name = elementProp.attrib.get("name")
                        parameters.append({"name": name, "in":"body"})
            if consumes_json:
                consumes.append("application/json")
            template_data["paths"].update({path: {}})
            template_data["paths"][path].update({method: {"parameters": parameters, "consumes": consumes}})
        return template_data, path_list


# if __name__ == '__main__':
#     # with open('D:/yt/2message_api.jmx', 'r',encoding='utf-8') as f:
#     with open('D:/yt/Test Plan.jmx', 'r',encoding='utf-8') as f:
#         # print("=============================================")
#         # print(f.read())
#         # print("=============================================")
#         file_content = f.read()
#         Jxm().source(jmx_content=file_content)



