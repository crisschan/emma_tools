#!/usr/bin/env python
# -*- coding: utf-8 -*-

from hi_po import HiPOUnit
from pages.search_page import SearchPage
from .config.config_uri import jd_uri,homeUri

class TestSearch(HiPOUnit):
    '''图书搜索测试用例'''
    def test_book(self):
        '''python图书搜索'''
        self.bookPage = SearchPage(self.driver,root_uri = jd_uri)
        self.bookPage.get(homeUri)
        self.bookPage.search_box = self.param['case']
        self.bookPage.search_buttom.click()
        self.bookPage.searchbox_input_exp = self.param['exp']
        self.bookPage.search_checkbox.click()
        self.search_result = self.bookPage.search_result.text
        self.assertEqual(self.search_result,self.bookPage.searchbox_input_exp,msg='书名不一致')
