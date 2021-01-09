#! usr/bin/python
# -*- coding:utf-8 -*-
# author : ouyi
# create_time : 2021-01-09

from functools import wraps

from app_frame.my_configs import config


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
