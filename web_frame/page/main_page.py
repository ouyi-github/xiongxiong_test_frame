#! /usr/bin/python
# -*- coding:utf-8 -*-
# author : ouyi
# create_time : 2021-01-09
import os

import yaml

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
            config.case_log.info('step: 首页》点击行情')
            self._load_element_yaml_action(os.path.join(config.BASE_DIR,'page_element_yaml/main_page.yaml'),'goto_mark')
            return MarkPage(self._driver)
        except Exception as e:
            raise e


