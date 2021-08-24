#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   ciscp_message.py
@Time    :   2021/08/17 16:07:10
@Author  :   CrissChan 
@Version :   1.0
@Site    :   https://blog.csdn.net/crisschan
@Desc    :   None
'''

from httper import Httper
import httper
import json

root_uri = 'http://10.50.137.13:8020'
cs_hp = Httper(root_uri)
# login 
login_uri='/api/ciscp/portal-service/session/login'
username = '15801371836'
pwd = 'cde3XSW@zaq1'
random_visitor_id='criss'
captcha_content='666666'
payload_login = '{"random_visitor_id":"'+random_visitor_id+'","captcha_content":"'+captcha_content+'","user_name": "'+username+'","user_pwd": "'+pwd+'"}'
headers_login = {'Content-Type':'application/json'}
login_res = cs_hp.post(login_uri,data = payload_login,headers=headers_login)
login_res_json = json.loads(login_res.text)

access_token = login_res_json['data']['access_token']
refresh_token=login_res_json['data']['refresh_token']
token_type = login_res_json['data']['token_type']

# print(access_token)
# print(refresh_token)
# print(token_type)
# # send message

message_uri = '/api/ciscp/portal-service/message'
headers_message  ={
    'Content-Type': 'application/json',
    'Authorization':token_type+' '+access_token
}

# 用户手机号
# 日期
## template_id 1 表示短消息 2 表示长消息  4 表示外链
# 现实title
# payload_message = '{"app_user_id": '+username+',"data": "string","template_id": 1,"title": "string","url": "string" }'
payload_messages = ['{"app_user_id": '+username+',"data": "strinxiaoxiing1","template_id": 1,"title": "天气晴朗","url": "string" }',
'{"app_user_id": '+username+',"data": "inxiaoxistring4","template_id": 2,"title": "inxiaoxistring2","url": "string" }',
'{"app_user_id": '+username+',"data": "inxiaoxistring4","template_id": 4,"title": "inxiaoxistring4","url": "http://phecda.cicc.group/" }',
'{"app_user_id": '+username+',"data": "inxiaoxistring1","template_id": 1,"title": "inxiaoxistring1","url": "string" }',
'{"app_user_id": '+username+',"data": "inxiaoxistring1","template_id": 1,"title": "inxiaoxistring1","url": "string" }',
'{"app_user_id": '+username+',"data": "inxiaoxistring2","template_id": 2,"title": "inxiaoxistring2","url": "string" }']
i=0
while i< len(payload_messages):
    payload_message = payload_messages[i]
    message_res= cs_hp.post(message_uri,data=payload_message.encode('utf8'),headers = headers_message)
    print(message_res.text)
    i=i+1