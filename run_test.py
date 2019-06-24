#!/usr/bin/env python
# -*- coding: utf-8 -*-

#__from__ = 'hi_po_example'
#__title__='PyCharm'
#__author__ = 'chancriss'
#__mtime__ = '2018/2/12'
#__instruction__=''
from hi_po import report
from hi_po import ParamFactory
from hi_po import HiPOUnit
from hi_po import Report
from hi_po import Sendmail
from test_case import reportTitle
from test_case import reportDescription
from test_case import reportDir
from test_case import TestSearch
from test_case.config.config_param import searchparam
import unittest

searchparam = ParamFactory().chooseParam('xls',{'file':searchparam,'sheet':0}).paramAlllineDict()

testSuite = unittest.TestSuite()
testSuite.addTests(HiPOUnit.TestCaseWithClass(TestSearch,param = searchparam))
Report(testSuite, reportDir, titleReport=reportTitle,descriptionReport=reportDescription)
#Sendmail(reportDir)
