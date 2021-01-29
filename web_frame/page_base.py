#! /usr/bin/python
# -*- coding: utf-8 -*-
# author : ouyi
# create_time: 2021-01-09
import yaml
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.webdriver import WebDriver

from web_frame.my_configs import config


class BasePage:
    def __init__(self,driver:WebDriver=None):
        if driver is None:
            self._driver = webdriver.Chrome()
            self._driver.implicitly_wait(5)
            self._driver.maximize_window()
        else:
            self._driver = driver

    def _get_url(self,url):
        try:
            self._driver.get(url)
            config.case_log.info(f'访问{url}》success')
        except Exception as e:
            config.case_log.error(f'访问{url}》failed')
            raise e

    def _get_url_with_cookie(self,url,cookie_path=config.COOKIE_PATH):
        try:
            self._driver.get(url)
            with open(cookie_path,'r') as f:
                cookies = yaml.safe_load(f)
                for cookie in cookies:
                    self._driver.add_cookie(cookie)
                self._driver.get(url)
                config.case_log.info(f'添加cookie后访问{url}》success')
        except Exception as e:
            config.case_log.error(f'添加cookie后访问{url}》failed')
            raise e








