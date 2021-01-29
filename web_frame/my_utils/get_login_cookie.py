#! /usr/bin/python
# -*- coding: utf-8 -*-
# author : ouyi
# create_time : 2021-01-12
import os

import yaml
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from web_frame.my_configs import config


def get_login_cookies():
    """
    封装方法：获取复用浏览器cookie
    :return:
    """
    option = Options()
    option.debugger_address = '127.0.0.1:9222'
    driver = webdriver.Chrome(options=option)
    cookies = driver.get_cookies()
    with open(os.path.join(config.BASE_DIR,'cookies.yaml'),'w') as f:
        yaml.safe_dump(cookies,stream=f)



if __name__ == "__main__":
    get_login_cookies()
