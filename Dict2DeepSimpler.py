#!/usr/bin/env python
# -*- coding: utf-8 -*-

#!/usr/bin/env python
# -*- coding: utf-8 -*-

#__from__ = 'PythonSpace'
#__title__='PyCharm'
#__author__ = 'chancriss'
#__mtime__ = '2018/1/4'
#__instruction__='将一个分度非常深的dict变成深度为1的dict（无嵌套的）'

class Dict2DeepSimpler(object):
    def __init__(self,adict):
        '''

        Args:
            adict: 输入需要降低深度的dict
        '''
        self.__dictResult=self.__deepSearchDict(adict)
    def __deepSearchDict(self,adict):
        dictResult = {}
        for (k,v) in adict.items():

            if type(v) is not dict:
                dictResult=dict(dictResult, **{k:v})
            else:
                dictResult = dict(dictResult,**self.__deepSearchDict(v))
        return dictResult
    @property
    def dictResult(self):
        return self.__dictResult

'''adict = {'s':'ff','rr':{'r':'44'}}
aa= json.dumps(adict)
print type(aa)
print aa
dict2DeepSimpler = Dict2DeepSimpler(adict)

print dict2DeepSimpler.dictResult'''

