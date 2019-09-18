#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/17 4:20 PM
# @Author  : Criss Chan
# @Site    : https://blog.csdn.net/crisschan
# @File    : serverchan.py
# @Software: PyCharm
# @instruction：调用serverchan发送微信消息：每人每天发送上限500条，相同内容5分钟内不能重复发送，
# 不同内容一分钟只能发送30条。24小时请求接口超过1000次的账户将被封禁。

import  requests
import json
class  WeChatMessage(object):
    '''
    申请http://sc.ftqq.com/3.version，就可以使用发微信通知的功能了
    '''
    def __init__(self,title,msg=''):
        '''

        :param title: 消息标题.maxlength是256字节，必填
        :param msg:消息内容maxlength是64k，支持markdown，非必填
        '''
        self.title = title
        self.msg = msg
        self._send_msg()


    def _send_msg(self):
        #{SCKEY}替换成你自己的SCKEY，具体获取流程在网站上
        url = 'https://sc.ftqq.com/{SCKEY}.send'

        payload = 'text='+self.title+'&desp='+self.msg

        headers = {'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'}
        res=requests.post(url,data=payload.encode('utf-8'),headers = headers)

        res_json = json.loads(res.text)

        print(res_json)


# if __name__ == '__main__':
#     wb =  WeChatMessage('我是谁','我在那')