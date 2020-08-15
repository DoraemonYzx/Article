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

    @ddt.data(*interface_select_data.queryHotArticleList)
    def test_05_queryHotArticleList(self, datalist):
        """
        queryHotArticleList--查询(上架时间)一个月内的文章/ 阅读量前15 / 绑定医生的所有文章
        """
        result = self.testcase.test_case(datalist)
        self.assertTrue(result)

    @ddt.data(*interface_select_data.selectAllListNew)
    def test_06_selectAllListNew(self, datalist):
        """
        selectAllListNew--查询文章列表_新
        """
        result = self.testcase.test_case(datalist)
        self.assertTrue(result)

    @ddt.data(*interface_select_data.selectAllPageNew)
    def test_07_selectAllPageNew(self, datalist):
        """
        selectAllPageNew--查询文章分页_新

        """
        result = self.testcase.test_case(datalist)
        self.assertTrue(result)

    @ddt.data(*interface_select_data.selectListNew)
    def test_08_selectListNew(self, datalist):
        """
        selectListNew--查询文章列表_新
        """
        result = self.testcase.test_case(datalist)
        self.assertTrue(result)

    @ddt.data(*interface_select_data.selectPageNew)
    def test_09_selectPageNew(self, datalist):
        """
        selectPageNew--查询文章分页_新

        """
        result = self.testcase.test_case(datalist)
        self.assertTrue(result)

    @ddt.data(*interface_select_data.selectArticleFlag)
    def test_10_selectArticleFlag(self, datalist):
        """
        selectArticleFlag--查询文章的标签

        """
        result = self.testcase.test_case(datalist)
        self.assertTrue(result)

    @ddt.data(*interface_select_data.selectArticleImage)
    def test_11_selectArticleImage(self, datalist):
        """
        selectArticleImage--查询文章的图片

        """
        result = self.testcase.test_case(datalist)
        self.assertTrue(result)

    @ddt.data(*interface_select_data.queryCategoryCount)
    def test_12_queryCategoryCount(self, datalist):
        """
        queryCategoryCount--根据分类查询各分类文章数量
        """
        result = self.testcase.test_case(datalist)
        self.assertTrue(result)

    @ddt.data(*interface_select_data.queryArticleListByArticleNos)
    def test_13_queryArticleListByArticleNos(self, datalist):
        """
        queryArticleListByArticleNos--根据文章编号查询文章标题
        """
        result = self.testcase.test_case(datalist)
        self.assertTrue(result)

    @ddt.data(*interface_select_data.queryCategoryAll)
    def test_14_queryCategoryAll(self, datalist):
        """
        queryCategoryAll--查询分类列表
        """
        result = self.testcase.test_case(datalist)
        self.assertTrue(result)

    @ddt.data(*interface_select_data.queryFlagAll)
    def test_15_queryFlagAll(self, datalist):
        """
        queryFlagAll--查询标签列表
        """
        result = self.testcase.test_case(datalist)
        self.assertTrue(result)

    @ddt.data(*interface_select_data.select)
    def test_16_select(self, datalist):
        """
        select--查询文章列表
        """
        result = self.testcase.test_case(datalist)
        self.assertTrue(result)

    # @ddt.data(*interface_select_data.select2)
    # def test_08_select2(self, datalist):
    #     """
    #     select2--查询文章列表
    #     """
    #     result = self.testcase.test_case(datalist)
    #     self.assertTrue(result)

    # @ddt.data(*interface_select_data.select3)
    # def test_10_select3(self, datalist):
    #     """
    #     select3--查询文章列表（此接口已停用）
    #     """
    #     result = self.testcase.test_case(datalist)
    #     self.assertTrue(result)

    @ddt.data(*interface_select_data.selectAll)
    def test_17_selectAll(self, datalist):
        """
        selectAll--查询文章列表
        """
        result = self.testcase.test_case(datalist)
        self.assertTrue(result)

    @ddt.data(*interface_select_data.selectByArticleNo)
    def test_18_selectByArticleNo(self, datalist):
        """
        selectByArticleNo--文章编号查询某个文章
        """
        result = self.testcase.test_case(datalist)
        self.assertTrue(result)

    @ddt.data(*interface_select_data.selectById)
    def test_19_selectById(self, datalist):
        """
        selectById--文章id查询某个文章
        """
        result = self.testcase.test_case(datalist)
        self.assertTrue(result)

    @ddt.data(*interface_select_data.selectCategoryAll)
    def test_20_selectCategoryAll(self, datalist):
        """
        selectCategoryAll--中心查询分类列表
        """
        result = self.testcase.test_case(datalist)
        self.assertTrue(result)

    @ddt.data(*interface_select_data.selectCategoryAllChild)
    def test_21_selectCategoryAllChild(self, datalist):
        """
        selectCategoryAllChild--中心查询分类列表
        """
        result = self.testcase.test_case(datalist)
        self.assertTrue(result)

    @ddt.data(*interface_select_data.selectFlagAll)
    def test_22_selectFlagAll(self, datalist):
        """
        selectFlagAll--中心查询标签列表
        """
        result = self.testcase.test_case(datalist)
        self.assertTrue(result)

    @ddt.data(*interface_select_data.selectFlagAllChild)
    def test_23_selectFlagAllChild(self, datalist):
        """
        selectFlagAllChild--中心查询标签列表
        """
        result = self.testcase.test_case(datalist)
        self.assertTrue(result)

    @ddt.data(*interface_select_data.findArticleReadTimes)
    def test_24_findArticleReadTimes(self, datalist):
        """
        findArticleReadTimes2--正确的文章编号查询阅读量
        """
        result = self.testcase.test_case(datalist)
        self.assertTrue(result)

    @ddt.data(*interface_select_data.findArticleReadTimes2)
    def test_25_findArticleReadTimes2(self, datalist):
        """
        findArticleReadTimes2--错误的文章编号查询阅读量
        """
        result = self.testcase.test_case(datalist)
        self.assertTrue(result)

    @ddt.data(*interface_select_data.getWxConfig)
    def test_26_getWxConfig(self, datalist):
        """
        getWxConfig--查询文章微信分享参数
        """
        result = self.testcase.test_case(datalist)
        self.assertTrue(result)


if __name__ == '__main__':
    test = unittest.TestSuite()
    test.addTest(TestInterfaceSelect('test_04_queryArtcleCategoryFlagByNo'))
    unittest.TextTestRunner(verbosity=2).run(test)
