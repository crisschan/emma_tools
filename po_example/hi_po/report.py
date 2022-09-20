#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __from__ = 'hi_po'
# __instruction__='for  test report'
from .HTMLTestRunner_cn import HTMLTestRunner
import time
import os


class Report(object):
    def __init__(self, testSuite, dirReport, titleReport='default', descriptionReport='default'):
        '''
        :param testSuite: testSuite Object
        :param dirReport:  the test result file location
        :param titleReport:  the report title  name
        :param descriptionReport: the test report description
        '''
        try:

            if not os.path.exists(dirReport):
                os.mkdir(dirReport)
            strTimeStamp = time.strftime('%Y%m%d%H%M%S')
            titleReport = titleReport + strTimeStamp  # 修改成YYMMDD HH:MM:SS
            descriptionReport = descriptionReport + strTimeStamp
            filename = dirReport + titleReport + '.html'
            fp = open(filename, 'wb')
            runner = HTMLTestRunner(fp, title=titleReport, description=descriptionReport)
            runner.run(testSuite)
            fp.close()
        except Exception:
            print("please input testCase,report file's location!")
