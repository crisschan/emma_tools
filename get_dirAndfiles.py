#!/usr/bin/env python
# -*- coding: utf-8 -*-

#__from__ = 'PythonSpace'
#__title__='PyCharm'
#__author__ = 'chancriss'
#__mtime__ = '2017/10/9'
#__instruction__='获取各种目录文件'
import os
class DirAndFiles(object):
    def __init__(self):
        self.__list=[]
    def allFiles(self,sOrgDir):  # 传入存储的list
        '''

        Args:
            sOrgDir: 目录

        Returns:
            list：全部文件，包含子目录内的
        '''
        self.__list=[]
        for file in os.listdir(sOrgDir):
            file_path = os.path.join(sOrgDir, file)
            if os.path.isdir(file_path):
                self.files(file_path)
            else:
                self.__list.append(file_path)
        return self.__list

    def dirAndFiles(self,sOrgDir):
        '''

        Args:
            sOrgDir: 目录

        Returns:
            list[dict]:dict{'root':root,'dirs':dirs,'files':files},root是根目录、dirs root下的第一级子目录、files root下第一级文件

        '''
        self.__list=[]
        for root, dirs, files in os.walk(sOrgDir):
            self.__list.append({'root':root,'dirs':dirs,'files':files})
        return self.__list

    def filesWithFilter(self,sOrgDir,sEx):
        '''

        Args:
            sOrgDir: 目录
            sEx: 需要查找的扩展名

        Returns:
            list：符合扩展名的全部文件，包含子目录里面的
        '''
        self.__list=[]
        for root, dirs, files in os.walk(sOrgDir):
            for file in files:
                if os.path.splitext(file)[1] == sEx:
                    self.__list.append(os.path.join(root, file))
        return self.__list
if __name__=='__main__':
    df = DirAndFiles()
    #print df.files('/Users/chancriss/Downloads')
    #print df.dirfiles('/Users/chancriss/Downloads')
    #print df.filesfilter('/Users/chancriss/Downloads','.jpg')