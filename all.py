#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/12/25 10:04
# @Author  : milian0711
# @File    : all.py

import json

import requests
from PIL import Image
import os
import re
import time
# from nose.tools import *

from config.config import Conf
from log.generate_log import logging

"""
登录的思路：
访问post_url时会出现两次302跳转，
第1次302时，获取到响应header中的url,
通过这个url,再次获取响应header中的url,
这个url就是获取到最新生成jessionid的url,
接着需要做的就是保持当前会话去请求其他接口
"""

session = requests.session()
def identify_code(IC_url):
    """
    获取验证码
    """
    r = session.get(IC_url, headers=Conf.headers)
    with open('./log/captcha.jpg', 'wb') as f:
        f.write(r.content)
        f.close()
    # 用pillow 的 Image 显示验证码
    # 如果没有安装 pillow 到源代码所在的目录去找到验证码然后手动输入
    try:
        im = Image.open('./log/captcha.jpg')
        im.show()
        im.close()
    except:
        print(u'请到 %s 目录找到captcha.jpg 手动输入' % os.path.abspath('./log/captcha.jpg'))
    captcha = input("please input the captcha\n>")
    return captcha

def get_lt(post_url):
    """
    获取lt
    """
    page = session.get(post_url, headers=Conf.headers)
    html = page.text
    pattern = r'id="lt" value="(.*?)"'
    # 这里的lt 返回的是一个list
    lt = re.findall(pattern, html)
    return lt[0]

def get_location(post_url):
    """
    获取302跳转的url
    """
    ID_card = identify_code(Conf.IC_url)
    lt = get_lt(post_url)
    print lt
    postdata = {
        'username': Conf.username,
        'password': Conf.password,
        '_eventId': "submit",
        'lt': lt,
        'j_captcha_response': ID_card
    }
    resp = session.post(post_url, data=postdata, headers=Conf.headers, allow_redirects=False, verify=False)
    # print requests.head(post_url).headers
    time.sleep(2)
    mylocation = resp.headers['location']

    logging.info("mylocation is %s"% mylocation)
    return mylocation
    # print resp.headers

    # session.cookies.save()
    # with open("login.html", "wb") as f:
    #     f.write(login_page.content)

def login_page(location_url):
    """
    获取最新生成jessonid的url
    """
    resp = session.get(location_url, headers=Conf.headers,allow_redirects=False, verify=False)
    oms_url = resp.headers['location']
    logging.info("oms_url is %s " % oms_url)
    oms_page = session.get(oms_url, headers=Conf.headers)

    # with open('./log/login.html', 'wb') as f:
    #     f.write(oms_page.content)


def test_change(change_url, id):
    """
    长链转短链接口，有以下几种情形：
    1、ID为普通新闻类型
    2、ID为节目推荐类型
    3、ID带有空格
    4、ID带有符号
    5、ID不存在
    """
    # qs = [17884373, 17754437, '185374 25', '185374#25', 185374]
    param_list = Conf.param_list
    for q in param_list:
        # data = {"keyWord": id}
        data = dict(keyWord=q[0])
        resp = session.post(change_url, data=data, headers=Conf.headers)
        logging.info("input id is: %s", q[0])
        logging.info("result is:%s", resp.json())
        # 由于q[1]类型为str, 而result类型为bool, 因而需要转换
        result = str(resp.json()['success'])
        # eq_(q[1], result, '{0}!={1}'.format(expect, result))
        if q[1] == result:
            logging.info('change_test success')
        else:
            logging.info('change_test fail')

def test_transExternalImg():
    """
    外部图片地址转换为服务器图片地址
    contID:新闻ID
    columname:IMAGES
    contText:图片标签
    :return:
    验证返回值是否为true
    """""
    contID = Conf.newsID
    columnName = "IMAGES"
    # 由于浏览器对传入的contText进入了渲染，传的时候需要传入源标签的内容
    # contText = '<img+src="http://www.cs.com.cn/ssgs/fcgs/201712/W020171201369316897595.jpg"+alt=""+/>'
    contText = '<img src="http://www.cs.com.cn/ssgs/fcgs/201712/W020171201369316897595.jpg" alt="" />'
    # 包含4种类型(bmp,png,jpg,gif)的图片转换
    contText = '<img src="http://www.cs.com.cn/ssgs/fcgs/201712/W020171201369316897595.jpg" alt="" /><img src="http://www.cr173.com/up/2014-9/14109191026919813.gif" alt="" /><img src="http://www.sucaitianxia.com/sheji/pic/200706/20070620224220832.bmp" alt="" /><img alt="" src="https://upload.wikimedia.org/wikipedia/commons/9/98/SAKURA.png" />'

    postdata = {
        "contId": contID,
        "columnName": columnName,
        "contText": contText
    }
    resp = session.post(Conf.transfer_url, data=postdata, headers=Conf.headers)
    logging.info("postdata is %s" % postdata)
    logging.info("response is %s" % resp.json())
    result = str(resp.json()['success'])
    logging.info("transExternalImg result is %s" % result)


def test_linkSearch():
    """
    链接到功能测试
    rowsContData：待链接的新闻ID
    rowsNodeData：链接到的栏目ID
    isCopy: 是否链接
    """
    rowsContData = "'" + '["' + str(Conf.newsID) + '"]' + "'"
    rowsNodeData = "'" + '["' + str(Conf.nodeID) + '"]' + "'"

    postdata = {
        "rowsContData":rowsContData,
        "rowsNodeData":rowsNodeData,
        "isCopy":"true"
    }
    resp = session.post(Conf.link_url, data=postdata, headers=Conf.headers)
    logging.info("postdata is %s" % postdata)
    logging.info("response is %s" % resp.json())
    result = str(resp.json()['success'])
    logging.info("linkSearch result is %s" % result)

