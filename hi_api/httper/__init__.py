#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/6/29 1:39 下午
# @Author  : CrissChan
# @Site    : https://blog.csdn.net/crisschan
# @File    : __init__.py.py
# @Software: PyCharm
import requests
from retries import ReTriesHTTPAdapter
from requests_toolbelt import sessions
from ..CONFIG import BASE_URL
class httper(sessions.BaseUrlSession):
    def __init__(self,base_url=BASE_URL):
        self.base_url=base_url
        super(httper, self).__init__(base_url=base_url)
        self.http_retries()
    def http_retries(self):
        readapter = ReTriesHTTPAdapter()
        return super().mount("http://",readapter)



# if __name__ == '__main__':
#     cf = ConfigFileParser('../config.ini')
#     base_url = cf.get_value('baseurl', 'baseurl')
#
#     h =httper(base_url=base_url)
#     a = h.get('/category_1404515.html')
#     print(a.headers)
