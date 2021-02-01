#! /usr/bin/python
# -*- coding: utf-8 -*-
# author: ouyi
# createtime: 2021-02-01
from typing import List

from api_frame.page_obj.base_page import BasePage


class ContactPage(BasePage):
    """
    通讯录管理相关接口封装
    """

    def add_remenber(self,userid:str,name:str,mobile:str,department:List[int],**kwargs):
        """
        添加成员接口封装
        :param userid: 成员UserID，必须参数。
        :param name: 成员名称。必须参数。
        :param mobile: 手机号码。企业内必须唯一，mobile/email二者不能同时为空
        :param department: 成员所属部门id列表,不超过100个
        :param kwargs:
        :return: 接口返回对象
        """
        json_data = {
            "userid": userid,
            "name": name,
            "mobile": mobile,
            "department": department
        }
        r = self.session.post(url='https://qyapi.weixin.qq.com/cgi-bin/user/create',json=json_data)
        return r

    def find_remenber(self,userid):
        """
        查询成员接口封装
        :param userid: 成员UserID。对应管理端的帐号，企业内必须唯一。不区分大小写，长度为1~64个字节
        :return: 接口返回对象
        """
        params = {
            "userid": userid
        }
        r = self.session.get(url='https://qyapi.weixin.qq.com/cgi-bin/user/get',params=params)
        return r

    def delete_remenber(self,userid):
        """
        删除成员接口封装
        :param userid: 成员UserID。对应管理端的帐号，企业内必须唯一。不区分大小写，长度为1~64个字节
        :return: 接口返回对象
        """
        params = {
            "userid": userid
        }
        r = self.session.get(url='https://qyapi.weixin.qq.com/cgi-bin/user/delete',params=params)
        return r


