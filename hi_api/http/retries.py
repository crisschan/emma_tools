#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/5/19 10:06 上午
# @Author  : CrissChan
# @Site    : https://blog.csdn.net/crisschan
# @File    : retries.py
# @Software: HTTP访问失败后的重试次数

import requests
from requests.adapters import HTTPAdapter
DEFAULT_MAX_RETRIES = 3 # 默认重试时间，单位次

class ReTriesHTTPAdapter(HTTPAdapter):
    def __init__(self,*arg,**kwargs):
        if "max_retries" not in kwargs:
            kwargs["max_retries"]= DEFAULT_MAX_RETRIES
        super().__init__(*arg,**kwargs)


# if __name__ == '__main__':
#
#     http = requests.Session()
#
#     # 把配置复制给http和https请求
#     readapter  = ReTriesHTTPAdapter(max_retries=3)
#     http.mount("http://",readapter)
#
#     # 使用全局等待时间2.5秒
#     response = http.get("https://blog.csdn.net/fadfadfadf")
#     print(response.text)
#     # 不用全局等待时间，设置请求自己的等待时间10秒
#     response = http.get("https://blog.csdn.net/crisschan", timeout=10)
#
#     print(response.text)