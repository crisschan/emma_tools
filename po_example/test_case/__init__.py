#!/usr/bin/env python
# -*- coding: utf-8 -*-

#__from__ = 'hi_po'
#__title__='PyCharm'
#__author__ = 'chancriss'
#__mtime__ = '2018/2/12'
#__instruction__=''




from .config.config_report import reportDir
from .config.config_report import reportDescription
from .config.config_report import reportTitle
from .config.config_mail import Smtp_Server
from .config.config_mail import Smtp_Sender
from .config.config_mail import Smtp_username
from .config.config_mail import Smtp_password
from .config.config_mail import Smtp_Receiver
from .config.config_mail import Mail_Body
from .config.config_db import dbuser
from .config.config_path import driver_path
from .config.config_param import searchparam
from .test_search import TestSearch

