#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    : analysis_har.py
@Time    : 2020/10/13 14:21
@Author  : liyinlong
@Software: PyCharm
"""
import sys
from urllib.parse import urlparse
import parse_tools


class Har(object):

    def source(self, har_json):
        """
        生成测试用例
        :param har_json:
        :return:
        """
        try:
            swagger_json, path_list = self.format_data(har_json)
            parse_tools.Parse.tmp(swagger_json, 'a')
            parse_tools.Parse.tmp_create_case()
            # swagger_json参数表入参
            return path_list, swagger_json
        except Exception as ex:
            print('获取har文件数据失败！')
            print(ex)
            sys.exit()

    def format_data(self, har_json):
        """
        格式化数据，使其满足“用例生成”的调用要求
        :param har_json: 读出的har文件数据
        :return:
        """
        entries = har_json.get("log").get("entries")
        template_data = {"swagger": "2.0"}
        template_data.update({"basePath": ""})
        template_data.update({"paths": {}})
        consumes = []
        path_list = []
        for entrie in entries:
            request = entrie.get("request")
            method = request.get("method").lower()
            url = request.get("url")
            path = urlparse(url).path
            path_list.append(path)
            headers = request.get("headers")
            query_string = request.get("queryString")
            if headers:
                for head in headers:
                    if head.get("name") == "Content-Type":
                        consumes.append(head.get("value"))
            parameters = []
            if query_string:
                for query_data in query_string:
                    parameters.append({"name": query_data.get("name"), "in": "body"})
            post_data = request.get("postData")
            if post_data:
                text = post_data.get("text")
                for key in eval(text).keys():
                    parameters.append({"name": key, "in": "body"})
            template_data["paths"].update({path: {}})
            template_data["paths"][path].update({method: {"parameters": parameters, "consumes": consumes}})
            consumes = []
        return template_data, path_list

