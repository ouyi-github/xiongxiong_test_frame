#! /usr/bin/python
# -*- coding: utf-8 -*-
# author : ouyi
# create_time: 2021-01-09
import os

import allure
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from app_frame.my_utils.get_data import get_data_from_yaml
from app_frame.common_decorator import black_list_find, black_list_wait
from app_frame.my_configs import config


class BasePage:
    def __init__(self,driver:WebDriver = None):
        if driver is None:
            caps = {}
            caps['platformName'] = 'Android'  # 被测设备为Android
            caps['platformVersion'] = '5.1.1'  # 被测设备系统版本
            caps['deviceName'] = '127.0.0.1:21503'  # 被测设备
            caps['appActivity'] = '.main.view.MainActivity'  # 被测app要打开的页面
            caps['appPackage'] = 'com.xueqiu.android'  # 被测app的包名
            caps['noReset'] = 'true'  # 启动时是否不重置app，可以跳过登录等
            caps['unicodeKeyboard'] = 'true'  # 设置中文输入
            caps['resetKeyboard'] = 'true'  # 设置中文输入
            self._driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',caps)
            self._driver.implicitly_wait(3)
        else:
            self._driver = driver

        self.black_list=[
            ('id','com.xueqiu.android:id/ib_close','首页活动弹窗关闭按钮'),
            ('id','com.xueqiu.android:id/iv_close','微信扫码登录页面关闭按钮'),
                         ]


    @black_list_find
    def _find_element(self,method,message,element):
        """
        二次封装查找元素方法,添加日志，黑名单操作
        :param method: example:id
        :param message: example: 'kw'
        """
        if method == "id":
            ele = self._driver.find_element(MobileBy.ID, message)
            config.case_log.info(f'find element {element} success (method={method},message={message})')
            return ele
        elif method == "name":
            ele = self._driver.find_element(MobileBy.NAME, message)
            config.case_log.info(f'find element {element} success (method={method},message={message})')
            return ele
        elif method == "xpath":
            ele = self._driver.find_element(MobileBy.XPATH, message)
            config.case_log.info(f'find element {element} success (method={method},message={message})')
            return ele
        elif method == "css":
            ele = self._driver.find_element(MobileBy.CSS_SELECTOR, message)
            config.case_log.info(f'find element {element} success (method={method},message={message})')
            return ele
        elif method == 'class':
            ele = self._driver.find_element(MobileBy.CLASS_NAME, message)
            config.case_log.info(f'find element {element} success (method={method},message={message})')
            return ele
        elif method == 'link_text':
            ele = self._driver.find_element(MobileBy.LINK_TEXT, message)
            config.case_log.info(f'find element {element} success (method={method},message={message})')
            return ele
        elif method == 'partial_link_text':
            ele = self._driver.find_element(MobileBy.PARTIAL_LINK_TEXT, message)
            config.case_log.info(f'find element {element} success (method={method},message={message})')
            return ele
        elif method == 'tag_name':
            ele = self._driver.find_element(MobileBy.TAG_NAME, message)
            config.case_log.info(f'find element {element} success (method={method},message={message})')
            return ele
        elif method == 'android_uiautomator':
            ele = self._driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,message)
            config.case_log.info(f'find element {element} success (method={method},message={message})')
            return ele
        elif method == 'accessibility':
            ele = self._driver.find_element(MobileBy.ACCESSIBILITY_ID,message)
            config.case_log.info(f'find element {element} success (method={method},message={message})')
            return ele






    def _find_elments(self,method,message,element):
        """
        二次封装查找多元素方法,添加日志功能
        :param method: example:id
        :param message: example: 'kw'
        """
        try:
            if method == "id":
                ele = self._driver.find_elements(MobileBy.ID, message)
                config.case_log.info(f'find elements {element} success (method={method},message={message})')
                return ele
            elif method == "name":
                ele = self._driver.find_elements(MobileBy.NAME, message)
                config.case_log.info(f'find elements {element} success (method={method},message={message})')
                return ele
            elif method == "xpath":
                ele = self._driver.find_elements(MobileBy.XPATH, message)
                config.case_log.info(f'find elements {element} success (method={method},message={message})')
                return ele
            elif method == "css":
                ele = self._driver.find_elements(MobileBy.CSS_SELECTOR, message)
                config.case_log.info(f'find elements {element} success (method={method},message={message})')
                return ele
            elif method == 'class':
                ele = self._driver.find_elements(MobileBy.CLASS_NAME, message)
                config.case_log.info(f'find elements {element} success (method={method},message={message})')
                return ele
            elif method == 'link_text':
                ele = self._driver.find_elements(MobileBy.LINK_TEXT, message)
                config.case_log.info(f'find elements {element} success (method={method},message={message})')
                return ele
            elif method == 'partial_link_text':
                ele = self._driver.find_elements(MobileBy.PARTIAL_LINK_TEXT, message)
                config.case_log.info(f'find elements {element} success (method={method},message={message})')
                return ele
            elif method == 'tag_name':
                ele = self._driver.find_elements(MobileBy.TAG_NAME, message)
                config.case_log.info(f'find elements {element} success (method={method},message={message})')
                return ele
            elif method == 'android_uiautomator':
                ele = self._driver.find_elements(MobileBy.ANDROID_UIAUTOMATOR,message)
                config.case_log.info(f'find elements {element} success (method={method},message={message})')
                return ele
            elif method == 'accessibility':
                ele = self._driver.find_elements(MobileBy.ACCESSIBILITY_ID,message)
                config.case_log.info(f'find elements {element} success (method={method},message={message})')
                return ele
        except Exception as e:
            config.case_log.error(f'find elements {element} failed (method={method},message={message})')
            raise e


    def _find_element_and_click(self,method,message,element):
        """
        封装查找元素并点击的方法，添加日志功能
        :return:
        """
        try:
            ele = self._find_element(method,message,element)
        except Exception as e:
            raise e
        try:
            ele.click()
            config.case_log.info(f'click element {element} success )')
        except Exception as e:
            config.case_log.error(f'click element {element} failed )')
            raise e






    def _find_element_and_sendkeys(self,method,message,element,text):
        """
        封装查找元素并输入内容的方法，添加日志功能
        :param method:
        :param message:
        :param element:
        :param text:
        :return:
        """
        try:
            ele = self._find_element(method,message,element)
        except Exception as e:
            raise e
        try:
            ele.send_keys(text)
            config.case_log.info(f'sendkeys {text} to element {element} success )')
        except Exception as e:
            config.case_log.error(f'sendkeys {text} to element {element} failed )')
            raise e

    @black_list_wait
    def _wait_element_to_click(self,method,message,element):
        """
        二次封装：显示等待方法，增加日志和黑名单功能
        :param method:
        :param message:
        :param element:
        :return:
        """
        if method == "id":
            WebDriverWait(self._driver,timeout=10).until(expected_conditions.element_to_be_clickable((MobileBy.ID,message)))
        elif method == "name":
            WebDriverWait(self._driver,timeout=10).until(expected_conditions.element_to_be_clickable((MobileBy.NAME,message)))
        elif method == "xpath":
            WebDriverWait(self._driver,timeout=10).until(expected_conditions.element_to_be_clickable((MobileBy.XPATH,message)))
        elif method == "css":
            WebDriverWait(self._driver,timeout=10).until(expected_conditions.element_to_be_clickable((MobileBy.CSS_SELECTOR,message)))
        elif method == 'class':
            WebDriverWait(self._driver,timeout=10).until(expected_conditions.element_to_be_clickable((MobileBy.CLASS_NAME,message)))
        elif method == 'link_text':
            WebDriverWait(self._driver,timeout=10).until(expected_conditions.element_to_be_clickable((MobileBy.LINK_TEXT,message)))
        elif method == 'partial_link_text':
            WebDriverWait(self._driver,timeout=10).until(expected_conditions.element_to_be_clickable((MobileBy.PARTIAL_LINK_TEXT,message)))
        elif method == 'tag_name':
            WebDriverWait(self._driver,timeout=10).until(expected_conditions.element_to_be_clickable((MobileBy.TAG_NAME,message)))
        elif method == 'android_uiautomator':
            WebDriverWait(self._driver,timeout=10).until(expected_conditions.element_to_be_clickable((MobileBy.ANDROID_UIAUTOMATOR,message)))
        elif method == 'accessibility':
            WebDriverWait(self._driver,timeout=10).until(expected_conditions.element_to_be_clickable((MobileBy.ACCESSIBILITY_ID,message)))






    def _swip_find_element(self,method,message,element):
        """
        自定义滑动查找元素
        :param method:
        :param message:
        :return:
        """
        self._driver.implicitly_wait(2)
        while True:
            ss = False
            try:
                element = self._find_element(method=method, message=message,element=element)
                ss = True
                config.case_log.info(f'swip_find_element element {element} success (method={method},message={message})')
            except:
                pass
            if ss:
                break
            w_size = self._driver.get_window_size()
            w_x = w_size['width']
            w_y = w_size['height']
            x = int(w_x) / 2
            y1 = int(w_y) * 0.8
            y2 = int(w_y) * 0.2
            action = TouchAction(self._driver)
            action.press(x=int(x), y=int(y1))
            action.move_to(x=int(x), y=int(y2))
            action.release()
            action.perform()
        return



    def _swip_find_element_and_click(self,method,message,element):
        """
        自定义滑动查找元素并点击
        :param method:
        :param message:
        :return:
        """
        self._driver.implicitly_wait(2)
        while True:
            ss = False
            try:
                element = self._find_element(method=method, message=message,element=element)
                element.click()
                ss = True
                config.case_log.info(f'swip_find_element_and_click element success (method={method},message={message})')
            except:
                pass
            if ss:
                break
            w_size = self._driver.get_window_size()
            w_x = w_size['width']
            w_y = w_size['height']
            x = int(w_x) / 2
            y1 = int(w_y) * 0.8
            y2 = int(w_y) * 0.2
            action = TouchAction(self._driver)
            action.press(x=int(x),y=int(y1))
            action.move_to(x=int(x),y=int(y2))
            action.release()
            action.perform()
        return

    def _get_toast(self):
        """
        获取页面Toast
        :return:
        """
        try:
            ele = self._driver.find_element(MobileBy.XPATH,'//*[@class="android.widget.Toast"]')
            config.case_log.info('获取页面Toast：success')
            return ele
        except Exception as e:
            config.case_log.error('获取页面Toast：error')
            raise e

    def _broswer_quit(self):
        self._driver.quit()

    def _get_screenshot(self,path):
        """
        二次封装：截图并上传allure报告的方法
        :param path:
        :return:
        """
        self._driver.get_screenshot_as_file(filename=path)
        allure.attach.file(source=path,name='失败截图', attachment_type=allure.attachment_type.PNG)

    def _load_element_yaml_action(self,path,node,*args,**kwargs):
        """
        从yaml文件中读取element信息，并遍历执行所有element
        :param path: yaml文件路径
        :param node: page页面中具体的函数名
        :return:
        """
        data = get_data_from_yaml(path)
        for step in data.get(node):
            if step['action'] == '_find_element':
                self._find_element(step['method'], step['message'], step['element'])
            elif step['action'] == '_find_elments':
                self._find_elments(step['method'], step['message'], step['element'])
            elif step['action'] == '_find_element_and_click':
                self._find_elments(step['method'], step['message'], step['element'])
            elif step['action'] == '_find_element_and_sendkeys':
                content = kwargs[step['text_key']]
                self._find_element_and_sendkeys(step['method'], step['message'], step['element'],content)
            elif step['action'] == '_wait_element_to_click':
                self._find_element_and_click(step['method'], step['message'], step['element'])
            elif step['action'] == '_swip_find_element':
                self._swip_find_element(step['method'], step['message'], step['element'])
            elif step['action'] == '_swip_find_element_and_click':
                self._swip_find_element_and_click(step['method'], step['message'], step['element'])
            elif step['action'] == '_broswer_quit':
                self._broswer_quit()
            elif step['action'] == '_get_toast':
                self._get_toast()
            else:
                config.case_log.error(f'yaml文件（{path}.{node}）中元素action: {step["action"]}未找到')
                raise Exception('yaml中元素信息填写错误')











if __name__ == "__main__":
    BasePage()._swip_find_element()





