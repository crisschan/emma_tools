# -*- encoding: utf-8 -*-
"""
@File    : TimedTasks.py
@Time    : 2020/9/9 9:38
@Author  : Yu Tao
@Software: PyCharm
"""

from apscheduler.schedulers.blocking import BlockingScheduler
from accio.config_file_parser import ConfigFileParserIni


class TimedTasks(object):

    def __init__(self, trigger=None):
        """
        初始化定时任务
        :param trigger: 触发器类型：interval、date、cron三种
        """
        if trigger is None:
            self.trigger = ConfigFileParserIni().get_value("scheduler", "trigger")
        elif trigger in ["interval", "date", "cron"]:
            self.trigger = trigger
        else:
            print("触发器输入有误。")
        self.cron = ConfigFileParserIni().get_value("scheduler", "time_pattern")

    def create_scheduler(self, job, time_pattern):
        """
        创建定时任务
        :param job: 任务
        :param time_pattern: 时间模式
        :return:
        """
        scheduler = BlockingScheduler()
        if self.trigger == "interval":
            scheduler.add_job(job, self.trigger, seconds=time_pattern)
        elif self.trigger == "date":
            scheduler.add_job(job, self.trigger, run_date=time_pattern)
        elif self.trigger == "cron":
            cronList = time_pattern.split(" ")
            scheduler.add_job(job, self.trigger, minutes=cronList[0], hours=cronList[1], date=cronList[2],
                              month=cronList[3], day_of_week=cronList[4])


# if __name__ == '__main__':
#     conf = TimedTasks("").create_scheduler()

    # while True:
    #     # print('main-start:', time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
    #     time.sleep(2)
    #     # print('main-end:', time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))