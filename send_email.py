# !/usr/bin/python
#coding:utf-8
# __author_='crisschan'
# __data__='20160908'
# __from__='EmmaTools https://github.com/crisschan/EMMATools'
# __instruction__=发送邮件
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
import time
class sendemail(object):

    def __init__(self,sender,receiver,subject,username,password,stmpconnect,transMsg):
        '''
        :param sender: 发送邮箱
        :param receiver: 接收邮箱
        :param subject: 邮件标题
        :param username: 发送邮箱用户名
        :param password: 发送邮箱密码
        :param transMsg: 发送正文
        :param stmpconnect stmp地址
        '''
        self.sender = sender
        self.receiver = receiver
        self.subject = subject
        self.username = username
        self.password =password
        self.transMsg  = transMsg
        self.stmpconnect = stmpconnect

    def _pickupMsgPlain(self):
        self.msg = MIMEText(self.transMsg, _subtype='plain', _charset='utf-8')  # 中文需参数‘utf-8’，单字节字符不需要

        self.msg['Subject'] = Header(self.subject, 'utf-8')
        self.msg['from'] = self.sender
        self.msg['to'] = self.receiver
    def _pickupMsgHTML(self):
        self.msg = MIMEText(self.transMsg, _subtype='html', _charset='utf-8')  # 中文需参数‘utf-8’，单字节字符不需要

        self.msg['Subject'] = Header(self.subject, 'utf-8')
        self.msg['from'] = self.sender
        self.msg['to'] = self.receiver

    def _pickupMsgAtt(self):
        self.msg = MIMEMultipart()
        for attfile in self.attfiles:
            att = MIMEText(open(attfile, 'rb').read(), 'base64', 'gb2312')
            att["Content-Type"] = 'application/octet-stream'
            att["Content-Disposition"] = 'attachment; filename='+attfile.split('/')[-1]  # 这里的filename可以任意写，写什么名字，邮件中显示什么名字
            self.msg.attach(att)

        self.msg['Subject'] = Header(self.subject, 'utf-8')
        self.msg['from'] = self.sender
        self.msg['to'] = self.receiver
    def send(self,sendMode='plain',attfiles=[]):
        '''

        :param sendMode: email send mode
                         plain is text
                         html is webpage
                         att is have attfile
        :param attfiles: is  a  list save the attfiles absolute address
        :return:
        '''
        if sendMode=='plain':
            self._pickupMsgPlain()
        elif sendMode=='HTML':
            self._pickupMsgHTML()
        elif sendMode=='att':
            if len(attfiles)<1:
                return 0
            else:
                self.attfiles = attfiles
                self._pickupMsgAtt()

        try:
            smtp = smtplib.SMTP()
            smtp.connect(self.stmpconnect)
            smtp.login(self.username, self.password)
            smtp.sendmail(self.sender, self.receiver, self.msg.as_string())
            smtp.quit()
            return 1
        except Exception as e:
            return e

'''
if __name__=='__main__':


    sender = '2053581240@qq.com'
    receiver='148065025@qq.com'
    subject = 'python email test'
    smtpserver = 'smtp.qq.com'
    username = '2053581240'
    password = ''
    stmpconnect = 'smtp.qq.com'
    transMsg = '等大大发发'+str(time.time())
    attfile = ['/Users/chancriss/Desktop/work/95.pic.jpg','/Users/chancriss/Desktop/work/95.pic.jpg','/Users/chancriss/Desktop/work/95.pic.jpg']
    tr = sendemail(sender,receiver,subject,username,password,stmpconnect,transMsg)
    print tr.send(sendMode='att',attfiles=attfile)
    '''
