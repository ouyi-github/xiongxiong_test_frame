#! /usr/bin/python
# -*- coding: utf-8 -*-
import os
from configparser import ConfigParser

import yaml


def get_data_from_ini(node,key):
    """
    封装：获取element.ini文件方法
    :return:
    """
    from app_frame.my_configs import config
    path = os.path.join(config.BASE_DIR,'data/element.ini')
    target = ConfigParser()
    target.read(path,encoding='utf-8')
    result = target.get(node,key)
    result = result.split('|')
    return result


def get_data_from_yaml(path):
    """
    获取指定yaml文件的内容
    :param path:
    :return:
    """

    with open(path,'r',encoding='utf-8') as f:
        result = yaml.safe_load(f)
        return result


if __name__ == "__main__":
    print(get_data_from_ini(node='main', key='goto_address'))
    # from app_frame.my_configs import config
    # s = get_data_from_yaml(os.path.join(config.BASE_DIR,'data/case_data/add_remenber.yaml'))
    # print(s)

