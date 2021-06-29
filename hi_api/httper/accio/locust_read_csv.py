# @Time : 2020/11/17 11:04

# @Author : Cuiluming

# @File : demo.py

# @Software: PyCharm
import csv
import pymysql
import time
import  os
from accio import config_file_parser
from random import randint
# curPath = os.path.abspath(os.path.dirname(__file__))  # 项目名称
# rootPath = os.path.split(curPath)[0]
class  ReadCvs(object):
    def __init__(self):
        self.rootPath=os.path.join(os.getcwd())
        self.csv_file_path =self.rootPath +"\\log\\locusts_report_stats.csv"
        self.csv_file_path_fail =self.rootPath +"\\log\\locusts_report_failures.csv"
        self.table_name_request = "webside_locust_result"
        self.table_name_fail = "webside_locust_fail_result"
        # db="accio"
        # self.user_name="崔"#压测作者需要传值
        self.now = int(time.time())
        self.creat_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        self.conf = config_file_parser.ConfigFileParserIni()
        print(self.conf)
        self.host = self.conf.get_value("connect_db", "host")
        self.user = self.conf.get_value("connect_db", "user")
        self.passwd = self.conf.get_value("connect_db", "passwd")
        self.db=self.conf.get_value("connect_db", "db")
        self.conn = pymysql.connect(user=self.user,
                       passwd=self.passwd,
                       db=self.db,
                       host=self.host,
                       local_infile=1)

    def read_csv(self,filename):
        read_list = []
        with open(filename) as f:
            f_csv = csv.reader(f)
            while True:
                try:
                    # 获得下一个值:
                    x = next(f_csv)
                    if len(x) == 0:
                        pass
                    else:
                        read_list.append(x)
                except StopIteration:
                    # 遇到StopIteration就退出循环
                    break
            # print(read_list)
        return read_list
    
    def conn_to_psto(self):
    
        self.conn.set_charset('utf8')
        self.cur = self.conn.cursor()
        self.cur.execute("set names utf8")
        self.cur.execute("SET character_set_connection=utf8;")
        return self.cur
    
    def  mysql_insert(self,author, performance_file_alis,times,user,proid):
        if not os.path.exists(self.rootPath + '\\log'):
            os.makedirs(self.rootPath + '\\log')
        f_csv = self.read_csv(self.csv_file_path)
        f_csv_file = self.read_csv(self.csv_file_path_fail)
        cur = self.conn_to_psto()
        now = int(time.time())
        creat_time=time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        # print(creat_time)
        for row in f_csv[1:]:
            print (row)
            try:
                sql = '''insert into %s (Type,Name,RequestCount,FailureCount,MedianResponseTime,AverageResponseTime,MinResponseTime,MaxResponseTime,AverageContentSize,Requests_s,Failures_s,Fifty_percent,sixty_six_percent,seventy_five_percent,eighty_percent,ninety_percent,ninety_five_percent,ninety_eight_percent,ninety_nine_percent,ninety_nine_point_nine_percent,ninety_nine_point_nine_nine_percent,one_hundred_percent,systime,user_name,creat_time,delete_flag,SceneName,user,times,proid)values(%s,%s,%d,%d,%f,%f,%d,%d,%d,%f,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%s,%s,%s,%s,%s,%s,%s,%s) ''' \
                      %(self.table_name_request,str("'" + row[0] + "'"), str("'" + row[1] + "'"), int(row[2]), int(row[3]), float(row[4]),\
                      float(row[5]), float(row[6]), float(row[7]), int(row[8].replace('.0','')), float(row[9]), float(row[10]), int(row[11]),\
                      int(row[12]), int(row[13]), int(row[14]), int(row[15]), int(row[16]), int(row[17]), int(row[18]),\
                      int(row[19]), int(row[20]), int(row[21]),  now,"'" + author+"'", "'" + self.creat_time+"'","0","'" + performance_file_alis+"'","'" + user+"'","'" + times+"'","'" + proid+"'")
                # print(sql)
                cur.execute(sql)
            except  Exception as e:
                print(e)
                print("发生数据错误")
                # conn.rollback()
            finally:
                pass
            for row in f_csv_file[1:]:
                # if len(row)==0:
                #     pass
                try:
                    sql = '''insert into %s (Method,Name,Error,Occurrences,systime,user_name,creat_time,delete_flag,SceneName)values(%s,%s,%s,%d,%s,%s,%s,%s,%s) ''' \
                          % (self.table_name_fail, str("'" + row[0] + "'"), str("'" + row[1] + "'"), str("'" + row[2] + "'"),
                             int(row[3]), now, "'" +  author + "'", "'" +  self.creat_time + "'","0","'" +  performance_file_alis + "'")
                    print(sql)
                    cur.execute(sql)
                except  Exception as e:
                    print(e)
                    print("发生数据错误")
                    # conn.rollback()
                finally:
                    pass
        self.conn.commit()
        self.conn.close()

# if __name__ == "__main__":
#     mysql_insert()
#     mysql_insert_fails()