#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/18 2:35 PM
# @Author  : Criss Chan
# @Site    : https://blog.csdn.net/crisschan
# @File    : work_webchat.py
# @Software: PyCharm
# @instruction：使用企业微信的机器人群发消息，在企业微信群里面，选择添加一个机器人，然后复制对应的webhook地址
#               每个机器人发送的消息不能超过20条/分钟。

from enum import Enum
import requests
import json

class MSGTYPE(Enum):
    TEXT = 'text'  # 文本类型。对应消息的限制：文本内容，最长不超过2048个字节，必须是utf8编码
    MARKDOWN = 'markdown'  # markdown类型,对应消息内容限制：markdown内容，最长不超过4096个字节，必须是utf8编码
    IMAGE = 'image'  # 图片，对应图片的base64编码限制：图片（base64编码前）最大不能超过2M，支持JPG,PNG格式
    NEWS = 'news'  # 图文消息，限制：图文消息，一个图文消息支持1到8条图文
    # title	是标题，不超过128个字节，超过会自动截断
    # description，描述不超过512个字节，超过会自动截断
    # url，点击后跳转的链接。
    # picurl图文消息的图片链接，支持JPG、PNG格式，较好的效果为大图 1068*455，小图150*150。


class workWechat(object):

    def __init__(self, webhook, msgtype, dictdetail, mentioned_mobile_list=''):
        '''

        :param webhook: 机器人的webhook地址
        :param msgtype: 消息类型，具体参见MSGTYPE枚举类型
        :param dictdetail: 消息主体内容
        :param mentioned_mobile_list: 手机号列表，提醒手机号对应的群成员(@某个成员)，@all表示提醒所有人(该参数只在消息类型为text的时候有效
        '''
        self.webhook = webhook
        self.msgtype = msgtype
        self.mentioned_mobile_list = mentioned_mobile_list

        self.detail = dictdetail

        self._send_msg()

    def _send_msg(self):
        headers = {'Content-Type': 'application/json'}
        payload = self._payload()

        res = requests.post(self.webhook, data=payload.encode('utf-8'), headers=headers)
        #{"errcode":0,"errmsg":"ok"}
        if json.loads(res.text)['errmsg']=='ok':
            print('scuccess')
        else:
            print('faile')

    def _payload(self):
        payload = ''
        mentioned_mobile = ''
        try:
            if len(self.mentioned_mobile_list) > 0:
                mentioned_mobile = '","'.join(self.mentioned_mobile_list)
                mentioned_mobile = '"mentioned_mobile_list":["' + mentioned_mobile + '"],'
        except:
            mentioned_mobile = ''

        if self.msgtype is MSGTYPE.NEWS:
            payload = '{"msgtype": "' + self.msgtype.value + '","' + self.msgtype.value + '": {  ' + mentioned_mobile + ' "articles" : [' + self.detail + ']}}'
        elif self.msgtype is MSGTYPE.MARKDOWN:
            payload = '{"msgtype": "' + self.msgtype.value + '","' + self.msgtype.value + '": {  ' + mentioned_mobile + '"content":"' + self.detail + '"}}'
        elif self.msgtype is MSGTYPE.TEXT:
            payload = '{"msgtype": "' + self.msgtype.value + '","' + self.msgtype.value + '": { ' + mentioned_mobile + '"content":"' + self.detail + '"}}'
        elif self.msgtype is MSGTYPE.IMAGE:
            payload = '{"msgtype": "' + self.msgtype.value + '","' + self.msgtype.value + '": { ' + mentioned_mobile + '"base64":' + self.detail + ',"md5":"MD5"}'

        else:
            payload = ''

        return payload


# if __name__ == '__main__':

    # wwc = workWechat('https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=',
    #                  MSGTYPE.MARKDOWN,
    #                  '实时新增用户反馈<font color=\\\"warning\\\">132例</font>，请相关同事注意。\n>类型:<font color=\\\"comment\\\">用户反馈</font> \n>普通用户反馈:<font color=\\\"comment\\\">117例</font> \n >VIP用户反馈:<font color=\\\"comment\\\">15例</font>',)
# wwc = workWechat('https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=',
#                  MSGTYPE.TEXT, ' "实时新增用户反馈，请注意')
# wwc = workWechat('https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=',
#                  MSGTYPE.IMAGE, ' "')
# aritcle = '''{
#            "title" : "就是你",
#            "description" : "gitflow",
#            "url" : "https://blog.csdn.net/crisschan/article/details/100922668",
#            "picurl" : "https://i.loli.net/2019/09/17/4wPgvOm72Q9zT8K.png"
#        }'''
# wwc = workWechat('https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=',
#                  MSGTYPE.NEWS, aritcle)
