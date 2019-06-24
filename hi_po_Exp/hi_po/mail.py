#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'CrissChan'
# __instruction__='for  mail report'
import sys
from selenium import webdriver
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
import smtplib
import os
from test_case.config.config_mail import Smtp_Server
from test_case.config.config_mail import Smtp_Sender
from test_case.config.config_mail import Smtp_username
from test_case.config.config_mail import Smtp_password
from test_case.config.config_mail import Smtp_Receiver
from test_case.config.config_mail import Mail_Body
from test_case.config.config_path import driver_path
import time
from test_case.config.config_db import dbserver,dbpassword,dbport,dbuser,db

class Sendmail(object):
    def __init__(self, dirReport):
        ##数据库
        # self.mycon = MySQLHelper(dbserver, dbport, dbuser, dbpassword)
        # self.mycon.selectDb(db)
        # try:
        if not os.path.exists(dirReport):
            os.mkdir(dirReport)
        file_new = self.new_report(dirReport)
        self.send_mail(file_new)
        # except Exception:
        #     print("please input testCase,report file's location!")

    # def __def__(self):
    #     try:
    #         self.mycon.close()
    #     except:
    #         return

    def new_report(self,testreport):
        lists = os.listdir(testreport)
        lists.sort(key=lambda fn: os.path.getmtime(testreport + fn))
        file_new = os.path.join(testreport, lists[-1])
        return file_new


    def send_mail(self,file_new):
        self.driver = webdriver.Chrome(driver_path)
        # self.driver = webdriver.PhantomJS(driver_path)
        ##得到测试报告路径
        result_url = "file://%s"%file_new
        self.driver.get(result_url)
        self.driver.quit()
        smtp = smtplib.SMTP()
        smtp.connect(Smtp_Server)
        sender = Smtp_Sender
        username = Smtp_username
        password = Smtp_password
        receiver = Smtp_Receiver
        smtp.login(username, password)
        mail_body = Mail_Body
        msg = MIMEMultipart('alternative')
        text = MIMEText(mail_body, 'html', 'utf-8')
        msg.attach(text)
        msg['Subject'] = Header("hi_po ui自动化测试报告" , 'utf-8')
        msg['From'] = sender
        msg['To'] = ",".join(receiver)
        file_open = open(file_new,'rb')
        sendfile = file_open.read()
        att = MIMEText(sendfile, 'base64', 'utf-8')
        att["Content-Type"] = 'application/octet-stream'
        att["Content-Disposition"] = 'attachment; filename="testreport.html"'
        msg.attach(att)
        smtp.sendmail(sender, receiver, msg.as_string())

