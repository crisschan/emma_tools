# -*- encoding: utf-8 -*-
"""
@File    : ConfigFIleParser.py
@Time    : 2020/9/3 9:44
@Author  : Yu Tao
@Software: PyCharm
"""


import os
from configparser import ConfigParser, NoSectionError, NoOptionError, MissingSectionHeaderError
from accio.return_code import _init_err_code, get_err_code
# from accio.Log import MyLog


class ConfigFileParser(object):

    def __init__(self, file=None):
        """
        初始化
        :param file: 配置文件路径，默认为根路径下ini文件
        """
        _init_err_code()
        # self.log = self.get_log()
        self.configer = ConfigParser()
        self.file = file
        if not os.path.exists(file):
            raise FileNotFoundError("请确保配置文件存在！")
        try:
            self.configer.read(file, encoding='utf-8')
        except :
            # self.log.debug(get_err_code("20002"))
            print(get_err_code("20002"))

    def get_value(self, title, key):
        """
        获取配置文件中的值
        :param title:
        :param key:
        :return:
        """
        # global config
        try:
            the_value = self.configer.get(title, key)
        except NoSectionError:
            # self.log.error(get_err_code("20003"))
            print(get_err_code("20003"))
            the_value = "error"
        except NoOptionError:
            # self.log.error(get_err_code("20004"))
            print(get_err_code("20004"))
            the_value = "error"
        return the_value

    def set_value(self, title, key, value):
        """
        设置配置文件中的键值
        :param title:
        :param key:
        :param value:
        :return:
        """
        # global config
        self.configer.set(title, key, value)

    def get_config_ini(self):
        # rootPath = str(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)))
        # file = os.path.join(rootPath, "config.ini")
        file = os.path.join(os.getcwd(), "configer.ini")
        self.configer = ConfigParser()
        if not os.path.exists(file):
            raise FileNotFoundError("请确保配置文件存在！")
        try:
            self.configer.read(file, encoding='utf-8')
        except:
            # self.log.debug(get_err_code("20002"))
            print(get_err_code("20002"))

    def write_config_ini(self, section, option, value):
        try:
            configer = self.configer
            configer.set(section, option, value)
            configer.write(open(self.file, "w", encoding='UTF-8'))
        except:
            print("更新ini文件失败！")


class ConfigFileParserIni(ConfigFileParser):

    def __init__(self):
        """
        加载框架级配置文件configer
        """
        # rootPath = str(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)))
        # file = os.path.join(rootPath, "configer.ini")
        file = os.path.join(os.getcwd(), "configer.ini")
        super().__init__(file)


# if __name__ == '__main__':
#     print(ConfigFileParserIni().get_value("scheduler", "time_pattern"))
