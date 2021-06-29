#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    : analysis_postmanjson.py
@Time    : 2020/10/19 9:40
@Author  : Yu Tao
@Software: PyCharm
"""
import sys
import parse_tools
from urllib.parse import urlparse


class Postman(object):

    def source(self, postman_json):
        """
        生成测试用例
        :param postman_json:
        :return:
        """
        try:
            swagger_json, path_list = self.format_data(postman_json)
            parse_tools.Parse.tmp(swagger_json, 'a')
            parse_tools.Parse.tmp_create_case()
            # swagger_json参数表入参
            return path_list, swagger_json
        except Exception as ex:
            print('获取postman文件数据失败！')
            print(ex)
            sys.exit()

    def format_data(self, postman_json):
        """
        格式化数据，使其满足“用例生成”的调用要求
        :param file_context: 读出的json文件数据
        :return:
        """
        template_data = {"swagger": "2.0"}
        template_data.update({"basePath":""})
        template_data.update({"paths":{}})
        consumes = []
        path_list = []
        if isinstance(postman_json, dict):
            item_list = postman_json.get("item")
            for item in item_list:
                request = item.get("request")
                method = request.get("method").lower()
                header = request.get("header")
                if header:
                    for header_content in header:
                        if header_content.get("key") == "Content-Type":
                            consumes.append(header_content.get("value"))
                url = request.get("url")
                path = urlparse(url.get("raw")).path
                path_list.append(path)
                parameters = []
                if request.get("body"):
                    if eval(request.get("body").get("raw")).keys():
                        for key in eval(request.get("body").get("raw")).keys():
                            parameters.append({"name":key, "in":"body"})
                if url.get("query"):
                    for para in url.get("query"):
                        parameters.append({"name":para.get("key"), "in":"body"})
                template_data["paths"].update({path:{}})
                template_data["paths"][path].update({method:{"parameters":parameters, "consumes":consumes}})
        return template_data, path_list

