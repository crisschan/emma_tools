# -*- encoding: utf-8 -*-
"""
@File    : Module_detection.py
@Time    : 2020/9/30 10:42
@Author  : liyinlong
@Software: PyCharm
"""
import re
import os
import sys
from accio import logger, parse_tools


class Module(object):

    def __init__(self):
        self.root_path=parse_tools.Parse.get_rootpath()
        # self.root_path = str(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)))
        self.file = os.path.join(self.root_path, "requirements.txt")
        if not os.path.exists(self.file):
            raise FileNotFoundError("请确保requirements文件存在！")
        self.log = logger.MyLog()

    def module_detection(self):
        with open(self.file, 'r') as e:
            f = e.read()
            list_m = f.strip('\n').split('\n')
            for i in list_m:
                try:
                    m_name = re.findall(r'(.+?)\=', i)[0]
                    print("正在检测 %s 模块" % m_name)
                    show_m = os.system('pip show %s' % m_name)
                    print(show_m)
                    if show_m != 0:
                        print("正在安装 %s 模块" % m_name)
                        install_m = os.system("pip install %s" % i)
                        if install_m != 0:
                            print("%s 模块安装失败" % m_name)
                            sys.exit(1)

                except:
                    self.log.error("-----模块检测出现异常！----")
                    print('模块检测出现异常！')


# if __name__ == "__main__":
#     k = Module()
#     k.module_detection()
