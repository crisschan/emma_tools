#!/usr/bin/env python
# -*- coding: utf-8 -*-

#__from__ = 'PythonSpace'
#__title__='PyCharm'
#__author__ = 'chancriss'
#__mtime__ = '2017/8/30'
#__instruction__='urldecode and urlencode: from urlcode import uriencode or from urlcode import uridecode'

from urllib import urlencode,quote,unquote

def uriencode(sInput):
    '''
    Args:
        sInput: 输入的是一个string or a dict

    Returns:
        url encode

    '''
    if type(sInput)==dict:
        return urlencode(sInput)
    else:
        return quote(sInput)

def uridecode(sInput):
    '''

    Returns: url decode

    '''
    return unquote(sInput)