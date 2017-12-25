#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/12/25 9:25
# @Author  : milian0711
# @File    : config.py


class Config(object):
    agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0'
    headers = {
    'User-Agent': agent
    }

class DevelopmentConfig(Config):
    host = "****"
    website = "http://" + host
    Config.headers['Host'] = host
    Config.headers['Referer'] = website + '/sso/login?service=' + website + '/oms/main.html'
    post_url = website + '/sso/login?service=' + website + '/oms/main.html'
    # 验证码
    IC_url = website + '/sso/captcha.htm'
    username = '***'
    password = '***'

    # 长短链转换
    change_url = website + '/oms/change.json'
    # 外部图片地址转换为服务器地址
    transfer_url = website + "/oms/transExternalImg.json"
    # 链接到
    link_url = website + "/oms/linkSearchResult.json"
    # 推荐到
    recommandSearch_url = website + "/oms/recommandSearchResult.json"
    # 复制到
    copySearch_url = website + "/oms/recommandSearchResult.json"
    # 添加评论
    addComment_url = website + "/oms/addComment.json"
    # 权重
    updateImportance_url = website + "/oms/updateImportance.json"


class ProductConfig(Config):
    host = "****"
    website = "http://" + host
    Config.headers['Host'] = host
    Config.headers['Referer'] = website + '/sso/login?service=' + website + '/oms/main.html'
    post_url = website + '/sso/login?service=' + website + '/oms/main.html'
    # 验证码
    IC_url = website + '/sso/captcha.htm'
    username = '***'
    password = '****'

    # 长短链转换
    change_url = website + '/oms/change.json'
    # 外部图片地址转换为服务器地址
    transfer_url = website + "/oms/transExternalImg.json"
    # 链接到
    link_url = website + "/oms/linkSearchResult.json"
    # 推荐到
    recommandSearch_url = website + "/oms/recommandSearchResult.json"
    # 复制到
    copySearch_url = website + "/oms/recommandSearchResult.json"
    # 添加评论
    addComment_url = website + "/oms/addComment.json"
    # 权重
    updateImportance_url = website + "/oms/updateImportance.json"


Conf = DevelopmentConfig