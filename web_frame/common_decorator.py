#! usr/bin/python
# -*- coding:utf-8 -*-
# author : ouyi
# create_time : 2021-01-09
import os
import signal
import subprocess
import time
from functools import wraps

import allure
from appium.webdriver.webdriver import WebDriver

from app_frame.my_configs import config
from app_frame.my_utils.get_time import get_now_time


def black_list_find(func):
    """
    自定义装饰器：给元素定位方法增加黑名单功能
    :param func:
    :return:
    """
    @wraps(func)
    def wrapper(*args,**kwargs):
        self = args[0]
        try:
            res = func(*args,**kwargs)
        except Exception as e:
            # 添加黑名单功能，当元素查找失败时。遍历黑名单
            self._driver.implicitly_wait(1)
            config.case_log.info(f'查找元素 {args[3]} 失败，开始遍历黑名单')
            for black in self.black_list:
                black_eles = self._find_elments(*black)
                if len(black_eles) > 0:
                    black_eles[0].click()
                    config.case_log.info(f'查找黑名单元素 {black[2]} 成功')
                    return func(*args,**kwargs)
            config.case_log.error(f'遍历黑名单元素结束，未找到黑名单元素')
            config.case_log.error(f'find element {args[3]} failed (method={args[1]},message={args[2]})')
            raise e
        return res
    return wrapper


def black_list_wait(func):
    """
    自定义装饰器：给显示等待方法增加黑名单功能
    :param func:
    :return:
    """
    @wraps(func)
    def wrapper(*args,**kwargs):
        self = args[0]
        try:
            res = func(*args,**kwargs)
        except Exception as e:
            # 添加黑名单功能，当元素查找失败时。遍历黑名单
            self._driver.implicitly_wait(1)
            config.case_log.info(f'查找元素 {args[3]} 失败，开始遍历黑名单')
            for black in self.black_list:
                black_eles = self._find_elments(*black)
                if len(black_eles) > 0:
                    black_eles[0].click()
                    config.case_log.info(f'查找黑名单元素 {black[2]} 成功')
                    return func(*args,**kwargs)
            config.case_log.error(f'遍历黑名单元素结束，未找到黑名单元素')
            config.case_log.error(f'wait element {args[3]} to click failed (method={args[1]},message={args[2]})')
            raise e
        return res

    return wrapper


def get_video(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        path = os.path.join(config.BASE_DIR, 'video')
        video_name = f'{func.__name__}-{get_now_time()}.mp4'
        cmd = f'scrcpy --record {video_name}'
        p = subprocess.Popen(cmd, shell=True, cwd=path)  # 注意，这里不能使用os.system来执行，因为os.system不能手动结束命令
        time.sleep(2)
        s = func(*args,**kwargs)
        os.kill(p.pid, signal.CTRL_C_EVENT)  # 使用CTRL_C结束进程
        time.sleep(2)
        allure.attach.file(source=os.path.join(path,video_name),name='录屏',attachment_type=allure.attachment_type.MP4)
        return s

    return wrapper
