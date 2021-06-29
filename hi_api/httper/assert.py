# -*- coding: utf-8 -*-
# @File    : Assert.py


"""
封装Assert方法

"""
from log import logger
import consts
import json


class Assertions(object):
    def __init__(self):
        self.log = logger.MyLog()

    def code(self, code, expected_code):
        """
        验证response状态码
        :param code:
        :param expected_code:
        :return:
        """
        try:
            assert code == expected_code
            return True
        except:
            self.log.error("statusCode error, expected_code is %s, statusCode is %s " % (expected_code, code))
            consts.RESULT_LIST.append('fail')

            raise

    def body(self, body, body_msg, expected_msg):
        """
        验证response body中任意属性的值
        :param body:
        :param body_msg:
        :param expected_msg:
        :return:
        """
        try:
            print("====body==============================>>>>", body)
            print("====body_msg============================>>>>>>", body_msg)
            msg = body[body_msg]
            assert msg == expected_msg
            return True

        except:
            self.log.error("Response body msg != expected_msg, expected_msg is %s, body_msg is %s" % (expected_msg, body_msg))
            consts.RESULT_LIST.append('fail')

            raise

    def find_key(self, content, akey):
        if akey in content:
            return content[akey]
        else:
            for key in content.keys():
                if isinstance(content[key], list):
                    for alist in content[key]:
                        if isinstance(alist, dict):
                            return self.find_key(alist, akey)
                elif isinstance(content[key], dict):
                    return self.find_key(content[key], akey)
        return None

    def assert_body(self, real_body, excepte_dict):
        """
        :param self:
        :param body:
        :param excepte_dict:
        :return:
        """
        print("------assert_body-----:", type(excepte_dict),excepte_dict)
        try:
            excepte_dict = eval(excepte_dict)
            dict = {}
            for element_key in excepte_dict:
                real_value = self.find_key(content=real_body, akey=element_key)
                print("=====+++++==real_value========", real_value)
                if type(real_value) == int or str(real_value) in ['true', 'false', 'null', 'True', 'False']:
                    real_value = str.lower(str(real_value))
                if real_value != "":
                    dict.update({element_key:real_value})
                else:
                    print("没找到key")
            print("校验结果dict------------------------------", dict)
            print("excepte_dict------------------------------", excepte_dict)
            assert excepte_dict == dict
            return True
        except:
            self.log.error("assertion error")
            consts.RESULT_LIST.append('fail')
            raise

    def in_body(self, body, body_msg, expected_msg):
        """
        验证response body中任意属性的值
        :param body:
        :param body_msg:
        :param expected_msg:
        :return:
        """
        try:
            msg = body[body_msg]
            assert expected_msg in msg
            return True

        except:
            self.log.error("Response body msg != expected_msg, expected_msg is %s, body_msg is %s" % (expected_msg, body_msg))
            consts.RESULT_LIST.append('fail')

            raise


    def in_text(self, body, expected_msg):
        """
        验证response body中是否包含预期字符串
        :param body:
        :param expected_msg:
        :return:
        """
        try:
            text = json.dumps(body, ensure_ascii=False)
            # print(text)
            assert expected_msg in text
            return True

        except:
            self.log.error("Response body Does not contain expected_msg, expected_msg is %s" % expected_msg)
            consts.RESULT_LIST.append('fail')

            raise

    def text(self, body, expected_msg):
        """
        验证response body中是否等于预期字符串
        :param body:
        :param expected_msg:
        :return:
        """
        try:
            assert body == expected_msg
            return True

        except:
            self.log.error("Response body != expected_msg, expected_msg is %s, body is %s" % (expected_msg, body))
            consts.RESULT_LIST.append('fail')

            raise

    def time(self, time, expected_time):
        """
        验证response body响应时间小于预期最大响应时间,单位：毫秒
        :param body:
        :param expected_time:
        :return:
        """
        try:
            assert time < expected_time
            return True

        except:
            self.log.error("Response time > expected_time, expected_time is %s, time is %s" % (expected_time, time))
            consts.RESULT_LIST.append('fail')

            raise


