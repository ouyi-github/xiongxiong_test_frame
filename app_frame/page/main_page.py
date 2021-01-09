#! /usr/bin/python
# -*- coding:utf-8 -*-
# author : ouyi
# create_time : 2021-01-09

from app_frame.my_configs import config
from app_frame.page.mark_page import MarkPage
from app_frame.page_base import BasePage
from app_frame.my_utils.get_data import get_data_from_ini


class MainPage(BasePage):
    def goto_mark(self):
        """
        首页》点击行情
        :return:
        """
        try:
            ele = get_data_from_ini('main','floating_pen')
            self._wait_element_to_click(*ele)
            self._find_element_and_click(*ele)
            ele = get_data_from_ini('main','mark_btn')
            self._wait_element_to_click(*ele)
            self._find_element_and_click(*ele)
            return MarkPage(self._driver)
        except Exception as e:
            raise e


