#! /usr/bin/python
# -*- coding: utf-8 -*-
import os
def get_base_dir():
    """
    获取项目根目录
    :return:
    """
    now_dir = os.getcwd()
    while True:
        now_dir_list = os.path.split(now_dir)
        now_dir = now_dir_list[0]
        if now_dir_list[1] == "xiongxiong_test_frame":
            now_dir = os.path.join(now_dir_list[0], now_dir_list[1])
            break
    return os.path.join(now_dir,'web_frame')



if __name__ == "__main__":
    print(get_base_dir())
