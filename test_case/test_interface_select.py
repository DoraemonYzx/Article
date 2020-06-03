#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:余振新
@file: test_interface_home.py
@time: 2020/04/21
"""
import unittest
from common.base_request import RequestInterface
from common.base_compare import CompareParm
import ddt
from data import interface_select_data
from public.test_case import TestCase
"""
文章中台-查询相关接口
"""


@ddt.ddt
class TestInterfaceSelect(unittest.TestCase):
    """
    查询功能相关接口
    """

    @classmethod
    def setUpClass(cls):
        cls.r = RequestInterface()
        cls.compare = CompareParm()
        cls.testcase = TestCase()

    @ddt.data(*interface_select_data.categorySelect)
    def test_01_categorySelect(self, datalist):
        """
        categorySelect--查询分类下拉框接口
        """
        result = self.testcase.test_case(datalist)
        self.assertTrue(result)

    @ddt.data(*interface_select_data.flagSelect)
    def test_02_flagSelect(self, datalist):
        """
        flagSelect--查询标签下拉框接口
        """
        result = self.testcase.test_case(datalist)
        self.assertTrue(result)

    @ddt.data(*interface_select_data.query)
    def test_03_query(self, datalist):
        """
        query--查询文章接口
        """
        result = self.testcase.test_case(datalist)
        self.assertTrue(result)

    @ddt.data(*interface_select_data.queryArtcleCategoryFlagByNo)
    def test_04_queryArtcleCategoryFlagByNo(self, datalist):
        """
        queryArtcleCategoryFlagByNo--根据文章编号查询文章分类和标签
        """
        result = self.testcase.test_case(datalist)
        self.assertTrue(result)

    @ddt.data(*interface_select_data.queryCategoryAll)
    def test_05_queryCategoryAll(self, datalist):
        """
        queryCategoryAll--查询分类列表
        """
        result = self.testcase.test_case(datalist)
        self.assertTrue(result)

    @ddt.data(*interface_select_data.queryFlagAll)
    def test_06_queryFlagAll(self, datalist):
        """
        queryFlagAll--查询标签列表
        """
        result = self.testcase.test_case(datalist)
        self.assertTrue(result)

    @ddt.data(*interface_select_data.select)
    def test_07_select(self, datalist):
        """
        select--查询文章列表
        """
        result = self.testcase.test_case(datalist)
        self.assertTrue(result)

    @ddt.data(*interface_select_data.select2)
    def test_08_select2(self, datalist):
        """
        select2--查询文章列表
        """
        result = self.testcase.test_case(datalist)
        self.assertTrue(result)

    # @ddt.data(*interface_select_data.select3)
    # def test_10_select3(self, datalist):
    #     """
    #     select3--查询文章列表（此接口已停用）
    #     """
    #     result = self.testcase.test_case(datalist)
    #     self.assertTrue(result)

    @ddt.data(*interface_select_data.selectAll)
    def test_09_selectAll(self, datalist):
        """
        selectAll--查询文章列表
        """
        result = self.testcase.test_case(datalist)
        self.assertTrue(result)

    @ddt.data(*interface_select_data.selectByArticleNo)
    def test_10_selectByArticleNo(self, datalist):
        """
        selectByArticleNo--文章编号查询某个文章
        """
        result = self.testcase.test_case(datalist)
        self.assertTrue(result)

    @ddt.data(*interface_select_data.selectById)
    def test_11_selectById(self, datalist):
        """
        selectById--文章id查询某个文章
        """
        result = self.testcase.test_case(datalist)
        self.assertTrue(result)

    @ddt.data(*interface_select_data.selectCategoryAll)
    def test_12_selectCategoryAll(self, datalist):
        """
        selectCategoryAll--中心查询分类列表
        """
        result = self.testcase.test_case(datalist)
        self.assertTrue(result)

    @ddt.data(*interface_select_data.selectCategoryAllChild)
    def test_13_selectCategoryAllChild(self, datalist):
        """
        selectCategoryAllChild--中心查询分类列表
        """
        result = self.testcase.test_case(datalist)
        self.assertTrue(result)

    @ddt.data(*interface_select_data.selectFlagAll)
    def test_14_selectFlagAll(self, datalist):
        """
        selectCategoryAllChild--中心查询分类列表
        """
        result = self.testcase.test_case(datalist)
        self.assertTrue(result)

    @ddt.data(*interface_select_data.selectFlagAllChild)
    def test_15_selectFlagAllChild(self, datalist):
        """
        selectCategoryAllChild--中心查询分类列表
        """
        result = self.testcase.test_case(datalist)
        self.assertTrue(result)
