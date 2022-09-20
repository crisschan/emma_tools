#!/usr/bin/env python
# -*- coding: utf-8 -*-

#__from__ = 'hi_po_example'
#__title__='PyCharm'
#__author__ = 'chancriss'
#__instruction__=''

import sys
import  os
# curPath = os.path.abspath('/root/script')
curPath = os.path.abspath('./')

#curPath = curPath[0:curPath.rfind('/')]

sys.path.append(curPath)
# 所有全局的参数都写在这个文件内

'''报告相关参数:报告文件的文件夹绝对地址(最后一层文件夹可以不存在):命名   系统功能(or 功能名称)_reportDir'''
'''            报告名称:命名    系统功能(or 功能名称)_titleReport'''
'''            报告描述:命名    系统功能(or 功能名称)_descriptionReport'''
reportDir = curPath+'/test_report/'
reportTitle = u'京东首页搜索测试'
reportDescription = u'搜索测试'