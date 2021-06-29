#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/5/19 10:02 上午
# @Author  : CrissChan
# @Site    : https://blog.csdn.net/crisschan
# @File    : timeout.py
# @Software: HTTP访问请求等待时间，等同于思考时间

import requests
from requests.adapters import HTTPAdapter
from retries import ReTriesHTTPAdapter
DEFAULT_TIMEOUT = 500 # 默认等待时间，也就是思考时间，单位seconds

class TimeoutHTTPAdapter(HTTPAdapter):
    def __init__(self, *args, **kwargs):
        self.timeout = DEFAULT_TIMEOUT
        if "timeout" in kwargs:
            self.timeout = kwargs["timeout"]
            del kwargs["timeout"]
        super().__init__(*args, **kwargs)

    def send(self, request, **kwargs):
        timeout = kwargs.get("timeout")
        if timeout is None:
            kwargs["timeout"] = self.timeout
        return super().send(request, **kwargs)


# if __name__ == '__main__':
#     http = requests.Session()
#
#     # 把配置复制给http和https请求
#     readapter = ReTriesHTTPAdapter(max_retries=3)
#     adapter = TimeoutHTTPAdapter(timeout=2.5)
#     http.mount("http://", adapter)
#     http.mount("http://", readapter)
#
#     # 使用全局等待时间2.5秒
#     response = http.get("https://blog.csdn.net/fadfadfadf")
#     # 不用全局等待时间，设置请求自己的等待时间10秒
#     response = http.get("https://blog.csdn.net/crisschan", timeout=10)
#
