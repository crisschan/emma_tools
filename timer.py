#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/14 9:11 AM
# @Author  : Criss Chan
# @Site    : https://blog.csdn.net/crisschan
# @File    : timer.py
# @Software: PyCharm
# @instruction：计算耗时的装饰器封装

import time
# 这是装饰函数
class timer(object):

    def timer(func):
        def wrapper(*args, **kw):
            t1=time.time()
            # 这是函数真正执行的地方
            func(*args, **kw)
            t2=time.time()

            # 计算下时长
            cost_time = t2-t1
            print("花费时间：{}秒".format(cost_time))
        return wrapper




#使用举例子


if __name__ == '__main__':

    @timer.timer
    def want_sleep(sleep_time):
        time.sleep(sleep_time)

    want_sleep(10)
