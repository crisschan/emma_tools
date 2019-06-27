#encoding=utf8
#!/usr/bin/env python
# __author_='crisschan'
# __data__='20161130'
# __from__='EmmaTools https://github.com/crisschan/EMMATools'
# __instruction__生成测试要用的json

from stack import Stack
class InitTestJson(object):
    '''
    subJsonLoop：将给定的json字符串中某一个子节点或者数组重复后，组成新json返回
                 主要服务于json的测试用例生成
    '''
    def __init__(self,strJsonTemplate):
        '''
        Args:
            strJsonTemplate: 要做处理的json原文件
        '''
        self.strJsonTemplate=str(strJsonTemplate)
        #print self.strJsonTemplate
        #self.arrNumberlist=arrNumberlist
        self.__Parsing()
    def __PreFirst(self,nPos,sTarget):
        '''
        找到字符串中nPos之前的第一次sTarget出现的位置
        Args:
            nPos: 位置
            sTarget: 目标字符
        Returns:
        '''
        while nPos>=0:
            nPos = nPos - 1
            if self.strJsonTemplate[nPos]==sTarget or self.strJsonTemplate[nPos]=='{':
                return nPos
            
            
    def __Parsing(self):
        '''
        按照栈的方式分析大括号和中括号的位置
        Returns:
        '''
        self.listbrace=[]#大括号
        self.listbrackets=[]#小括号
        sCharTemp=Stack()#存大括号和中括号（{【）
        #sIntTemp=Stack()#位置（{）
        nPos=0

        for aTemp in self.strJsonTemplate:
            #print aTemp
            if aTemp == '{':
                dictTemp = {nPos:'{'}
                sCharTemp.push(dictTemp)

            elif aTemp=="[":
                dictTemp = {nPos: '['}
                sCharTemp.push(dictTemp)

            elif  aTemp==']':
                keyTemp = sCharTemp.pop()
                if keyTemp.values()[0] == '[':
                    sPos = keyTemp.keys()[0]
                    sign=(sPos,nPos+1)
                    self.listbrackets.append(sign)
                    #print self.listbrackets
            elif aTemp=='}':
                keyTemp = sCharTemp.pop()
                if keyTemp.values()[0] == '{':
                    sPos = keyTemp.keys()[0]
                    sign = (sPos, nPos+1)
                    self.listbrace.append(sign)
                    #print self.listbrace
            nPos=nPos+1
        self.listbrace=sorted(self.listbrace, key=lambda x: x[0])
        self.listbrackets = sorted(self.listbrackets, key=lambda x: x[0])

    def createTestJson(self,Type,number,count):
        '''
        Args:
            Type: {或者[两中输入
            number: type的字符第几次出现
            count: 要重复的次数（结果json要重复几次number的位置）
        Returns:
        '''
        if count<=0:
            return 0
        else:
            if Type=='{':
                if number <= 0:
                    return 0
                startpos = self.listbrace[number][0]
                endpos = self.listbrace[number][1]
                prestr=self.strJsonTemplate[0:endpos]
                poststr=self.strJsonTemplate[endpos:]

                nkey=self.__PreFirst(startpos,',')+1
                strRe = prestr
                while count-1>0:
                    strRe=strRe+','+self.strJsonTemplate[nkey:endpos]
                    count=count -1
                strRe=strRe+poststr
                return strRe
            elif Type=='[':
                if number < 0:
                    return 0
                startpos = self.listbrackets[number][0]+1
                endpos = self.listbrackets[number][1]-1
                prestr = self.strJsonTemplate[0:endpos ]


                poststr = self.strJsonTemplate[endpos + 1:]

                strRe = prestr
                while count-1 > 0:
                    strRe = strRe +','+ self.strJsonTemplate[startpos:endpos]
                    count = count - 1
                strRe = strRe +']'+ poststr
                return strRe
            else:
                return 0





if __name__=='__main__':
    data3 = {'a': 123, 'b': 789, 'c': 456, 'd': {'b': 7897, 'c': 4567, 'a': 1237}}
    data1 = {'i':{'a': 123, 'b': 789},'k':{'c': 456, 'd': {'b': 789, 'c': 456, 'a': 123}}}
    data2 = {'a': 123, 'b': 789,'c': [{'a': 123, 'b': 789}]}
    I1= InitTestJson(data2)
    print(I1.createTestJson('[',0,4))


    #print str(data1)[0:81]



