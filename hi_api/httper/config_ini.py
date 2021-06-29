#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/6/29 1:46 下午
# @Author  : CrissChan
# @Site    : https://blog.csdn.net/crisschan
# @File    : config_ini.py
# @Software: 读取ini格式配置文件


import os
from configparser import ConfigParser, NoSectionError, NoOptionError


class ConfigFileParser(object):

    def __init__(self, file=None):
        """
        初始化
        :param file: 配置文件路径，默认为根路径下ini文件
        """
        self.configer = ConfigParser()
        self.file = file
        if not os.path.exists(file):
            raise FileNotFoundError("请确保配置文件存在！")
        try:
            self.configer.read(file, encoding='utf-8')
        except:
            # self.log.debug(get_err_code("20002"))
            print("文件不符合格式或字符集编码有问题")

    def get_value(self, title, key):
        """
        获取配置文件中的值
        :param title:
        :param key:
        :return:
        """
        # global config
        try:
            the_value = self.configer.get(title, key)
        except NoSectionError:
            print("title没有找到")
            the_value = "error"
        except NoOptionError:
            print("key没有找到")
            the_value = "error"
        return the_value

    def set_value(self, title, key, value):
        """
        设置配置文件中的键值
        :param title:
        :param key:
        :param value:
        :return:
        """
        # global config
        self.configer.set(title, key, value)

    def get_config_ini(self):
        file = os.path.join(os.getcwd(), "configer.ini")
        self.configer = ConfigParser()
        if not os.path.exists(file):
            raise FileNotFoundError("请确保配置文件存在！")
        try:
            self.configer.read(file, encoding='utf-8')
        except:

            print("文件不符合格式或字符集编码有问题")

    def write_config_ini(self, section, option, value):
        try:
            configer = self.configer
            configer.set(section, option, value)
            configer.write(open(self.file, "w", encoding='UTF-8'))
        except:
            print("更新ini文件失败！")
