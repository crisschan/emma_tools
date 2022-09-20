#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __from__ = 'hi_po'
# __author__ = 'CrissChan'
# __mtime__ = '2018/2/12'
# __instruction__=''

from selenium import webdriver
import unittest

class HiPOUnit(unittest.TestCase):
    '''
    modi this function delete lines param and the lines count in this function
    '''
    def __init__(self, methodName='HiPORunTest', param=None):
        super(HiPOUnit, self).__init__(methodName)
        self.param = param

    def setUp(self):
        self.verificationErrors = []
        self.accept_next_alert = True
        # 启动Chrome浏览器并且最大化
        self.driver = webdriver.Chrome('././driver/chromedriver')
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    # 关闭浏览器
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

    @staticmethod
    def TestCaseWithClass(testcase_class, param=None):
        '''
        Create a suite containing all tests taken from the given
            subclass, passing them the parameter 'param'.
        Modi this function delete lines param and the lines count in this function
        :param testcase_class: testcase类名
        :param param: 参数
        :return: null
        '''
        testloader = unittest.TestLoader()
        testnames = testloader.getTestCaseNames(testcase_class)
        suite = unittest.TestSuite()
        if param is not None:
            lines=len(param)
        else:
            lines=0
        i = 0
        while i < lines:
            for name in testnames:
                suite.addTest(testcase_class(name, param=param[i]))
            i = i + 1

        return suite

    @staticmethod
    def TestCaseWithFuncc(testcase_class, testcase_fun, param=None):
        '''
        Create a suite containing one test taken from the given
            subclass, passing them the parameter 'param'.
        Modi this function delete lines param and the lines count in this function

        :param testcase_class:  testcase类名
        :param testcase_func: 要执行的test_开头的函数名
        :param lines: 参数行数(参数文件有多少行参数
        :param param:
        :return: null
        '''
        suite = unittest.TestSuite()

        if param is not None:
            lines = len(param)
        else:
            lines = 0
        i = 0

        while i < lines:
            suite.addTest(testcase_class(testcase_fun, param=param[i]))
            i = i + 1
        return suite
