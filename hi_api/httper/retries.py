#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/5/19 10:06 上午
# @Author  : CrissChan
# @Site    : https://blog.csdn.net/crisschan
# @File    : retries.py
# @Software: HTTP访问失败后的重试次数
import requests
from requests.adapters import HTTPAdapter
from ..CONFIG import MAX_RETRIES

class ReTriesHTTPAdapter(HTTPAdapter):
    def __init__(self,*arg,**kwargs):
        if "max_retries" not in kwargs:
            kwargs["max_retries"]= MAX_RETRIES
        super().__init__(*arg,**kwargs)

