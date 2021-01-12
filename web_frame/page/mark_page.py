#! /usr/bin/python
# -*- coding:utf-8 -*-
# author : ouyi
# create_time : 2021-01-09
import os

from app_frame.my_configs import config
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
            config.case_log.info('step: 行情页面》点击搜索按钮')
            self._load_element_yaml_action(os.path.join(config.BASE_DIR,'page_element_yaml/mark_page.yaml'),'goto_search')
            return SearchPage(self._driver)
        except Exception as e:
            raise e


