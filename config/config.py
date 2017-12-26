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
    host = ""
    ano = ""
    website = "http://" + host
    Config.headers['Host'] = host
    Config.headers['Referer'] = website + '/sso/login?service=' + ano + '/oms/main.html'
    post_url = website + '/sso/login?service=' + ano + '/oms/main.html'
    # 验证码
    IC_url = website + '/sso/captcha.htm'
    username = ''
    password = ''

    # TEST栏目下面的一条普通新闻
    newsID = 6869323
    # 链接到的栏目名称：批量测试
    nodeID = 2002662
    # 第二项为节目推荐类型
    param_list = [('6869323', 'True'), ('17754437', 'False'), ('185374 25', 'False'), ('185374#25', 'False'), (185374, 'False')]



    ID = 6869314
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
    # 添加新闻到我的收藏夹
    addFavoriteNews_url = website + "/oms/addFavoriteNews.json"
    # 从我的收藏夹中取消收藏
    cancelFavoriteNews_url = website + "/oms/cancelFavoriteNews.json"
    # 获得随机昵称
    getNickname_url = website + "/oms/getRandomCommentNickName.json"
    # 后台添加评论
    addComments_url = website + "/oms/addComment.json"

class ProductConfig(Config):
    host = ""
    website = "http://" + host
    Config.headers['Host'] = host
    Config.headers['Referer'] = website + '/sso/login?service=' + website + '/oms/main.html'
    post_url = website + '/sso/login?service=' + website + '/oms/main.html'
    # 验证码
    IC_url = website + '/sso/captcha.htm'
    username = ''
    password = ''


    # NEW栏目下面的一条普通新闻
    newsID = 17884373
    # 链接到的栏目名称：批量测试
    nodeID = 2008364

    param_list = [('17884373', 'True'), ('17754437', 'False'), ('185374 25', 'False'), ('185374#25', 'False'), (185374, 'False')]

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
    # 添加新闻到我的收藏夹
    addFavoriteNews_url = website + "/oms/addFavoriteNews.json"
    # 从我的收藏夹中取消收藏
    cancelFavoriteNews_url = website + "/oms/cancelFavoriteNews.json"
    # 获得随机昵称
    getNickname_url = website + "/oms/getRandomCommentNickName.json"
    # 后台添加评论
    addComments_url = website + "/oms/addComment.json"

Conf = ProductConfig