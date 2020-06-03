#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:余振新
@file: interface_home.py
@time: 2020/04/22
"""

categoryInsert = [
    {
     'interface': '分类新增一级接口',
     'msg': '\"categoryName\": \"自动化接口新增一级分类\", \"categoryType\": \"0\",\"categoryLevel\": \"1\", \"createdBy\": \"demoAdmin\"',
     'url': '/interface/tArticle/categoryInsert',
     'mode': 'post',
     'h': {'Content-Type': 'application/json'},
     'd': {"categoryName": "自动化接口新增一级分类", "categoryType": "0", "categoryLevel": "1", "createdBy": "demoAdmin"},
     'code': 'code',
     'expected_code': '200',
     'expected_key': ['code', 'data', 'id', 'categoryNo', 'categoryName', 'categoryType', 'categoryLevel', 'createdBy'],
     }
]

categoryInsert2 = [
    {
     'interface': '分类新增二级接口',
     'msg': '\"categoryName\": \"自动化接口新增二级分类\", \"categoryType\": \"0\",'
            '\"categoryLevel\": \"2\", \"createdBy\": \"demoAdmin\"， \"parentCategory\": \"刚刚通过接口新增的一级分类categoryNo\"',
     'url': '/interface/tArticle/categoryInsert',
     'mode': 'post',
     'h': {'Content-Type': 'application/json'},
     'd': {"categoryName": "自动化接口新增二级分类", "categoryType": "0", "categoryLevel": "2", "createdBy": "demoAdmin", },
     'code': 'code',
     'expected_code': '200',
     'expected_key': ['code', 'data', 'id', 'categoryNo', 'categoryName', 'categoryType', 'categoryLevel', 'createdBy'],
     }
]

categoryUpdate = [
    {
     'interface': '修改一级分类接口',
     'msg': '\"categoryName\": \"自动化接口修改后的一级分类\", \"updatedBy\": \"demoAdmin\",\"id\": \"刚刚通过接口新增的一级分类id\"',
     'url': '/interface/tArticle/categoryUpdate',
     'mode': 'post',
     'h': {'Content-Type': 'application/json'},
     'd': {"categoryName": "自动化接口修改后的一级分类", "updatedBy": "demoAdmin"},
     'code': 'code',
     'expected_code': '200',
     'expected_key': ['code', 'data', 'id', 'categoryNo', 'categoryName', 'categoryType', 'categoryLevel', 'updatedBy'],
     }
]

categoryUpdate2 = [
    {
     'interface': '修改二级分类接口',
     'msg': '\"categoryName\": \"自动化接口修改后的二级分类\", \"updatedBy\": \"demoAdmin\",\"id\": \"刚刚通过接口新增的二级分类id\"',
     'url': '/interface/tArticle/categoryUpdate',
     'mode': 'post',
     'h': {'Content-Type': 'application/json'},
     'd': {"categoryName": "自动化接口修改后的二级分类", "updatedBy": "demoAdmin"},
     'code': 'code',
     'expected_code': '200',
     'expected_key': ['code', 'data', 'id', 'categoryNo', 'categoryName', 'categoryType', 'categoryLevel', 'updatedBy'],
     }
]

categoryDelete = [
    {
     'interface': '删除一级分类接口',
     'msg': '\"updatedBy\": \"demoAdmin\",\"id\": \"刚刚通过接口新增的一级分类id\"',
     'url': '/interface/tArticle/categoryDelete',
     'mode': 'post',
     'h': {'Content-Type': 'application/x-www-form-urlencoded'},
     'd': {'updatedBy': 'demoAdmin'},
     'code': 'code',
     'expected_code': '200',
     'expected_key': ['code', 'data', 'id', 'categoryNo', 'categoryName', 'categoryType', 'categoryLevel', 'createdBy'],
     }
]

categoryDelete2 = [
    {
     'interface': '删除二级分类接口',
     'msg': '\"updatedBy\": \"demoAdmin\",\"id\": \"刚刚通过接口新增的二级分类id\"',
     'url': '/interface/tArticle/categoryDelete',
     'mode': 'post',
     'h': {'Content-Type': 'application/x-www-form-urlencoded'},
     'd': {'updatedBy': 'demoAdmin'},
     'code': 'code',
     'expected_code': '200',
     'expected_key': ['code', 'data', 'id', 'categoryNo', 'categoryName', 'categoryType', 'categoryLevel', 'createdBy'],
     }
]

flagInsert = [
    {
     'interface': '新增一级标签',
     'msg': '\"flagName\": \"自动化接口自动新增一级标签\",\"flagType\": \"0\",\"flagLevel\": \"1\",\"createdBy\": \"demoAdmin\"',
     'url': '/interface/tArticle/flagInsert',
     'mode': 'post',
     'h': {'Content-Type': 'application/json'},
     'd': {"createdBy": "demoAdmin", "flagLevel": "1", "flagName": "自动化接口自动新增一级标签", "flagType": "0"},
     'code': 'code',
     'expected_code': '200',
     'expected_key': ['code', 'data', 'id', 'flagNo', 'flagName', 'flagType', 'flagLevel', 'createdBy'],
     }
]

flagInsert2 = [
    {
     'interface': '新增二级标签',
     'msg': '\"flagName\": \"自动化接口自动新增二级标签\",\"flagType\": \"0\",\"flagLevel\": \"2\",'
            '\"createdBy\": \"demoAdmin\",\"parentFlag\": \"刚刚新增的一级标签flagNo\"',
     'url': '/interface/tArticle/flagInsert',
     'mode': 'post',
     'h': {'Content-Type': 'application/json'},
     'd': {"createdBy": "demoAdmin", "flagLevel": "2", "flagName": "自动化接口自动新增二级标签", "flagType": "0"},
     'code': 'code',
     'expected_code': '200',
     'expected_key': ['code', 'data', 'id', 'flagNo', 'flagName', 'flagType', 'flagLevel', 'createdBy'],
     }
]

flagUpdate = [
    {
     'interface': '修改一级标签接口',
     'msg': '\"flagName\": \"自动化接口修改后的一级标签\", \"updatedBy\": \"demoAdmin\",\"id\": \"刚刚通过接口新增的一级标签id\"',
     'url': '/interface/tArticle/flagUpdate',
     'mode': 'post',
     'h': {'Content-Type': 'application/json'},
     'd': {"flagName": "自动化接口修改后的一级标签", "updatedBy": "demoAdmin"},
     'code': 'code',
     'expected_code': '200',
     'expected_key': ['code', 'data', 'id', 'flagNo', 'flagName', 'flagType', 'flagLevel', 'updatedBy'],
     }
]

flagUpdate2 = [
    {
     'interface': '修改二级标签接口',
     'msg': '\"flagName\": \"自动化接口修改后的二级标签\", \"updatedBy\": \"demoAdmin\",\"id\": \"刚刚通过接口新增的二级标签id\"',
     'url': '/interface/tArticle/flagUpdate',
     'mode': 'post',
     'h': {'Content-Type': 'application/json'},
     'd': {"flagName": "自动化接口修改后的二级标签", "updatedBy": "demoAdmin"},
     'code': 'code',
     'expected_code': '200',
     'expected_key': ['code', 'data', 'id', 'flagNo', 'flagName', 'flagType', 'flagLevel', 'updatedBy'],
     }
]

flagDelete = [
    {
     'interface': '删除一级标签接口',
     'msg': '\"updatedBy\": \"demoAdmin\",\"id\": \"刚刚通过接口新增的一级标签id\"',
     'url': '/interface/tArticle/flagDelete',
     'mode': 'post',
     'h': {'Content-Type': 'application/x-www-form-urlencoded'},
     'd': {'updatedBy': 'demoAdmin'},
     'code': 'code',
     'expected_code': '200',
     'expected_key': ['code', 'data', 'id', 'flagNo', 'flagName', 'flagType', 'flagLevel', 'updatedBy'],
     }
]

flagDelete2 = [
    {
     'interface': '删除二级标签接口',
     'msg': '\"updatedBy\": \"demoAdmin\",\"id\": \"刚刚通过接口新增的二级标签id\"',
     'url': '/interface/tArticle/flagDelete',
     'mode': 'post',
     'h': {'Content-Type': 'application/x-www-form-urlencoded'},
     'd': {'updatedBy': 'demoAdmin'},
     'code': 'code',
     'expected_code': '200',
     'expected_key': ['code', 'data', 'id', 'flagNo', 'flagName', 'flagType', 'flagLevel', 'updatedBy'],
     }
]

insert = [
    {
     'interface': '新增文章接口',
     'msg': '\"authorName\": \"yuzhenxin\",\"categoryNoStr\": \"CATEGORY00000183\",\"content\": \"自动化接口新增的文章内容\",'
            '\"createdBy\": \"demoAdmin\",\"linkUrl\": \"图片地址\",\"putWay\": \"0\",\"title\": \"自动化接口新增的文章标题\"',
     'url': '/interface/tArticle/insert',
     'mode': 'post',
     'h': {'Content-Type': 'application/json'},
     'd': {"authorName": "yuzhenxin", "categoryNoStr": "CATEGORY00000183", "content": "自动化接口新增的文章内容", "createdBy": "demoAdmin",
           "linkUrl": "https://cxjktest.oss-cn-shanghai.aliyuncs.com/article/2020/06/0ffc2c7c-6858-4036-9558-bdfc93ae1f9e.jpg",
           "putWay": "0", "title": "自动化接口新增的文章标题"},
     'code': 'code',
     'expected_code': '200',
     'expected_key': ['code', 'data', 'id', 'articleNo', 'title', 'authorName', 'content', 'putWay', 'linkUrl', 'createdBy'],
     }
]

update = [
    {
     'interface': '修改文章接口',
     'msg': '\"authorName\": \"yuzhenxin\",\"categoryNoStr\": \"CATEGORY00000183\",\"content\": \"自动化接口修改的文章内容\",'
            '\"updatedBy\": \"demoAdmin\",\"linkUrl\": \"图片地址\",\"putWay\": \"0\",\"title\": \"自动化接口修改的文章标题\",'
            '\"id\": \"刚刚通过接口新增的文章id\"',
     'url': '/interface/tArticle/update',
     'mode': 'post',
     'h': {'Content-Type': 'application/json'},
     'd': {"authorName": "yuzhenxin", "categoryNoStr": "CATEGORY00000183", "content": "自动化接口修改的文章内容", "updatedBy": "demoAdmin",
           "linkUrl": "https://cxjktest.oss-cn-shanghai.aliyuncs.com/article/2020/06/0ffc2c7c-6858-4036-9558-bdfc93ae1f9e.jpg",
           "putWay": "0", "title": "自动化接口修改的文章标题"},
     'code': 'code',
     'expected_code': '200',
     'expected_key': ['code', 'data', 'id', 'articleNo', 'title', 'authorName', 'content', 'putWay', 'linkUrl', 'createdBy'],
     }
]

delete = [
    {
     'interface': '删除文章接口',
     'msg': '\"updatedBy\": \"demoAdmin\",\"id\": \"刚刚通过接口新增的文章id\"',
     'url': '/interface/tArticle/delete',
     'mode': 'post',
     'h': {'Content-Type': 'application/x-www-form-urlencoded'},
     'd': {'updatedBy': 'demoAdmin'},
     'code': 'code',
     'expected_code': '200',
     'expected_key': ['code', 'data', 'id', 'articleNo', 'title', 'authorName', 'content', 'putWay', 'linkUrl', 'createdBy'],
     }
]

onshelf = [
    {
     'interface': '上架文章',
     'msg': '\"updatedBy\": \"demoAdmin\",\"id\": \"刚刚通过接口新增的文章id\",\"putWay\": \"1\"',
     'url': '/interface/tArticle/onshelf',
     'mode': 'post',
     'h': {'Content-Type': 'application/json'},
     'd': {'updatedBy': 'demoAdmin', 'putWay': '1'},
     'code': 'code',
     'expected_code': '200',
     'expected_key': ['code', 'data'],
     }
]

onshelf2 = [
    {
     'interface': '下架文章',
     'msg': '\"updatedBy\": \"demoAdmin\",\"id\": \"刚刚通过接口新增的文章id\",\"putWay\": \"0\"',
     'url': '/interface/tArticle/onshelf',
     'mode': 'post',
     'h': {'Content-Type': 'application/json'},
     'd': {'updatedBy': 'demoAdmin', 'putWay': '1'},
     'code': 'code',
     'expected_code': '200',
     'expected_key': ['code', 'data'],
     }
]

changePutWay = [
    {
     'interface': '一键上架文章',
     'msg': '\"updatedBy\": \"demoAdmin\",\"articleIdStr\": \"刚刚通过接口新增的文章id\",\"putWayType\": \"1\"',
     'url': '/interface/tArticle/changePutWay',
     'mode': 'post',
     'h': {'Content-Type': 'application/json'},
     'd': {'updatedBy': 'demoAdmin', 'putWayType': '1'},
     'code': 'code',
     'expected_code': '200',
     'expected_key': ['code', 'data', 'putWayType', 'articleIdStr', 'articleIdArray', 'putWay', 'updatedBy'],
     }
]

changePutWay2 = [
    {
     'interface': '一键下架文章',
     'msg': '\"updatedBy\": \"demoAdmin\",\"articleIdStr\": \"刚刚通过接口新增的文章id\",\"putWayType\": \"0\"',
     'url': '/interface/tArticle/changePutWay',
     'mode': 'post',
     'h': {'Content-Type': 'application/json'},
     'd': {'updatedBy': 'demoAdmin', 'putWayType': '1'},
     'code': 'code',
     'expected_code': '200',
     'expected_key': ['code', 'data', 'putWayType', 'articleIdStr', 'articleIdArray', 'putWay', 'updatedBy'],
     }
]
