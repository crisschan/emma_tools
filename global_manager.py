#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2020/8/24 2:54 下午
# @Author  : CrissChan
# @From    ：https://github.com/crisschan/
# @Site    : https://blog.csdn.net/crisschan
# @File    : global_manager.py
# @Intro   : 项目级的全局变量管理器，通过global定义全局字典，完成项目的全局变量的定义
#            使用方法在对应的文件中：
#               import global_manager as glob
#               glob._init()  # 先必须在主模块初始化
#                # 定义跨模块全局变量
#               glob.set_value('sessionid', sessionid)
#           在使用全局变量的项目内的文件前中：
#               import global_manager as glob
#               sessionid=glob.get_value('sessionid')
#
#            这就达到了项目将全局变量的目的



def _init():
    '''
    初始化全局变量管理器
    :return:
    '''
    global _glo_dict
    _glo_dict = {}


def set_value(key, value):
    '''
    将全局变量存入全局变量管理器
    :param key: 全局变量的名字
    :param value: 全局变量的值
    :return:
    '''
    _global_dict[key] = value


def get_value(key):
    '''

    :param key: 全局变量的名字
    :return:
    '''
    try:
        return _global_dict[key]
    except KeyError as e:
        print(e)

