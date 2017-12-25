#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/12/5 17:26
# @Author  : milian0711
# @File    : generate_log.py
import logging
import os

check_path = '.'
LOG_DIR = os.path.join(check_path, 'log')

log_file = os.path.join(LOG_DIR, 'OMS_login.log')
print os.getcwd()
log_format = '[%(asctime)s] [%(levelname)s] %(message)s'
logging.basicConfig(format=log_format, filename=log_file, filemode='w', level=logging.INFO)
# 将日志同时输出到文件和屏幕
console = logging.StreamHandler()
console.setLevel(logging.DEBUG)
formatter = logging.Formatter(log_format)
console.setFormatter(formatter)
logging.getLogger('').addHandler(console)
