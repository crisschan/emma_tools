#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/6/29 1:39 下午
# @Author  : CrissChan
# @Site    : https://blog.csdn.net/crisschan
# @File    : __init__.py.py
# @Software: 创建一个更适合测试使用的http协议类


from requests_toolbelt import sessions
from requests.adapters import HTTPAdapter
from .CONFIG import MAX_RETRIES,DEFAULT_TIMEOUT

class ReTriesHTTPAdapter(HTTPAdapter):
    """设置HTTP失败重跑次数类"""
    def __init__(self,*arg,**kwargs):
        """
        设置HTTP失败重跑次数类，重跑次数MAX_RETRIES在CONFIG里面设置
        """
        if "max_retries" not in kwargs:
            kwargs["max_retries"]= MAX_RETRIES
        super().__init__(*arg,**kwargs)



class TimeoutHTTPAdapter(HTTPAdapter):
    """HTTP访问请求等待时间，等同于思考时间"""
    def __init__(self, *args, **kwargs):
        self.timeout = DEFAULT_TIMEOUT
        if "timeout" in kwargs:
            self.timeout = kwargs["timeout"]
            del kwargs["timeout"]
        super().__init__(*args, **kwargs)

    def send(self, request, **kwargs):
        timeout = kwargs.get("timeout")
        if timeout is None:
            kwargs["timeout"] = DEFAULT_TIMEOUT
        return super().send(request, **kwargs)

class Httper(sessions.BaseUrlSession):
    def __init__(self,base_url):

        self.base_url=base_url
        super(Httper, self).__init__(base_url=base_url)
        self.__retries()
        self.__timeout()
    def __retries(self):
        """
        设置失败重跑次数，如果本次http请求失败了，重试次
        """
        readapter = ReTriesHTTPAdapter()
        return super().mount("http://",readapter)
    def __timeout(self):
        """
        设置请求超市时间，和测试中的thinktime一样
        """
        tadapter = TimeoutHTTPAdapter()
        return super(Httper, self).mount("http://",tadapter)
    def get_cookies(self):
        return self.cookies
