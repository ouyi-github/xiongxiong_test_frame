#! /usr/bin/python
# -*- coding: utf-8 -*-
# author : ouyi
# create_time : 2021-01-09

import os
import inspect
import signal
import subprocess
import time

import allure
import pytest

from app_frame.common_decorator import get_video
from app_frame.my_configs import config
from app_frame.page.main_page import MainPage
from app_frame.page_base import BasePage
from app_frame.my_utils.get_data import get_data_from_yaml
from app_frame.my_utils.get_time import get_now_time

class Test_MarkPage_Search:
    datas = get_data_from_yaml(path=os.path.join(config.BASE_DIR, 'data/test_markpage_search.yaml')).get('search')
    def setup(self):
        self.main = MainPage()
    def teardown(self):
        self.main._broswer_quit()

    @get_video
    @pytest.mark.parametrize('text',datas)
    def test_markpage_search(self,text):
        try:
            res = self.main.goto_mark().goto_search().search(text)
            time.sleep(2)
        except Exception as e:
            img_path = os.path.join(config.BASE_DIR, f'imgs/{inspect.stack()[0][3]}-{get_now_time()}.PNG')
            self.main._get_screenshot(path=img_path)
            raise e


if __name__ == "__main__":
    json_path = os.path.join(config.BASE_DIR,f'report/allure_result/{get_now_time()}') # 指定生成的json报告文件的路径
    html_path = os.path.join(config.BASE_DIR,f'report/allure_report/{get_now_time()}') # 指定生成的html报告文件的路径
    pytest.main(['-vs','test_markpage_search.py', f'--alluredir={json_path}'])
    os.system(f'allure generate {json_path} -o {html_path}')

