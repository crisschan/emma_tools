# -*- encoding: utf-8 -*-
"""
@File    : ReturnCode.py
@Time    : 2020/9/7 11:19
@Author  : Yu Tao
@Software: PyCharm
"""


def _init_err_code():
    """
    初始化异常返回码字典
    通用异常返回码10001-19999
    文件读取类异常返回码20001-29999
    :return:
    """
    global glo_err_code
    glo_err_code = {"10001":"ParmisEmpty，参数为空",
                    "10002":"CallFunctionFail，调用方法异常",
                    "10003":"OtherError，其他异常",
                    "20001":"FileNotFound，文件没有找到",
                    "20002":"MissingSectionHeaderError，文件不符合格式或字符集编码有问题",
                    "20003":"NoSectionError，title没有找到",
                    "20004":"NoOptionError，key没有找到",
                    }


def set_err_code(key, value):
    """
    设置异常返回码
    :param key: 键
    :param value: 值
    :return:
    """
    glo_err_code[key] = value


def get_err_code(key):
    """
    获取异常返回码
    :param key: 键
    :return: 值
    """
    # from accio import Log
    # log = Log.MyLog()
    try:
        return glo_err_code[key]
    except KeyError:
        # log.error("key错误")
        print("key错误")





