# -*- coding: utf-8 -*-
# @File    : Log.py

"""
封装log方法

"""

import logging
import os
import time
from accio import config_file_parser

LEVELS = {
    'debug': logging.DEBUG,
    'info': logging.INFO,
    'warning': logging.WARNING,
    'error': logging.ERROR,
    'critical': logging.CRITICAL
}

logger = logging.getLogger()


class MyLog(object):
    # path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    def __init__(self):
        conf = config_file_parser.ConfigFileParserIni()
        level = conf.get_value('log', 'level')

        path = conf.get_value('log', 'path')
        log_file = path + 'log.log'
        err_file = path + 'error.log'
        logger.setLevel(LEVELS.get(level, logging.NOTSET))
        self.create_file(log_file)
        self.create_file(err_file)
        self.date = '%Y-%m-%d %H:%M:%S'

        self.handler = logging.FileHandler(log_file, encoding='utf-8')
        self.err_handler = logging.FileHandler(err_file, encoding='utf-8')

    def create_file(self, filename):
        path = filename[0:filename.rfind('/')]
        if not os.path.isdir(path):
            os.makedirs(path)
        if not os.path.isfile(filename):
            fd = open(filename, mode='w', encoding='utf-8')
            fd.close()
        else:
            pass

    def set_handler(self, levels):
        if levels == 'error':
            logger.addHandler(self.err_handler)
        logger.addHandler(self.handler)

    def remove_handler(self, levels):
        if levels == 'error':
            logger.removeHandler(self.err_handler)
        logger.removeHandler(self.handler)

    def get_current_time(self):
        return time.strftime(self.date, time.localtime(time.time()))

    def debug(self, log_meg):
        self.set_handler('debug')
        logger.debug("[DEBUG " + self.get_current_time() + "]" + log_meg)
        self.remove_handler('debug')

    def info(self, log_meg):
        self.set_handler('info')
        logger.info("[INFO " + self.get_current_time() + "]" + log_meg)
        self.remove_handler('info')

    def warning(self, log_meg):
        self.set_handler('warning')
        logger.warning("[WARNING " + self.get_current_time() + "]" + log_meg)
        self.remove_handler('warning')

    def error(self, log_meg):
        self.set_handler('error')
        logger.error("[ERROR " + self.get_current_time() + "]" + log_meg)
        self.remove_handler('error')

    def critical(self, log_meg):
        self.set_handler('critical')
        logger.error("[CRITICAL " + self.get_current_time() + "]" + log_meg)
        self.remove_handler('critical')


# if __name__ == "__main__":
#     MyLog().debug("This is debug message")
#     MyLog().info("This is info message")
#     MyLog().warning("This is warning message")
#     MyLog().error("This is error")
#     MyLog().critical("This is critical message")

