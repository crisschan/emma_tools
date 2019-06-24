#!/usr/bin/env python
# -*- coding: utf-8 -*-

#__from__ = 'hi_po_example'
#__title__='PyCharm'
#__author__ = 'chancriss'
#__instruction__=''

import json
import xlrd
class Param(object):
    def __init__(self,paramConf='{}'):
        self.paramConf = json.loads(paramConf)

    def paramRowsCount(self):
        pass
    def paramColsCount(self):
        pass
    def paramHeader(self):
        pass
    def paramAllline(self):
        pass
    def paramAlllineDict(self):
        pass



class XLS(Param):
    '''
    xls基本格式(如果要把xls中存储的数字按照文本读出来的话,纯数字前要加上英文单引号:
    第一行是参数的注释,就是每一行参数是什么
    第二行是参数名,参数名和对应模块的po页面的变量名一致
    第3~N行是参数
    最后一列是预期默认头Exp
    '''

    def __init__(self, paramConf):
        '''
        :param paramfile: xls 文件位置(绝对路径)
        '''
        self.paramConf = paramConf
        self.paramfile = self.paramConf['file']
        self.data = xlrd.open_workbook(self.paramfile)
        self.getParamSheet(self.paramConf['sheet'])


    def getParamSheet(self,nsheets):
        '''
        设定参数所处的sheet
        :param nsheets: 参数在第几个sheet中
        :return:
        '''
        self.paramsheet = self.data.sheets()[nsheets]
    def getOneline(self,nRow):
        '''
        返回一行数据
        :param nRow: 行数
        :return: 一行数据 []
        '''

        return self.paramsheet.row_values(nRow)


    def getOneCol(self,nCol):
        '''
        返回一列
        :param nCol: 列数
        :return: 一列数据 []
        '''
        return self.paramsheet.col_values(nCol)
    def paramRowsCount(self):
        '''
        获取参数文件行数
        :return: 参数行数 int
        '''
        return self.paramsheet.nrows
    def paramColsCount(self):
        '''
        获取参数文件列数(参数个数)
        :return: 参数文件列数(参数个数) int
        '''
        return self.paramsheet.ncols
    def paramHeader(self):
        '''
        获取参数名称
        :return: 参数名称[]
        '''
        return self.getOneline(1)
    def paramAlllineDict(self):
        '''
        获取全部参数
        :return: {{}},其中dict的key值是header的值
        '''
        nCountRows = self.paramRowsCount()
        nCountCols = self.paramColsCount()
        ParamAllListDict = {}

        iRowStep = 2
        iColStep = 0
        ParamHeader= self.paramHeader()

        while iRowStep < nCountRows:
            ParamOneLinelist=self.getOneline(iRowStep)
            ParamOnelineDict = {}
            while iColStep<nCountCols:
                ParamOnelineDict[ParamHeader[iColStep]]=ParamOneLinelist[iColStep]
                iColStep=iColStep+1
            iColStep=0
            #print ParamOnelineDict
            ParamAllListDict[iRowStep-2]=ParamOnelineDict
            iRowStep=iRowStep+1
        return ParamAllListDict

    def paramAllline(self):
        '''
        获取全部参数
        :return: 全部参数[[]]
        '''
        nCountRows= self.getCountRows()
        paramall = []
        iRowStep =2
        while iRowStep<nCountRows:
            paramall.append(self.getOneline(iRowStep))
            iRowStep=iRowStep+1
        return paramall
    def __getParamCell(self,numberRow,numberCol):
        return self.paramsheet.cell_value(numberRow,numberCol)


class ParamFactory(object):
    def chooseParam(self,type,paramConf):
        map_ = {
            'xls': XLS(paramConf)
        }
        return map_[type]

'''
if __name__=='__main__':
    param = ParamFactory().chooseParam('xls',{'file':'searchkeyword.xls','sheet':0})
    print param.paramAlllineDict()'''