#!/usr/bin/env python
# -*- coding: utf-8 -*-

#__from__ = 'hi_po_example'
#__title__='PyCharm'
#__author__ = 'crisschan'
#__mtime__ = '2018/2/12'
#__instruction__='存储参数的位置信息'

import sys
import  os
curPath = os.path.abspath('.')

#curPath = curPath[0:curPath.rfind('/')]

sys.path.append(curPath)
# 所有全局的参数都写在这个文件内

searchparam = curPath+'/test_case/param/searchparam.xls'

