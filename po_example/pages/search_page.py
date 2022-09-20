#!/usr/bin/env python
# -*- coding: utf-8 -*-
from hi_po import PageObject,PageElement

class SearchPage(PageObject):
    '''京东首页搜索'''
    search_box = PageElement(xpath='//*[@id="key"]')
    search_buttom = PageElement(xpath='//*[@id="search"]/div/div[2]/button/i')
    search_checkbox = PageElement(xpath='//*[@id="J_feature"]/ul/li[1]/a/i')
    search_result = PageElement(xpath = '//*[@id="J_goodsList"]/ul/li[1]/div/div[3]/a/em/font')




class PlayPage(PageObject):
    '''课程播放页'''
    search_buttom = PageElement(xpath='//*[@id="search"]/div/div[2]/button/i')
    user_name_txt = PageElement(xpath='//*[@id="key"]')
    password_txt = PageElement(xpath='//*[@id="search"]/div/div[2]/button/i')
    login_but = PageElement(xpath='//*[@id="J_feature"]/ul/li[1]/a/i')
    search_box = PageElement(xpath='//*[@id="key"]')
    search_result = PageElement(xpath='//*[@id="J_goodsList"]/ul/li[1]/div/div[3]/a/em/font')
    search_checkbox = PageElement(xpath='//*[@id="J_feature"]/ul/li[1]/a/i')
