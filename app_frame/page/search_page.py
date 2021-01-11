#! /usr/bin/python
# -*- coding:utf-8 -*-
# author : ouyi
# create_time : 2021-01-09
import os

from app_frame.my_configs import config
from app_frame.page_base import BasePage
from app_frame.my_utils.get_data import get_data_from_ini


class SearchPage(BasePage):
    def search(self,text):
        """
        搜索页面》搜索功能
        :param text:
        :return:
        """
        try:
            config.case_log.info('step: 搜索页面》搜索功能')
            self._load_element_yaml_action(os.path.join(config.BASE_DIR,'page_element_yaml/search_page.yaml'),'search',text=text)
            return SearchPage(self._driver)
        except Exception as e:
            raise e
