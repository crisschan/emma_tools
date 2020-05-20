#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time       : 2020/5/20 12:24 下午
# @Author     : CrissChan
# @Site       : https://blog.csdn.net/crisschan
# @File       : __init__.py.py
# @instruction:
#               1、Dict2DeepSimpler：将一个深度非常深的dict变成深度为1的dict（无嵌套的）
#               2、DirAndFiles：获取各种目录文件：
#               3、GetDistance：计算两经纬度间的距离
#               4、ImageChange：所有图片类型的相互转换
#               5、Img2Base64：将图片变成base64编码，然后在web中打开，不用引入图片外部图片文件
#               6、SendeMail：发送邮件
#               7、SplitImg：图片分割
#               8、RotateImg：图片旋转
#               9、Stack:栈
#               10、InitTestJson:生成测试要用的json
#               11、TestString:测试需要处理字符串的类,类似LoadRunner的关联方法
#               12、Timer:计算耗时的装饰器封装
#               13、VideoChange:视频修改码率的，为创建各种不同测试使用的视频文件做准备
#               14、workWechat:计算耗时的装饰器封装
#                   MSGTYPE:message类型
#



from dict_reduce_deep import Dict2DeepSimpler
from get_dirAndfiles import DirAndFiles
from get_distance import GetDistance
from image_change import ImageChange
from Img2Base64 import Img2Base64
from info_hidden2img import InfoHidden2Img
from rotate_img import RotateImg
from send_mail import SendeMail
from slipt_img import SplitImg
from stack import Stack
from init_test_json import InitTestJson
from test_string import TestString
from timer import Timer
from video_change import VideoChange
from work_webchat_robot import workWechat,MSGTYPE


