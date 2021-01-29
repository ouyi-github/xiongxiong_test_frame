#! /usr/bin/python
# -*- coding: utf-8 -*-
import logging
import os

from app_frame.my_utils.get_dir import get_base_dir
from app_frame.my_utils.get_time import get_now_time
from app_frame.my_utils.get_logger import MyLogger

# 项目目录
BASE_DIR = get_base_dir()

# logger模块配置
logger_path = os.path.join(BASE_DIR,f'logs/{get_now_time()}.log')
logger_level = logging.INFO
logger_format = logging.Formatter('%(asctime)s-%(levelname)s-%(message)s-%(filename)s-%(lineno)d-%(funcName)s')
# 生成一个logger实例
case_log = MyLogger(name='caselog',path=logger_path,level=logger_level,format=logger_format).get_logger()

# allure报告路径配置
result_path = os.path.join(BASE_DIR,f'report/allure_result/{get_now_time()}')
report_path = os.path.join(BASE_DIR,f'report/allure_report/{get_now_time()}')

# element_yaml中所有的action配置
element_yaml_actions = ['_find_element','_find_elments','_find_element_and_click','_find_element_and_sendkeys','_wait_element_to_click',
                        '_swip_find_element','_broswer_quit','_get_toast','_swip_find_element_and_click']

# 浏览器cookie文件地址
COOKIE_PATH = os.path.join(BASE_DIR,'cookies.yaml')
