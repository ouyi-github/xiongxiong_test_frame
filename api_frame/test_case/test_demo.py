#! /usr/bin/python
# -*- coding: utf-8 -*-
# author: ouyi
# create_time: 2021-01-29
import pytest
import requests


class TestDemo:
    def setup_class(self):
        # 生成token
        url = 'https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=wwb0963a3a379de433&corpsecret=X-G73KTHX9is69sJcNbv-T80SyqL86EyvFUOpm4MTsg'
        r = requests.get(url=url)
        self.token = r.json()['access_token']

    def test_add_remenber(self):
        """
        创建成员测试用例
        :return:
        """
        url = f'https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={self.token}'
        # 请求数据体
        request_json = {
            "userid": "cndy",
            "name": "王大锤",
            "mobile": "13118175239",
            "department": [5]
        }
        r = requests.post(url=url,json=request_json)
        assert r.json()['errcode'] == 0
        assert r.json()['errmsg'] == 'created'

    def test_delete_remenber(self):
        """
        删除成员测试用例
        :return:
        """
        url = f'https://qyapi.weixin.qq.com/cgi-bin/user/delete?access_token={self.token}&userid=cndy'
        r = requests.get(url=url)
        assert r.json()['errcode'] == 0
        assert r.json()['errmsg'] == 'deleted'

if __name__ == "__main__":
    pytest.main(['-vs','test_demo.py'])