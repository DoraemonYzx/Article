#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:余振新
@file: test_interface_home.py
@time: 2020/04/21
"""
import unittest
import time
from common.base_request import RequestInterface
from common.base_compare import CompareParm
import json
import ddt
from data import interface_insert_delete_update_data
from public.test_case import TestCase
"""
文章中台-增删改相关接口
"""


@ddt.ddt
class TestInterfaceInsertDeleteUpdate(unittest.TestCase):
    """
    增删改功能相关接口
    """

    @classmethod
    def setUpClass(cls):
        cls.r = RequestInterface()
        cls.compare = CompareParm()
        cls.testcase = TestCase()
        cls.timeNow = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        cls.categoryNo1 = ""  # 一级分类categoryNo
        cls.categoryid1 = ""  # 一级分类id
        cls.categoryNo2 = ""  # 二级分类categoryNo
        cls.categoryid1 = ""  # 二级分类id
        cls.flagNo1 = ""  # 一级标签flagNo
        cls.flagid1 = ""  # 一级标签id
        cls.flagNo2 = ""  # 二级标签flagNo
        cls.flagid1 = ""  # 二级标签id
        cls.articleid = ""  # 文章id

    @ddt.data(*interface_insert_delete_update_data.categoryInsert)
    def test_01_categoryInsert(self, datalist):
        """
        categoryInsert--新增一级分类
        """
        datalist['d']['categoryName'] = datalist['d']['categoryName']+TestInterfaceInsertDeleteUpdate.timeNow
        result = self.testcase.test_case(datalist)
        response = self.testcase.response
        TestInterfaceInsertDeleteUpdate.categoryNo1 = json.loads(response['data'])['data']['categoryNo']
        TestInterfaceInsertDeleteUpdate.categoryid1 = json.loads(response['data'])['data']['id']
        print("新增的一级分类categoryNo是：%s\n新增的一级分类id是：%s" %
              (TestInterfaceInsertDeleteUpdate.categoryNo1, TestInterfaceInsertDeleteUpdate.categoryid1))
        self.assertTrue(result)

    @ddt.data(*interface_insert_delete_update_data.categoryInsert2)
    def test_02_categoryInsert2(self, datalist):
        """
        categoryInsert--新增二级分类
        """
        print("之前新增的一级父分类categoryNo是：%s" % TestInterfaceInsertDeleteUpdate.categoryNo1)
        datalist['d']['categoryName'] = datalist['d']['categoryName'] + TestInterfaceInsertDeleteUpdate.timeNow
        datalist['d']['parentCategory'] = TestInterfaceInsertDeleteUpdate.categoryNo1
        result = self.testcase.test_case(datalist)
        response = self.testcase.response
        TestInterfaceInsertDeleteUpdate.categoryNo2 = json.loads(response['data'])['data']['categoryNo']
        TestInterfaceInsertDeleteUpdate.categoryid2 = json.loads(response['data'])['data']['id']
        print("新增的二级分类categoryNo是：%s\n新增的二级分类id是：%s" %
              (TestInterfaceInsertDeleteUpdate.categoryNo2, TestInterfaceInsertDeleteUpdate.categoryid2))
        self.assertTrue(result)

    @ddt.data(*interface_insert_delete_update_data.categoryUpdate)
    def test_03_categoryUpdate(self, datalist):
        """
        categoryUpdate--修改一级分类
        """
        print("之前新增的一级父分类id是：%s" % TestInterfaceInsertDeleteUpdate.categoryid1)
        datalist['d']['categoryName'] = datalist['d']['categoryName'] + TestInterfaceInsertDeleteUpdate.timeNow
        datalist['d']['id'] = TestInterfaceInsertDeleteUpdate.categoryid1
        result = self.testcase.test_case(datalist)
        self.assertTrue(result)

    @ddt.data(*interface_insert_delete_update_data.categoryUpdate2)
    def test_04_categoryUpdate2(self, datalist):
        """
        categoryUpdate--修改二级分类
        """
        print("之前新增的一级父分类id是：%s" % TestInterfaceInsertDeleteUpdate.categoryid2)
        datalist['d']['categoryName'] = datalist['d']['categoryName'] + TestInterfaceInsertDeleteUpdate.timeNow
        datalist['d']['id'] = TestInterfaceInsertDeleteUpdate.categoryid2
        result = self.testcase.test_case(datalist)
        self.assertTrue(result)

    @ddt.data(*interface_insert_delete_update_data.categoryDelete2)
    def test_05_categoryDelete2(self, datalist):
        """
        categoryDelete--删除二级分类
        """
        print("之前新增的一级分类id是：%s" % TestInterfaceInsertDeleteUpdate.categoryid2)
        datalist['d']['id'] = TestInterfaceInsertDeleteUpdate.categoryid2
        result = self.testcase.test_case(datalist)
        self.assertTrue(result)

    @ddt.data(*interface_insert_delete_update_data.categoryDelete)
    def test_06_categoryDelete(self, datalist):
        """
        categoryDelete--删除一级分类
        """
        print("之前新增的一级分类id是：%s" % TestInterfaceInsertDeleteUpdate.categoryid1)
        datalist['d']['id'] = TestInterfaceInsertDeleteUpdate.categoryid1
        result = self.testcase.test_case(datalist)
        self.assertTrue(result)

    @ddt.data(*interface_insert_delete_update_data.flagInsert)
    def test_07_flagInsert(self, datalist):
        """
        flagInsert--新增一级标签
        """
        datalist['d']['flagName'] = datalist['d']['flagName'] + TestInterfaceInsertDeleteUpdate.timeNow
        result = self.testcase.test_case(datalist)
        response = self.testcase.response
        TestInterfaceInsertDeleteUpdate.flagNo1 = json.loads(response['data'])['data']['flagNo']
        TestInterfaceInsertDeleteUpdate.flagid1 = json.loads(response['data'])['data']['id']
        print("新增的一级标签flagNo是：%s\n新增的一级标签id是：%s" %
              (TestInterfaceInsertDeleteUpdate.flagNo1, TestInterfaceInsertDeleteUpdate.flagid1))
        self.assertTrue(result)

    @ddt.data(*interface_insert_delete_update_data.flagInsert2)
    def test_08_flagInsert2(self, datalist):
        """
        flagInsert--新增二级分类
        """
        print("之前新增的一级父分类flagNo是：%s" % TestInterfaceInsertDeleteUpdate.flagNo1)
        datalist['d']['flagName'] = datalist['d']['flagName'] + TestInterfaceInsertDeleteUpdate.timeNow
        datalist['d']['parentFlag'] = TestInterfaceInsertDeleteUpdate.flagNo1
        result = self.testcase.test_case(datalist)
        response = self.testcase.response
        TestInterfaceInsertDeleteUpdate.flagNo2 = json.loads(response['data'])['data']['flagNo']
        TestInterfaceInsertDeleteUpdate.flagid2 = json.loads(response['data'])['data']['id']
        print("新增的二级标签flagNo是：%s\n新增的二级标签id是：%s" %
              (TestInterfaceInsertDeleteUpdate.flagNo2, TestInterfaceInsertDeleteUpdate.flagid2))
        self.assertTrue(result)

    @ddt.data(*interface_insert_delete_update_data.flagUpdate)
    def test_09_flagUpdate(self, datalist):
        """
        flagUpdate--修改一级标签
        """
        print("之前新增的一级父标签id是：%s" % TestInterfaceInsertDeleteUpdate.flagid1)
        datalist['d']['flagName'] = datalist['d']['flagName'] + TestInterfaceInsertDeleteUpdate.timeNow
        datalist['d']['id'] = TestInterfaceInsertDeleteUpdate.flagid1
        result = self.testcase.test_case(datalist)
        self.assertTrue(result)

    @ddt.data(*interface_insert_delete_update_data.flagUpdate2)
    def test_10_flagUpdate2(self, datalist):
        """
        flagUpdate--修改二级标签
        """
        print("之前新增的一级父标签id是：%s" % TestInterfaceInsertDeleteUpdate.flagid2)
        datalist['d']['flagName'] = datalist['d']['flagName'] + TestInterfaceInsertDeleteUpdate.timeNow
        datalist['d']['id'] = TestInterfaceInsertDeleteUpdate.flagid2
        result = self.testcase.test_case(datalist)
        self.assertTrue(result)

    @ddt.data(*interface_insert_delete_update_data.flagDelete2)
    def test_11_flagDelete2(self, datalist):
        """
        flagDelete--删除二级标签
        """
        print("之前新增的一级分类id是：%s" % TestInterfaceInsertDeleteUpdate.flagid2)
        datalist['d']['id'] = TestInterfaceInsertDeleteUpdate.flagid2
        result = self.testcase.test_case(datalist)
        self.assertTrue(result)

    @ddt.data(*interface_insert_delete_update_data.flagDelete)
    def test_12_flagDelete(self, datalist):
        """
        flagDelete--删除一级标签
        """
        print("之前新增的一级分类id是：%s" % TestInterfaceInsertDeleteUpdate.flagid1)
        datalist['d']['id'] = TestInterfaceInsertDeleteUpdate.flagid1
        result = self.testcase.test_case(datalist)
        self.assertTrue(result)

    @ddt.data(*interface_insert_delete_update_data.insert)
    def test_13_insert(self, datalist):
        """
        insert--新增文章
        """
        datalist['d']['content'] = datalist['d']['content']+TestInterfaceInsertDeleteUpdate.timeNow
        datalist['d']['title'] = datalist['d']['title'] + TestInterfaceInsertDeleteUpdate.timeNow
        result = self.testcase.test_case(datalist)
        response = self.testcase.response
        TestInterfaceInsertDeleteUpdate.articleid = json.loads(response['data'])['data']['id']
        print("新增的文章id是：%s" % TestInterfaceInsertDeleteUpdate.articleid)
        self.assertTrue(result)

    @ddt.data(*interface_insert_delete_update_data.update)
    def test_14_update(self, datalist):
        """
        update--修改文章
        """
        print("之前新增的文章id是：%s" % TestInterfaceInsertDeleteUpdate.articleid)
        datalist['d']['content'] = datalist['d']['content'] + TestInterfaceInsertDeleteUpdate.timeNow
        datalist['d']['title'] = datalist['d']['title'] + TestInterfaceInsertDeleteUpdate.timeNow
        datalist['d']['id'] = TestInterfaceInsertDeleteUpdate.articleid
        result = self.testcase.test_case(datalist)
        self.assertTrue(result)

    @ddt.data(*interface_insert_delete_update_data.onshelf)
    def test_15_onshelf(self, datalist):
        """
        onshelf--上架文章
        """
        print("之前新增的文章id是：%s" % TestInterfaceInsertDeleteUpdate.articleid)
        datalist['d']['id'] = TestInterfaceInsertDeleteUpdate.articleid
        result = self.testcase.test_case(datalist)
        self.assertTrue(result)

    @ddt.data(*interface_insert_delete_update_data.onshelf2)
    def test_16_onshelf2(self, datalist):
        """
        onshelf--下架文章
        """
        print("之前新增的文章id是：%s" % TestInterfaceInsertDeleteUpdate.articleid)
        datalist['d']['id'] = TestInterfaceInsertDeleteUpdate.articleid
        result = self.testcase.test_case(datalist)
        self.assertTrue(result)

    @ddt.data(*interface_insert_delete_update_data.changePutWay)
    def test_17_changePutWay(self, datalist):
        """
        onshelf--上架文章
        """
        print("之前新增的文章id是：%s" % TestInterfaceInsertDeleteUpdate.articleid)
        datalist['d']['articleIdStr'] = TestInterfaceInsertDeleteUpdate.articleid
        result = self.testcase.test_case(datalist)
        self.assertTrue(result)

    @ddt.data(*interface_insert_delete_update_data.changePutWay2)
    def test_18_changePutWay2(self, datalist):
        """
        onshelf--下架文章
        """
        print("之前新增的文章id是：%s" % TestInterfaceInsertDeleteUpdate.articleid)
        datalist['d']['articleIdStr'] = TestInterfaceInsertDeleteUpdate.articleid
        result = self.testcase.test_case(datalist)
        self.assertTrue(result)

    @ddt.data(*interface_insert_delete_update_data.delete)
    def test_19_delete(self, datalist):
        """
        delete--删除文章
        """
        print("之前新增的文章id是：%s" % TestInterfaceInsertDeleteUpdate.articleid)
        datalist['d']['id'] = TestInterfaceInsertDeleteUpdate.articleid
        result = self.testcase.test_case(datalist)
        self.assertTrue(result)
