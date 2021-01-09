#! /usr/bin/python
# -*- coding:utf-8 -*-
# author : ouyi
# create_time : 2021-01-09
from app_frame.page.search_page import SearchPage
from app_frame.page_base import BasePage
from app_frame.my_utils.get_data import get_data_from_ini

class MarkPage(BasePage):
    def goto_search(self):
        """
        行情页面》点击搜索按钮
        :return:
        """
        try:
            ele = get_data_from_ini('mark','search_btn')
            self._wait_element_to_click(*ele)
            self._find_element_and_click(*ele)
            return SearchPage(self._driver)
        except Exception as e:
            raise e


