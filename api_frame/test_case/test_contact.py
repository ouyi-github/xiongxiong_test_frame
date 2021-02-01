#! /usr/bin/python
# -*- coding: utf-8 -*-
# author: ouyi
# create_time: 2021-01-29

import pytest
from api_frame.page_obj.contact_page import ContactPage


class TestContact:
    def setup_class(self):
        self.contact = ContactPage()


    @pytest.mark.parametrize("userid,name,mobile,department",[('wsdsb_add001','wsdsb_add001','13118176666',[1]),
                                                              ('wsdsb_add002','wsdsb_add002','13118176667',[2,3]),
                                                              ('wsdsb_add003','wsdsb_add003','13118176668',[1,2,3,4,5]),
                                                              ('wsdsb_add004','wsdsb_add004','13118176669',[1]),
                                                              ('wsdsb_add005','wsdsb_add005','13118176661',[1])])
    def test_addremenber(self,userid,name,mobile,department):
        """添加成员接口测试用例"""
        # 添加成员接口测试
        r = self.contact.add_remenber(userid=userid,name=name,mobile=mobile,department=department)
        assert r.json()['errcode'] == 0
        assert r.json()['errmsg'] == 'created'
        # 清理数据
        self.contact.delete_remenber(userid=userid)


    @pytest.mark.parametrize("userid,name,mobile,department", [('wsdsb_find001', 'wsdsb_find001', '13118177666', [1]),
                                                               ('wsdsb_find002', 'wsdsb_find002', '13118177667', [2, 3]),
                                                               ('wsdsb_find003', 'wsdsb_find003', '13118177668',[1, 2, 3, 4, 5]),
                                                               ('wsdsb_find004', 'wsdsb_find004', '13118177669', [1]),
                                                               ('wsdsb_find005', 'wsdsb_find005', '13118177661', [1])])
    def test_findremenber(self,userid,name,mobile,department):
        """查询成员接口测试用例"""
        # 生成测试数据
        self.contact.add_remenber(userid=userid,name=name,mobile=mobile,department=department)
        # 查询成员接口测试
        r = self.contact.find_remenber(userid=userid)
        assert r.json()['errcode'] == 0
        assert r.json()['errmsg'] == 'ok'
        assert r.json()['userid'] == userid
        assert r.json()['name'] == name
        assert set(r.json()['department']) == set(department)
        assert r.json()['mobile'] == mobile
        # 清理测试数据
        self.contact.delete_remenber(userid=userid)



    @pytest.mark.parametrize("userid,name,mobile,department", [('wsdsb_delete001', 'wsdsb_delete001', '13118178666', [1]),
                                                               ('wsdsb_delete002', 'wsdsb_delete002', '13118178667', [2, 3]),
                                                               ('wsdsb_delete003', 'wsdsb_delete003', '13118178668',[1, 2, 3, 4, 5]),
                                                               ('wsdsb_delete004', 'wsdsb_delete004', '13118178669', [1]),
                                                               ('wsdsb_delete005', 'wsdsb_delete005', '13118178661', [1])])
    def test_deleteremenber(self,userid,name,mobile,department):
        """删除成员接口测试用例"""
        # 生成测试数据
        self.contact.add_remenber(userid=userid, name=name, mobile=mobile, department=department)
        # 成员删除接口测试
        r = self.contact.delete_remenber(userid=userid)
        assert r.json()['errcode'] == 0
        assert r.json()['errmsg'] == 'deleted'




if __name__ == "__main__":
    pytest.main(['test_contact.py','-n auto'])
