# -*- coding: utf-8 -*-
# @File    : Http.py

"""
封装request

"""

import os
import random
import requests
import accio.Consts

from requests_toolbelt import MultipartEncoder


class Request(object):

    def __init__(self):
        """
        :param
        """
        self.get_session = {}

    def get(self, url, data, header):
        """
        Get请求
        :param url:
        :param data:
        :param header:
        :return:

        """
        if not url.startswith('http'):
            url = '%s%s' % ('http://', url)

        try:
            if data is None:
                response = requests.get(url=url, headers=header, cookies=self.get_session)
            else:
                response = requests.get(url=url, params=data, headers=header, cookies=self.get_session)

        except requests.RequestException as e:
            print('%s%s' % ('RequestException url: ', url))
            print(e)
            return ()

        except Exception as e:
            print('%s%s' % ('Exception url: ', url))
            print(e)
            return ()

        time_consuming = response.elapsed.microseconds/1000
        time_total = response.elapsed.total_seconds()

        accio.Consts.STRESS_LIST.append(time_consuming)

        response_dicts = dict()
        response_dicts['code'] = response.status_code
        try:
            response_dicts['body'] = response.json()
        except Exception as e:
            print(e)
            response_dicts['body'] = ''
        response_dicts['text'] = response.text
        response_dicts['time_consuming'] = time_consuming
        response_dicts['time_total'] = time_total

        return response_dicts

    def get_json(self, url, data, header):
        """
        Get请求,返回数据为json
        :param url:
        :param data:
        :param header:
        :return:

        """
        if not url.startswith('http'):
            url = '%s%s' % ('http://', url)

        try:
            if data is None:
                response = requests.get(url=url, headers=header, cookies=self.get_session)
            else:
                response = requests.get(url=url, params=data, headers=header, cookies=self.get_session)

        except requests.RequestException as e:
            print('%s%s' % ('RequestException url: ', url))
            print(e)
            return ()

        except Exception as e:
            print('%s%s' % ('Exception url: ', url))
            print(e)
            return ()

        time_consuming = response.elapsed.microseconds/1000
        accio.Consts.STRESS_LIST.append(time_consuming)

        try:
            response_json = response.json()
        except Exception as e:
            print(e)

        return response_json

    def get_text(self, url, data, header):
        """
        Get请求,返回数据为text
        :param url:
        :param data:
        :param header:
        :return:

        """
        if not url.startswith('http'):
            url = '%s%s' % ('http://', url)

        try:
            if data is None:
                response = requests.get(url=url, headers=header, cookies=self.get_session)
            else:
                response = requests.get(url=url, params=data, headers=header, cookies=self.get_session)

        except requests.RequestException as e:
            print('%s%s' % ('RequestException url: ', url))
            print(e)
            return ()

        except Exception as e:
            print('%s%s' % ('Exception url: ', url))
            print(e)
            return ()

        time_consuming = response.elapsed.microseconds/1000
        accio.Consts.STRESS_LIST.append(time_consuming)

        try:
            response_text = response.text
        except Exception as e:
            print(e)

        return response_text

    def post(self, url, data, header):
        """
        Post请求
        :param url:
        :param data:
        :param header:
        :return:

        """
        if not url.startswith('http'):
            url = '%s%s' % ('http://', url)
            print(url)
        try:
            if data is None:
                response = requests.post(url=url, headers=header, cookies=self.get_session)
            else:
                response = requests.post(url=url, data=data.encode(), headers=header, cookies=self.get_session)

        except requests.RequestException as e:
            print('%s%s' % ('RequestException url: ', url))
            print(e)
            return ()

        except Exception as e:
            print('%s%s' % ('Exception url: ', url))
            print(e)
            return ()

        # time_consuming为响应时间，单位为毫秒
        time_consuming = response.elapsed.microseconds/1000
        # time_total为响应时间，单位为秒
        time_total = response.elapsed.total_seconds()

        accio.Consts.STRESS_LIST.append(time_consuming)

        response_dicts = dict()
        response_dicts['code'] = response.status_code
        try:
            response_dicts['body'] = response.json()
        except Exception as e:
            print(e)
            response_dicts['body'] = ''

        response_dicts['text'] = response.text
        response_dicts['time_consuming'] = time_consuming
        response_dicts['time_total'] = time_total

        return response_dicts

    def post_json(self, url, data, header):
        """
        Post请求,返回数据格式为json
        :param url:
        :param data:
        :param header:
        :return:

        """
        if not url.startswith('http'):
            url = '%s%s' % ('http://', url)
            print(url)
        try:
            if data is None:
                response = requests.post(url=url, headers=header, cookies=self.get_session)
            else:
                response = requests.post(url=url, data=data.encode(), headers=header, cookies=self.get_session)

        except requests.RequestException as e:
            print('%s%s' % ('RequestException url: ', url))
            print(e)
            return ()

        except Exception as e:
            print('%s%s' % ('Exception url: ', url))
            print(e)
            return ()

        # time_consuming为响应时间，单位为毫秒
        time_consuming = response.elapsed.microseconds/1000
        # time_total为响应时间，单位为秒
        time_total = response.elapsed.total_seconds()

        accio.Consts.STRESS_LIST.append(time_consuming)

        try:
            response_json = response.json()
        except Exception as e:
            print(e)

        return response_json

    def post_text(self, url, data, header):
        """
        Post请求,返回数据格式为text
        :param url:
        :param data:
        :param header:
        :return:

        """
        if not url.startswith('http'):
            url = '%s%s' % ('http://', url)
            print(url)
        try:
            if data is None:
                response = requests.post(url=url, headers=header, cookies=self.get_session)
            else:
                response = requests.post(url=url, data=data.encode(), headers=header, cookies=self.get_session)

        except requests.RequestException as e:
            print('%s%s' % ('RequestException url: ', url))
            print(e)
            return ()

        except Exception as e:
            print('%s%s' % ('Exception url: ', url))
            print(e)
            return ()

        # time_consuming为响应时间，单位为毫秒
        time_consuming = response.elapsed.microseconds/1000
        # time_total为响应时间，单位为秒
        time_total = response.elapsed.total_seconds()

        accio.Consts.STRESS_LIST.append(time_consuming)

        try:
            response_text = response.text
        except Exception as e:
            print(e)

        return response_text

    def post_multipart(self, url, data, header, file_parm, file, f_type):
        """
        提交Multipart/form-data 格式的Post请求
        :param url:
        :param data:
        :param header:
        :param file_parm:
        :param file:
        :param type:
        :return:
        """
        if not url.startswith('http'):
            url = '%s%s' % ('http://', url)
            print(url)
        try:
            if data is None:
                response = requests.post(url=url, headers=header, cookies=self.get_session)
            else:
                data[file_parm] = os.path.basename(file), open(file, 'rb'), f_type

                enc = MultipartEncoder(
                    fields=data,
                    boundary='--------------' + str(random.randint(1e28, 1e29 - 1))
                )

                header['Content-Type'] = enc.content_type
                response = requests.post(url=url, data=data.encode(), headers=header, cookies=self.get_session)

        except requests.RequestException as e:
            print('%s%s' % ('RequestException url: ', url))
            print(e)
            return ()

        except Exception as e:
            print('%s%s' % ('Exception url: ', url))
            print(e)
            return ()

        # time_consuming为响应时间，单位为毫秒
        time_consuming = response.elapsed.microseconds/1000
        # time_total为响应时间，单位为秒
        time_total = response.elapsed.total_seconds()

        accio.Consts.STRESS_LIST.append(time_consuming)

        response_dicts = dict()
        response_dicts['code'] = response.status_code
        try:
            response_dicts['body'] = response.json()
        except Exception as e:
            print(e)
            response_dicts['body'] = ''

        response_dicts['text'] = response.text
        response_dicts['time_consuming'] = time_consuming
        response_dicts['time_total'] = time_total

        return response_dicts

    def put(self, url, data, header):
        """
        Put请求
        :param url:
        :param data:
        :param header:
        :return:

        """
        if not url.startswith('http'):
            url = '%s%s' % ('http://', url)
            print(url)

        try:
            if data is None:
                response = requests.put(url=url, headers=header, cookies=self.get_session)
            else:
                response = requests.put(url=url, data=data.encode(), headers=header, cookies=self.get_session)

        except requests.RequestException as e:
            print('%s%s' % ('RequestException url: ', url))
            print(e)
            return ()

        except Exception as e:
            print('%s%s' % ('Exception url: ', url))
            print(e)
            return ()

        time_consuming = response.elapsed.microseconds/1000
        time_total = response.elapsed.total_seconds()

        accio.Consts.STRESS_LIST.append(time_consuming)

        response_dicts = dict()
        response_dicts['code'] = response.status_code
        try:
            response_dicts['body'] = response.json()
        except Exception as e:
            print(e)
            response_dicts['body'] = ''
        response_dicts['text'] = response.text
        response_dicts['time_consuming'] = time_consuming
        response_dicts['time_total'] = time_total

        return response_dicts

    def put_json(self, url, data, header):
        """
        Put请求,返回数据为json
        :param url:
        :param data:
        :param header:
        :return:

        """
        if not url.startswith('http'):
            url = '%s%s' % ('http://', url)
            print(url)

        try:
            if data is None:
                response = requests.put(url=url, headers=header, cookies=self.get_session)
            else:
                response = requests.put(url=url, data=data.encode(), headers=header, cookies=self.get_session)

        except requests.RequestException as e:
            print('%s%s' % ('RequestException url: ', url))
            print(e)
            return ()

        except Exception as e:
            print('%s%s' % ('Exception url: ', url))
            print(e)
            return ()

        time_consuming = response.elapsed.microseconds/1000
        time_total = response.elapsed.total_seconds()

        accio.Consts.STRESS_LIST.append(time_consuming)

        try:
            response_json = response.json()
        except Exception as e:
            print(e)

        return response_json

    def put_text(self, url, data, header):
        """
        Put请求,返回数据为text
        :param url:
        :param data:
        :param header:
        :return:

        """
        if not url.startswith('http'):
            url = '%s%s' % ('http://', url)
            print(url)

        try:
            if data is None:
                response = requests.put(url=url, headers=header, cookies=self.get_session)
            else:
                response = requests.put(url=url, data=data.encode(), headers=header, cookies=self.get_session)

        except requests.RequestException as e:
            print('%s%s' % ('RequestException url: ', url))
            print(e)
            return ()

        except Exception as e:
            print('%s%s' % ('Exception url: ', url))
            print(e)
            return ()

        time_consuming = response.elapsed.microseconds/1000
        time_total = response.elapsed.total_seconds()

        accio.Consts.STRESS_LIST.append(time_consuming)

        try:
            response_text = response.text
        except Exception as e:
            print(e)

        return response_text
