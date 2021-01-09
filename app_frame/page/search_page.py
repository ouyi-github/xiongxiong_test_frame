#! /usr/bin/python
# -*- coding:utf-8 -*-
# author : ouyi
# create_time : 2021-01-09

from app_frame.page_base import BasePage
from app_frame.my_utils.get_data import get_data_from_ini


class SearchPage(BasePage):
    def search(self,text):
        """
        搜索页面》搜索功能
        :param text:
        :return:
        """
        ele = get_data_from_ini('search','search_input')
        self._wait_element_to_click(*ele)
        self._find_element_and_sendkeys(*ele,text=text)
