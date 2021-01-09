#! /usr/bin/python
# -*- coding: utf-8 -*-
# author : ouyi
# create_time : 2021-01-09

import pytest

from app_frame.page.main_page import MainPage
from app_frame.page_base import BasePage


class TestXueqiu:
    def setup(self):
        self.main = MainPage()
    def testa(self):
        self.main.goto_mark().goto_search().search(666)


if __name__ == "__main__":
    pytest.main(['-vs','test_xueqiu_demo.py'])