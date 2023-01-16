#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2020/5/30 10:23 上午
# @Author  : CrissChan
# @Site    : https://blog.csdn.net/crisschan
# @File    : remove.py
# @Intro   : 删除文件或者目录

import os
import shutil

class Remover(object):
    @classmethod
    def dir(cls,rm_root):
        '''
        递归删除目录以及目录内的所有内容.
        :param root:删除目录

        :return:
        '''
        for root, dirs, files in os.walk(rm_root, topdown=False):
            for name in files:
                os.remove(os.path.join(root, name))
            for name in dirs:
                os.rmdir(os.path.join(root, name))
        os.removedirs(rm_root)
    @classmethod
    def dir_under(cls,rm_root):
        '''

        :param rm_root:删除目录下所有的文件，目录不删除存在
        :return:
        '''

        shutil.rmtree(rm_root)
    @classmethod
    def file(cls,rm_file):
        '''
        删除文件
        :param root:删除文件路径
        :return:
        '''
        if os.path.exists(rm_file):
            os.unlink(rm_file)
    @classmethod
    def dir_empty(cls,rm_root):
        '''
        递归删除目录，如果有一个目录非空则会抛出异常
        :param rm_root: 删除目录
        :return:
        '''
        if os.path.exists(rm_root):
            os.removedirs(rm_root)


