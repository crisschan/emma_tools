#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2020/5/20 1:56 下午
# @Author  : CrissChan
# @Site    : https://blog.csdn.net/crisschan
# @File    : zip_memless.py
# @Intro   ：低内存压缩



import zipfly



class ZipMemless(object):

    def __init__(self,paths,out_zip):
        '''

        :param paths: # paths = [{
                                     'fs': 'home/user/Videos/jupiter.mp4',被压缩文件物理位置1
                                     'n': 'movies/jupiter.mp4'在压缩包中的全路径1
                                },{
                                    'fs': 'home/user/Documents/mercury.mp4',被压缩文件物理位置2
                                    'n': 'movies/mercury.mp4'在压缩包中的全路径2
                                }]
        :param out_zip: 输出文件.zip的全路径
        '''
        self.paths=paths
        self.out_zip = out_zip
        self.out_zip(self.paths,self.out_zip)

    def __zip(self):
        zfly = zipfly.ZipFly(paths=paths)
        generator = zfly.generator()
        with open("test.zip", "wb") as f:
            for i in generator:
                f.write(i)

