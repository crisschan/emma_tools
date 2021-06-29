# -*- coding: utf-8 -*-
# @File    : Session.py

"""
封装获取cookie方法

"""

import requests
from log import logger


class Session(object):
    def __init__(self):
        self.log = logger.MyLog()

    def get_session(self, url, parm, headers):
        """
        获取session
        :param
        :return:
        """

        try:

            session_release = requests.session()
            response = session_release.post(url, parm, headers)
            print(response.cookies.get_dict())
            self.log.debug('cookies: %s' % response.cookies.get_dict())
            return response.cookies.get_dict()

        except:
            print("get cookies error")
            self.log.error('get cookies error, please checkout!!!')


# if __name__ == '__main__':
#     ss = Session()
#     ss.get_session('debug')