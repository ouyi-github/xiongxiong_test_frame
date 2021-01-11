#! /usr/bin/python
# -*- coding: utf-8 -*-

import logging
class MyLogger:
    """
    自定义logging类
    """
    def __init__(self,name,path,level,format):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.DEBUG)
        self.path = path
        self.level = level
        self.format = format

    def get_logger(self):
        """
        生成一个FileHandler
        :return:
        """
        if not self.logger.hasHandlers():
            file_handler = logging.FileHandler(self.path,encoding='utf-8')
            file_handler.setLevel(self.level)
            file_handler.setFormatter(self.format)
            self.logger.addHandler(file_handler)
        else:
            self.logger = self.logger
        return self.logger


if __name__ == "__main__":
    from app_frame.my_configs import config
    # 生成一个logger实例
    case_log = MyLogger(name='caselog', path=config.logger_path, level=config.logger_level, format=config.logger_format).get_logger()
    case_log.info('success')
    case_log.error('failed')

