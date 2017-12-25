#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/12/6 18:50
# @Author  : milian0711
# @File    : generateTime.py

"""
用于设置权重失效时间
思路：
1、将当前时间转换为时间戳
2、在生成的时间戳上加上秒数
3、再次转换为标准时间格式
eg: minute = 5
当前时间的5分钟后权重失效
"""

import re
import time

def generateTime(minute):
    now = time.time()
    # print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    setting_time = time.localtime(now + (minute * 60))
    dt = time.strftime("%Y-%m-%d %H:%M:%S", setting_time)
    # print type(dt)
    # dt_list = re.findall("\d+", str)
    # return"%s年%s月%s日%s时%s分%s秒"%(dt_list[0], dt_list[1], dt_list[2], dt_list[3], dt_list[4], dt_list[5])
    # print dt
    return dt

