# @Time : 2020/11/13 10:18 

# @Author : Cuiluming

# @File : locust_get_runlog.py

# @Software: PyCharm

import io
import platform
import os, sys
from accio.conn_influxdb import ConnectInfluxDB
import threading
import time
from accio import config_file_parser,parse_tools

interval = 3
conf = config_file_parser.ConfigFileParserIni()
time1=conf.get_value("locust_report","time")
start_time=int(time.time())
end_time=start_time+int(time1)*60


def read_file():
    locust_list = []
    # BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # 项目目录
    BASE_DIR = parse_tools.Parse.get_rootpath()
    curPath = os.path.abspath(os.path.dirname(__file__))  # 项目名称
    rootPath = os.path.split(curPath)[0] + '\\' + os.path.split(curPath)[1]
    sys.path.append(rootPath)
    pattern = '/' if platform.system() != 'Windows' else '\\'
    performance_path = os.path.join(BASE_DIR, 'log' + pattern + "run.log")
    # print(performance_path)
    influxdb = ConnectInfluxDB()
    with io.open(performance_path) as f:
        data_list = f.readlines()
        i=0
        for data in data_list:
            splits = data.split()
            # print("splits :%s" % splits)
            temp = []
            for s in splits:
                if s.replace(" ", "").strip('\n').strip('|').__len__() != 0:
                    temp.append(s)
                    # print(temp)
            if len(temp) > 1 and (temp[0] == 'POST' or temp[0] == 'GET'):
                # print("进入res")
                # print(temp)
                method = temp[0]
                api = temp[1]
                reqs = temp[2]
                fails = temp[3]
                Avg = temp[4]
                Min = temp[5]
                Max = temp[6]
                Median = temp[7]
                qps = temp[8]
                failures = temp[9]
                # ninety_percent=float(temp[10])
                # ninety_five_percent= float(temp[11])
                # ninety_nine_percent=float(temp[13])
                locust_dict = {'Method': method, 'Name': api, 'Requests': reqs, 'Fails': fails, 'Average_ms': Avg,
                               'Min_ms': Min, 'Max_ms': Max, 'Median_ms': Median, 'Current_RPS': qps,
                               'Failures_s': failures,}
                locust_list.append(locust_dict)
            if len(temp) > 1 and temp[0] == 'Aggregated':
                # print("进入Aggregated")
                # print("Aggregated:%s" % temp)
                method = temp[0]
                api = temp[0]
                reqs = temp[1]
                fails = temp[2]
                Avg = temp[3]
                Min = temp[4]
                Max = temp[5]
                Median = temp[6]
                qps = temp[7]
                failures = temp[8]
                locust_dict = {'Method': method, 'Name': api, 'Requests': reqs, 'Fails': fails, 'Average_ms': Avg,
                               'Min_ms': Min, 'Max_ms': Max, 'Median_ms': Median, 'Current_RPS': qps,
                               'Failures_s': failures}
                locust_list.append(locust_dict)
        influxdb.post_dump_data(locust_list, "locust")
    # return locust_dict


def monitor(project_name):
    print("start monitoring")
    read_file()
    timer = threading.Timer(interval, monitor, args=[project_name])
    timer.start()
    start_time = int(time.time())
    if(start_time<=end_time):
        print(start_time,end_time)
        pass
    else:
        timer.cancel()


def start(*args, **kwargs):
    timer = threading.Timer(interval, monitor, args=args, kwargs=kwargs)
    print("start=====")
    timer.start()

# if __name__ == '__main__':
#     locust_result().read_file()