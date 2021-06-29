#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/6/29 1:39 下午
# @Author  : CrissChan
# @Site    : https://blog.csdn.net/crisschan
# @File    : __init__.py.py
# @Software: PyCharm
from retries import ReTriesHTTPAdapter
from config_ini import ConfigFileParser
from requests_toolbelt import sessions
from config_ini import ConfigFileParser


class httper(sessions.BaseUrlSession):
    def __init__(self,base_url=None):
        cf = ConfigFileParser('../config.ini')
        self.base_url=cf.get_value('baseurl','baseurl')
        super().__init__()
        self.http_retries()


    def http_retries(self):
        readapter = ReTriesHTTPAdapter(max_retries=3)
        return super().mount("http://",readapter)




