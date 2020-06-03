#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:余振新
@file: interface_home.py
@time: 2020/04/22
"""

categorySelect = [
    {
     'interface': '查询分类下拉框接口',
     'msg': '\"categoryLevel\": \"\", \"categoryType\": \"\"',
     'url': '/interface/tArticle/categorySelect',
     'mode': 'post',
     'h': {'Content-Type': 'application/json'},
     'd': {"categoryLevel": "", "categoryType": ""},
     'code': 'code',
     'expected_code': '200',
     'expected_key': ['code', 'data', 'id', 'categoryNo', 'categoryName', 'parentCategory', 'categoryType', 'categoryLevel', 'deleteFlag',
                      'createdBy', 'createdDate', 'updatedBy', 'updatedDate'],
     },
    {
     'interface': '查询分类下拉框接口',
     'msg': '\"categoryLevel\": \"1\", \"categoryType\": \"0\"',
     'url': '/interface/tArticle/categorySelect',
     'mode': 'post',
     'h': {'Content-Type': 'application/json'},
     'd': {"categoryLevel": "1", "categoryType": "0"},
     'code': 'code',
     'expected_code': '200',
     'expected_key': ['code', 'data', 'id', 'categoryNo', 'categoryName', 'parentCategory', 'categoryType', 'categoryLevel', 'deleteFlag',
                      'createdBy', 'createdDate', 'updatedBy', 'updatedDate'],
     }
]

flagSelect = [
    {
     'interface': '查询标签下拉框接口',
     'msg': '\"flagLevel\": \"\", \"flagType\": \"\"',
     'url': '/interface/tArticle/flagSelect',
     'mode': 'post',
     'h': {'Content-Type': 'application/json'},
     'd': {"flagLevel": "", "flagType": ""},
     'code': 'code',
     'expected_code': '200',
     'expected_key': ['code', 'data', 'id', 'flagNo', 'flagName', 'parentFlag', 'flagType', 'flagLevel', 'deleteFlag',
                      'createdBy', 'createdDate', 'updatedBy', 'updatedDate'],
     },
    {
     'interface': '查询标签下拉框接口',
     'msg': '\"flagLevel\": \"1\", \"flagType\": \"0\"',
     'url': '/interface/tArticle/flagSelect',
     'mode': 'post',
     'h': {'Content-Type': 'application/json'},
     'd': {"flagLevel": "1", "flagType": "0"},
     'code': 'code',
     'expected_code': '200',
     'expected_key': ['code', 'data', 'id', 'flagNo', 'flagName', 'parentFlag', 'flagType', 'flagLevel', 'deleteFlag',
                      'createdBy', 'createdDate', 'updatedBy', 'updatedDate'],
     }
]

query = [
    {
     'interface': '查询文章接口',
     'msg': '\"currentPage\": \"1\", \"pageSize\": \"1\"',
     'url': '/interface/tArticle/query',
     'mode': 'post',
     'h': {'Content-Type': 'application/json'},
     'd': {"currentPage": "1", "pageSize": "1"},
     'code': 'code',
     'expected_code': '200',
     'expected_key': ['code', 'data', 'total', 'list', 'id', 'articleNo', 'title', 'authorName', 'content',
                      'pageSize', 'pageNum', 'size', 'pages'],
     }
]

queryArtcleCategoryFlagByNo = [
    {
     'interface': '根据文章编号查询文章分类和标签接口',
     'msg': '\"articleNo\": \"ARTICLE00002713\"',
     'url': '/interface/tArticle/queryArtcleCategoryFlagByNo',
     'mode': 'post',
     'h': {'Content-Type': 'application/x-www-form-urlencoded'},
     'd': {'articleNo': 'ARTICLE00002713'},
     'code': 'code',
     'expected_code': '200',
     'expected_key': ['code', 'data', 'articleNo', 'categoryList', 'flagList'],
     }
]

queryByPlatformNo = [
    {
     'interface': '查询该平台已上架文章接口',
     'msg': '\"articleNo\": \"ARTICLE00002713\"',
     'url': '/interface/tArticle/queryByPlatformNo',
     'mode': 'post',
     'h': {'Content-Type': 'application/json'},
     'd': {'articleNo': 'ARTICLE00002713'},
     'code': 'code',
     'expected_code': '200',
     'expected_key': ['code', 'data', 'articleNo', 'categoryList', 'categoryNo', 'categoryName'],
     }
]  # 这个接口没有用到，没写用例

queryCategoryAll = [
    {
     'interface': '查询分类列表接口',
     'msg': '\"currentPage\": \"1\",\"pageSize\": \"1\"',
     'url': '/interface/tArticle/queryCategoryAll',
     'mode': 'post',
     'h': {'Content-Type': 'application/json'},
     'd': {"currentPage": "1", "pageSize": "1"},
     'code': 'code',
     'expected_code': '200',
     'expected_key': ['code', 'data', 'list', 'categoryName', 'id', 'categoryNo'],
     }
]

queryFlagAll = [
    {
     'interface': '查询标签列表接口',
     'msg': '\"currentPage\": \"1\",\"pageSize\": \"1\"',
     'url': '/interface/tArticle/queryFlagAll',
     'mode': 'post',
     'h': {'Content-Type': 'application/json'},
     'd': {"currentPage": "1", "pageSize": "1"},
     'code': 'code',
     'expected_code': '200',
     'expected_key': ['code', 'data', 'list', 'flagNo', 'secondFlagNo', 'id'],
     }
]

select = [
    {
     'interface': '查询文章列表接口',
     'msg': '\"currentPage\": \"1\",\"pageSize\": \"1\"',
     'url': '/interface/tArticle/select',
     'mode': 'post',
     'h': {'Content-Type': 'application/json'},
     'd': {"currentPage": "1", "pageSize": "1"},
     'code': 'code',
     'expected_code': '200',
     'expected_key': ['code', 'data', 'list', 'title', 'putWay', 'id'],
     }
]

select2 = [
    {
     'interface': '查询文章列表接口',
     'msg': '\"currentPage\": \"1\",\"pageSize\": \"1\"',
     'url': '/interface/tArticle/select2',
     'mode': 'post',
     'h': {'Content-Type': 'application/json'},
     'd': {"currentPage": "1", "pageSize": "1"},
     'code': 'code',
     'expected_code': '200',
     'expected_key': ['code', 'data', 'list', 'title', 'putWay', 'id'],
     }
]

select3 = [
    {
     'interface': '查询文章列表接口',
     'msg': '\"currentPage\": \"1\",\"pageSize\": \"1\"',
     'url': '/interface/tArticle/select3',
     'mode': 'post',
     'h': {'Content-Type': 'application/json'},
     'd': {"currentPage": "1", "pageSize": "1"},
     'code': 'code',
     'expected_code': '200',
     'expected_key': ['code', 'data', 'list', 'title', 'putWay', 'id'],
     }
]  # 已经不用了

selectAll = [
    {
     'interface': '查询文章列表接口',
     'msg': '\"currentPage\": \"1\",\"pageSize\": \"1\"',
     'url': '/interface/tArticle/selectAll',
     'mode': 'post',
     'h': {'Content-Type': 'application/json'},
     'd': {"currentPage": "1", "pageSize": "1"},
     'code': 'code',
     'expected_code': '200',
     'expected_key': ['code', 'data', 'list', 'title', 'putWay', 'id'],
     }
]

selectByArticleNo = [
    {
     'interface': '文章编号查询某个文章接口',
     'msg': '\"articleNo\": \"ARTICLE00002713\"',
     'url': '/interface/tArticle/selectByArticleNo',
     'mode': 'post',
     'h': {'Content-Type': 'application/json'},
     'd': {"articleNo": "ARTICLE00002713"},
     'code': 'code',
     'expected_code': '200',
     'expected_key': ['code', 'data', 'title', 'articleNo', 'authorName', 'id'],
     }
]

selectById = [
    {
     'interface': '查询某个文章接口',
     'msg': '\"id\": \"1468\"',
     'url': '/interface/tArticle/selectById',
     'mode': 'post',
     'h': {'Content-Type': 'application/json'},
     'd': {"id": "1468"},
     'code': 'code',
     'expected_code': '200',
     'expected_key': ['code', 'data', 'title', 'articleNo', 'authorName', 'id'],
     }
]

selectCategoryAll = [
    {
     'interface': '中心查询分类列表接口',
     'msg': '\"currentPage\": \"1\",\"pageSize\": \"1\"',
     'url': '/interface/tArticle/selectCategoryAll',
     'mode': 'post',
     'h': {'Content-Type': 'application/json'},
     'd': {"currentPage": "1", "pageSize": "1"},
     'code': 'code',
     'expected_code': '200',
     'expected_key': ['code', 'data', 'list', 'categoryLevel', 'categoryNo', 'id'],
     }
]

selectCategoryAllChild = [
    {
     'interface': '中心查询分类列表接口',
     'msg': '没有入参',
     'url': '/interface/tArticle/selectCategoryAllChild',
     'mode': 'post',
     'h': {'Content-Type': 'application/json'},
     'd': {},
     'code': 'code',
     'expected_code': '200',
     'expected_key': ['code', 'data', 'categoryName', 'categoryLevel', 'categoryNo', 'id', 'children'],
     }
]

selectFlagAll = [
    {
     'interface': '中心查询标签列表接口',
     'msg': '\"currentPage\": \"1\",\"pageSize\": \"1\"',
     'url': '/interface/tArticle/selectFlagAll',
     'mode': 'post',
     'h': {'Content-Type': 'application/json'},
     'd': {"currentPage": "1", "pageSize": "1"},
     'code': 'code',
     'expected_code': '200',
     'expected_key': ['code', 'data', 'list', 'flagNo', 'total', 'id'],
     }
]

selectFlagAllChild = [
    {
     'interface': '中心查询标签列表接口',
     'msg': '没有入参',
     'url': '/interface/tArticle/selectFlagAllChild',
     'mode': 'post',
     'h': {'Content-Type': 'application/json'},
     'd': {},
     'code': 'code',
     'expected_code': '200',
     'expected_key': ['code', 'data', 'flagLevel', 'flagName', 'id', 'children', 'flagNo'],
     }
]
