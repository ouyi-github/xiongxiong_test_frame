#! /usr/bin/python
# -*- coding: utf-8 -*-

from datetime import datetime

def get_now_time():
    """
    获取当前时间字符串
    :return:
    """
    now = datetime.now().strftime('%Y-%m-%d-%H%M%S')
    return now


if __name__ == "__main__":
    print(get_now_time())
