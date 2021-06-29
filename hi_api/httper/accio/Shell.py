# -*- coding: utf-8 -*-
# @File    : Shell.py

"""
封装执行shell语句方法

"""

import subprocess


class Shell(object):
    @staticmethod
    def invoke(cmd):
        output, errors = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
        o = output.decode("utf-8","ignore")
        return o
