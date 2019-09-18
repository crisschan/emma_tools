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


class MSGTYPE(Enum):
    TEXT = 'text'  # 文本类型
    MARKDOWN = 'markdown'  # markdown类型
    IMAGE = 'image'  # 图片
    NEWS = 'news'  # 图文消息


class workWechat(object):

    def __init__(self, webhook, msgtype, dictdetail):
        self.webhook = webhook
        self.msgtype = msgtype

        self.detail = dictdetail

        self._send_msg()

    def _send_msg(self):
        headers = {'Content-Type': 'application/json'}
        payload = ''
        if self.msgtype is MSGTYPE.NEWS:
            payload = '{"msgtype": "' + self.msgtype.value + '","' + self.msgtype.value + '": {  "articles" : [' + self.detail + ']}}'
        elif self.msgtype is MSGTYPE.MARKDOWN:
            payload = '{"msgtype": "' + self.msgtype.value + '","' + self.msgtype.value + '": { "content":' + self.detail + '}}'
        elif self.msgtype is MSGTYPE.TEXT:
            payload = '{"msgtype": "' + self.msgtype.value + '","' + self.msgtype.value + '": { "content":' + self.detail + '}}'
        elif self.msgtype is MSGTYPE.IMAGE:
            payload = '{"msgtype": "' + self.msgtype.value + '","' + self.msgtype.value + '": {"base64":' + self.detail + ',"md5":"MD5"}'

        else:
            paylaod = ''

        print(payload)
        res = requests.post(self.webhook, data=payload.encode('utf-8'), headers=headers)

        print(res.text)


#if __name__ == '__main__':
    # wwc = workWechat('https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=',
    #                  MSGTYPE.MARKDOWN,
    #                  ' "实时新增用户反馈<font color=\\\"warning\\\">132例</font>，请相关同事注意。\n>类型:<font color=\\\"comment\\\">用户反馈</font> \n>普通用户反馈:<font color=\\\"comment\\\">117例</font> \n >VIP用户反馈:<font color=\\\"comment\\\">15例</font>"')
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