# @Time : 2020/11/12 14:13

# @Author : Cuiluming

# @File : locust_run.py

# @Software: PyCharm

import subprocess
from accio import locust_get_runlog
import threading
from accio import config_file_parser
import os
# import platform


def run(file,time,user):
    # BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # 项目目录
    BASE_DIR = os.path.dirname(os.path.join(os.getcwd()))
    # pattern = '/' if platform.system() != 'Windows' else '\\'
    if not os.path.exists(BASE_DIR + '\\log'):
        os.makedirs(BASE_DIR + '\\log')
    t1 = threading.Thread(target=locust_get_runlog.start("locust_monitoring"), args=())
    t1.start()
    try:
        a = subprocess.call('locust -f ..\\Performance\\{} --headless -u {} -r 5 -t {}m  --csv=..\\log\\locusts_report  --logfile=..\\log\\locust.log --loglevel=INFO 1>..\\log\\stdout.log  2>..\\log\\run.log '.format(file, user, time),
                              shell=True
                             )
        print("===========")
    except Exception as e:
        print(e)
    return a


# if __name__ == '__main__':
#     conf = config_file_parser.ConfigFileParserIni()
#     file = conf.get_value("locust_report","file")
#     time=conf.get_value("locust_report","time")
#     user=conf.get_value("locust_report", "user")
#     run(file = file,time = time,user = user )

