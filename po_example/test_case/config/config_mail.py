#!/usr/bin/env python
# -*- coding: utf-8 -*-
#__from__ = 'hi_po_example'
#__author__ = ''
#__mtime__ = '2018/4/28'
#__instruction__='邮件配置'
from hi_po import mail
Smtp_Server = 'smtp.qq.com'
Smtp_Sender = 'ee-rdc-yys-test@hi_po.com'
Smtp_username = 'ee-rdc-yys-test'
Smtp_password = 'crisschan!'
# Smtp_Receiver = ['ee-rdc-yystest@jd.com']
Smtp_Receiver = ['admin@hi_po.com']

Mail_Body = '<html><head><script src="https://cdn.bootcss.com/echarts/3.8.5/echarts.common.min.js"></script></head><meta charset = "utf-8"/ >'\
        '<body>' \
             '<div id="div_base"> ' \
             '<div class="page-header">' \
             '<h1>hipo UI自动化测试报告</h1>' \
                '<h1 color="DarkGray">—————————————————————————————</h1>' \
                    '<p class="attribute">更多详情请查看附件> hipo测试报告</a></p>' \
                    '<p class="attribute">本次上线：日常功能回归</p>' \
                    '<font color="#FF0000">本报告由自动化工具生成，如有疑问，请联系报告人。</font><br>' \
            '</div>' \
            '</div>' \
        '</body>' \
        '</html>'