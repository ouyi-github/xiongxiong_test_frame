#! /usr/bin/python
# -*- coding: utf-8 -*-
# author: ouyi
# createtime: 2021-02-01
import requests
from requests import Session


class BasePage:
    def __init__(self,corpid=None,corpsecret=None):
        # 生成session
        if corpid is None:
            my_corpid = 'wwb0963a3a379de433'
        else:
            my_corpid = corpid
        if corpsecret is None:
            my_corpsecret = 'X-G73KTHX9is69sJcNbv-T80SyqL86EyvFUOpm4MTsg'
        else:
            my_corpsecret = corpsecret

        r = requests.get(url=f'https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={my_corpid}&corpsecret={my_corpsecret}')
        token = r.json()['access_token']
        self.session = Session()
        # 将token封装到session
        self.session.params['access_token'] = token