def test_recommandSearch():
    """
    推荐到功能测试
    rowsContData：待推荐的新闻ID
    rowsNodeData：推荐到的栏目ID
    isCopy: 是否推荐
    """
    rowsContData = "'" + '["' + str(Conf.newsID) + '"]' + "'"
    rowsNodeData = "'" + '["' + str(Conf.nodeID) + '"]' + "'"

    postdata = {
        "rowsContData": rowsContData,
        "rowsNodeData": rowsNodeData,
        "isCopy":"true"
    }
    resp = session.post(Conf.recommandSearch_url, data=postdata, headers=Conf.headers)
    logging.info("postdata is %s" % postdata)
    logging.info("response is %s" % resp.json())
    result = str(resp.json()['success'])
    logging.info("linkSearch result is %s" % result)


def test_copySearch():
    """
    复制到功能测试
    rowsContData：待复制的新闻ID
    rowsNodeData：复制到的栏目ID
    isCopy: 是否复制
    """
    rowsContData = "'" + '["' + str(Conf.newsID) + '"]' + "'"
    rowsNodeData = "'" + '["' + str(Conf.nodeID) + '"]' + "'"

    postdata = {
        "rowsContData": rowsContData,
        "rowsNodeData": rowsNodeData,
        "isCopy":"true"
    }
    resp = session.post(Conf.copySearch_url, data=postdata, headers=Conf.headers)
    logging.info("postdata is %s" % postdata)
    logging.info("response is %s" % resp.json())
    result = str(resp.json()['success'])
    logging.info("linkSearch result is %s" % result)




from public.generateTime import generateTime
def test_importance(importance):
    """
    设置权重功能
    nodeId：栏目ID
    check：状态是否是已审核
    contIds: 新闻ID
    importanceValue：权重值
    cleanImportanceTime: 权重失效时间
    """
    setting_time = generateTime(20)
    postdata = {
        "nodeId":str(Conf.nodeID),
        "check":"1",
        "contIds":str(Conf.newsID),
        "importanceValue": importance,
        "cleanImportanceTime": setting_time
    }
    resp = session.post(Conf.updateImportance_url, data=json.dumps(postdata), headers=Conf.headers)
    logging.info("postdata is %s" % postdata)
    logging.info("response is %s" % resp.json())
    result = str(resp.json()['message'])
    logging.info("updateImportance result is %s" % result)

def test_addFavoriteNews():
    """
    添加新闻到收藏夹
    newsId: 待收藏的新闻ID
    """
    postdata = {
        "newsId": str(Conf.newsID)
    }
    resp = session.post(Conf.addFavoriteNews_url, data=json.dumps(postdata), headers=Conf.headers)
    result = str(resp.json()['success'])
    logging.info("response is %s" % result)
    if bool(result) == True:
        logging.info("addFavoriteNews success" )
    else:
        logging.info("addFavoriteNews failure" )

def test_cancelFavoriteNews():
    """
    从我的收藏夹中取消收藏
    newsId: 待取消的新闻ID
    """
    postdata = {
        "newsId": str(Conf.newsID)
    }
    resp = session.post(Conf.cancelFavoriteNews_url, data=json.dumps(postdata), headers=Conf.headers)
    result = str(resp.json()['success'])
    logging.info("response is %s" % result)
    # 由于result为str类型，在判断时需要进行转换
    # logging.info("type response is %s" % type(result))

    if bool(result) == True:
        logging.info("cancelFavoriteNews success" )
    else:
        logging.info("cancelFavoriteNews failure" )

def test_getNickname():
    resp = session.post(Conf.getNickname_url, headers=Conf.headers)
    nickname = resp.json()["data"]
    logging.info("randomNickname is %s" % nickname)
    return nickname

def test_addComment():
    """
    添加评论功能
    method：添加评论
    objId：被评论的新闻ID
    userNickName: 用户昵称名字
    content：评论内容
    objectName: 新闻标题
    """

    postdata = {
        "method":"comment",
        "objId": str(Conf.newsID),
        "userNickName": test_getNickname(),
        "content":"oms add comments",
        "objectName": "这一“充电焦虑”怎么破解？国家放出大招"
    }
    resp = session.post(Conf.addComment_url, data=json.dumps(postdata), headers=Conf.headers)
    logging.info("postdata is %s" % postdata)
    logging.info("response is %s" % resp)
    logging.info("response is %s" % resp.json())
    result = str(resp.json()['result'])
    if str(result) == '0000':
        logging.info("linkSearch result success")





if __name__ == '__main__':

    mylocation = get_location(Conf.post_url)
    # 由于测试环境的mylocation没有http
    # 若是测试环境，需要加个判断
    if Conf.host == "```":
        mylocation = "http://" + mylocation
    login_page(mylocation)
    # test_change(Conf.change_url, Conf.newsID)
    # test_transExternalImg()
    # test_linkSearch()
    # test_recommandSearch()
    # test_copySearch()
    # test_addComment()
    # test_importance(5)
    test_addFavoriteNews()
    test_cancelFavoriteNews()
