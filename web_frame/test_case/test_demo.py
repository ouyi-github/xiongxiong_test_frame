#! /usr/bin/python
# -*- coding: utf-8 -*-
# author : ouyi
# create_time : 2021-01-12
import pytest

from web_frame.my_configs import config
from web_frame.page_base import BasePage


class TestDemo:
    def testaa(self):
        self.base = BasePage()
        self.base._get_url_with_cookie('https://work.weixin.qq.com/wework_admin/frame')


if __name__ == "__main__":
    pytest.main(['-vs','test_demo.py'])