#!/usr/bin/env python
# -*- coding: utf-8 -*-
from hi_po import PageObject,PageElement

class SearchPage(PageObject):
    '''京东首页搜索'''
    search_box = PageElement(xpath='//*[@id="key"]')
    search_buttom = PageElement(xpath='//*[@id="search"]/div/div[2]/button/i')
    search_checkbox = PageElement(xpath='//*[@id="J_feature"]/ul/li[1]/a/i')
    search_result = PageElement(xpath = '//*[@id="J_goodsList"]/ul/li[1]/div/div[3]/a/em/font')
