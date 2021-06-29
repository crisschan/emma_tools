# coding=utf8
# !/usr/bin/env python
# __author_='crisschan'
# __data__='20160908'
# __from__='EmmaTools https://github.com/crisschan/EMMATools'
# __instruction__= 测试需要处理字符串的类:
#           修改了方法添加了@classmethod装饰器
import random
import re


class TestString(object):
    def __GetMiddleStr(self,content, startPos, endPos):
        '''
        :根据开头和结尾字符串获取中间字符串
        :param content:原始string
        :param startPos: 开始位置
        :param endPos: 结束位置
        :return: 一个string
        '''
        # startIndex = content.index(startStr)
        # if startIndex >= 0:
        #    startIndex += len(startStr)
        # endIndex = content.index(endStr)
        return content[startPos:endPos]

    def __Getsubindex(self,content, subStr):
        '''
        :param content: 原始string
        :param subStr: 字符边界
        :return:  字符边界出现的第一个字符的在原始string中的位置 []
        '''
        alist = []

        asublen = len(subStr)
        sRep = ''
        istep = 0
        while istep < asublen:
            if random.uniform(1, 2) == 1:
                sRep = sRep + '~'
            else:
                sRep = sRep + '^'
            istep = istep + 1


        apos = content.find(subStr)
        while apos >= 0:
            alist.append(apos)
            content = content.replace(subStr, sRep, 1)

            apos = content.find(subStr)
        return alist

    @classmethod
    def GetTestString(cls_obj,content, startStr, endStr):
        '''
        :param content: 原始string
        :param startStr: 开始字符边界
        :param endStr: 结束字符边界
        :return: 前后边界一致的中间部分字符串 []
        '''
        reStrList = []
        if content is None or content=='':
            return reStrList
        if startStr!='' and content.find(startStr)<0:
            startStr=''
        if endStr!='' and content.find(endStr)<0:
            endStr=''

        if startStr=='':
            reStrList.append(content[:content.find(endStr)])
            return reStrList
        elif endStr=='':
            reStrList.append(content[content.find(startStr)+len(startStr):])
            return reStrList
        elif startStr=='' and  endStr=='':
            reStrList.append(content)
            return reStrList
        else:
            starttemplist = cls_obj().__Getsubindex(content, startStr)

            nStartlen = len(startStr)
            startIndexlist = []
            for ntemp in starttemplist:
                startIndexlist.append(ntemp + nStartlen)
            endIndexlist = cls_obj().__Getsubindex(content, endStr)

            astep = 0
            bstep = 0
            dr = re.compile(r'<[^>]+>', re.S)

            while astep < len(startIndexlist) and bstep < len(endIndexlist):
                while startIndexlist[astep] >= endIndexlist[bstep]:
                    bstep = bstep + 1
                strTemp = cls_obj().__GetMiddleStr(content, startIndexlist[astep], endIndexlist[bstep])
                strTemp = dr.sub('', strTemp)

                reStrList.append(strTemp)
                astep = astep + 1
                bstep = bstep + 1

            return reStrList

# if __name__ == "__main__":
#     strgg = '24214jnjkanrhquihrghjw<>eufhuin/jfghs<><a href=ajfjsanfghj/kg/hjkghj<>kghjfasd/sdaf'
#     print(TestString.GetTestString(strgg,'14','/'))