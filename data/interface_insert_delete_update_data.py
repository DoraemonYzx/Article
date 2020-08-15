#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:余振新
@file: interface_home.py
@time: 2020/04/22
"""

categoryInsert = [
    {
     "interface": "https://testserver.cxjk.com/api/cxjk-article/interface/tArticle/categoryInsert",
     "msg": "新增一级分类，新增成功",
     "url": "/interface/tArticle/categoryInsert",
     "mode": "post",
     "h": {"Content-Type": "application/json"},
     "d": {"categoryName": "一级分类", "categoryType": "0", "categoryLevel": "1", "createdBy": "demoAdmin"},
     "code": "code",
     "expected_code": "200",
     "expected_key": ["code", "data", "id", "categoryNo", "categoryName", "categoryType", "categoryLevel", "createdBy"],
     }
]

categoryInsert1 = [
    {
     "interface": "https://testserver.cxjk.com/api/cxjk-article/interface/tArticle/categoryInsert",
     "msg": "新增已存在一级分类，新增失败",
     "url": "/interface/tArticle/categoryInsert",
     "mode": "post",
     "h": {"Content-Type": "application/json"},
     "d": {"categoryName": "肿瘤科", "categoryType": "0", "categoryLevel": "1", "createdBy": "demoAdmin"},
     "code": "code",
     "expected_code": "500",
     "expected_key": ["code", "data", "msg"],
     }
]

categoryInsert2 = [
    {
     "interface": "https://testserver.cxjk.com/api/cxjk-article/interface/tArticle/categoryInsert",
     "msg": "新增二级分类，关联一级分类，新增成功",
     "url": "/interface/tArticle/categoryInsert",
     "mode": "post",
     "h": {"Content-Type": "application/json"},
     "d": {"categoryName": "二级分类", "categoryType": "0", "categoryLevel": "2", "createdBy": "demoAdmin", "parentCategory": "CATEGORY00000004"},
     "code": "code",
     "expected_code": "200",
     "expected_key": ["code", "data", "id", "categoryNo", "categoryName", "categoryType", "categoryLevel", "createdBy"],
     }
]

categoryInsert3 = [
    {
     "interface": "https://testserver.cxjk.com/api/cxjk-article/interface/tArticle/categoryInsert",
     "msg": "新增已存在二级分类，新增失败",
     "url": "/interface/tArticle/categoryInsert",
     "mode": "post",
     "h": {"Content-Type": "application/json"},
     "d": {"categoryName": "乳腺癌", "categoryType": "0", "categoryLevel": "2", "createdBy": "demoAdmin", },
     "code": "code",
     "expected_code": "500",
     "expected_key": ["code", "data", "msg"],
     }
]

categoryUpdate = [
    {
     "interface": "https://testserver.cxjk.com/api/cxjk-article/interface/tArticle/categoryUpdate",
     "msg": "根据正确一级分类id修改分类名字，id关联，成功",
     "url": "/interface/tArticle/categoryUpdate",
     "mode": "post",
     "h": {"Content-Type": "application/json"},
     "d": {"categoryName": "改一级分类", "updatedBy": "demoAdmin"},
     "code": "code",
     "expected_code": "200",
     "expected_key": ["code", "data", "id", "categoryNo", "categoryName", "categoryType", "categoryLevel", "updatedBy"],
     },
    {
     "interface": "https://testserver.cxjk.com/api/cxjk-article/interface/tArticle/categoryUpdate",
     "msg": "根据正确二级分类id修改分类名字，id关联，成功",
     "url": "/interface/tArticle/categoryUpdate",
     "mode": "post",
     "h": {"Content-Type": "application/json"},
     "d": {"categoryName": "改二级分类", "updatedBy": "demoAdmin"},
     "code": "code",
     "expected_code": "200",
     "expected_key": ["code", "data", "id", "categoryNo", "categoryName", "categoryType", "categoryLevel", "updatedBy"],
     }
]

categoryUpdate2 = [
    {
     "interface": "https://testserver.cxjk.com/api/cxjk-article/interface/tArticle/categoryUpdate",
     "msg": "通过不存在id修改分类名字，修改失败",
     "url": "/interface/tArticle/categoryUpdate",
     "mode": "post",
     "h": {"Content-Type": "application/json"},
     "d": {"categoryName": "改二级分类", "updatedBy": "demoAdmin", "id": "99999"},
     "code": "code",
     "expected_code": "500",
     "expected_key": ["code", "data", "id", "categoryNo", "categoryName", "categoryType", "categoryLevel", "updatedBy"],
     }
]

categoryDelete = [
    {
     "interface": "https://testserver.cxjk.com/api/cxjk-article/interface/tArticle/categoryDelete",
     "msg": "删除正确的一级标签，删除成功",
     "url": "/interface/tArticle/categoryDelete",
     "mode": "post",
     "h": {"Content-Type": "application/x-www-form-urlencoded"},
     "d": {"updatedBy": "demoAdmin"},
     "code": "code",
     "expected_code": "200",
     "expected_key": ["code", "data", "id", "categoryNo", "categoryName", "categoryType", "categoryLevel", "createdBy"],
     }
]

categoryDelete2 = [
    {
     "interface": "https://testserver.cxjk.com/api/cxjk-article/interface/tArticle/categoryDelete",
     "msg": "删除正确的二级分类，删除成功",
     "url": "/interface/tArticle/categoryDelete",
     "mode": "post",
     "h": {"Content-Type": "application/x-www-form-urlencoded"},
     "d": {"updatedBy": "demoAdmin"},
     "code": "code",
     "expected_code": "200",
     "expected_key": ["code", "data", "id", "categoryNo", "categoryName", "categoryType", "categoryLevel", "createdBy"],
     }
]

categoryDelete3 = [
    {
     "interface": "https://testserver.cxjk.com/api/cxjk-article/interface/tArticle/categoryDelete",
     "msg": "删除已经删除的标签，系统错误未找到指定对象",
     "url": "/interface/tArticle/categoryDelete",
     "mode": "post",
     "h": {"Content-Type": "application/x-www-form-urlencoded"},
     "d": {"updatedBy": "demoAdmin"},
     "code": "code",
     "expected_code": "500",
     "expected_key": ["code", "data", "id", "categoryNo", "categoryName", "categoryType", "categoryLevel", "createdBy"],
     }
]

categoryDelete4 = [
    {
     "interface": "https://testserver.cxjk.com/api/cxjk-article/interface/tArticle/categoryDelete",
     "msg": "删除不存在的标签，系统错误未找到指定对象",
     "url": "/interface/tArticle/categoryDelete",
     "mode": "post",
     "h": {"Content-Type": "application/x-www-form-urlencoded"},
     "d": {"updatedBy": "demoAdmin", "id": "99999"},
     "code": "code",
     "expected_code": "500",
     "expected_key": ["code", "data", "id", "categoryNo", "categoryName", "categoryType", "categoryLevel", "createdBy"],
     }
]

flagInsert = [
    {
     "interface": "https://testserver.cxjk.com/api/cxjk-article/interface/tArticle/flagInsert",
     "msg": "新增一级标签，新增成功",
     "url": "/interface/tArticle/flagInsert",
     "mode": "post",
     "h": {"Content-Type": "application/json"},
     "d": {"createdBy": "demoAdmin", "flagLevel": "1", "flagName": "自动化接口自动新增一级标签", "flagType": "0"},
     "code": "code",
     "expected_code": "200",
     "expected_key": ["code", "data", "id", "flagNo", "flagName", "flagType", "flagLevel", "createdBy"],
     }
]

flagInsert1 = [
    {
     "interface": "https://testserver.cxjk.com/api/cxjk-article/interface/tArticle/flagInsert",
     "msg": "新增已存在的一级标签，新增失败",
     "url": "/interface/tArticle/flagInsert",
     "mode": "post",
     "h": {"Content-Type": "application/json"},
     "d": {"createdBy": "demoAdmin", "flagLevel": "1", "flagName": "test", "flagType": "0"},
     "code": "code",
     "expected_code": "500",
     "expected_key": ["code", "data", "msg"],
     }
]

flagInsert2 = [
    {
     "interface": "https://testserver.cxjk.com/api/cxjk-article/interface/tArticle/flagInsert",
     "msg": "新增二级标签，关联一级分类标签，新增成功,",
     "url": "/interface/tArticle/flagInsert",
     "mode": "post",
     "h": {"Content-Type": "application/json"},
     "d": {"createdBy": "demoAdmin", "flagLevel": "2", "flagName": "自动化接口自动新增二级标签", "flagType": "0"},
     "code": "code",
     "expected_code": "200",
     "expected_key": ["code", "data", "id", "flagNo", "flagName", "flagType", "flagLevel", "createdBy"],
     }
]

flagInsert3 = [
    {
     "interface": "https://testserver.cxjk.com/api/cxjk-article/interface/tArticle/flagInsert",
     "msg": "增已存在的二级标签，新增失败",
     "url": "/interface/tArticle/flagInsert",
     "mode": "post",
     "h": {"Content-Type": "application/json"},
     "d": {"createdBy": "demoAdmin", "flagLevel": "2", "flagName": "test1", "flagType": "0", "parentFlag": "FLAG00000179"},
     "code": "code",
     "expected_code": "500",
     "expected_key": ["code", "data", "msg"],
     }
]

flagUpdate = [
    {
     "interface": "https://testserver.cxjk.com/api/cxjk-article/interface/tArticle/flagUpdate",
     "msg": "通过正确id修改一级标签名字，修改成功",
     "url": "/interface/tArticle/flagUpdate",
     "mode": "post",
     "h": {"Content-Type": "application/json"},
     "d": {"flagName": "自动化接口修改后的一级标签", "updatedBy": "demoAdmin"},
     "code": "code",
     "expected_code": "200",
     "expected_key": ["code", "data", "id", "flagNo", "flagName", "flagType", "flagLevel", "updatedBy"],
     },
    {
     "interface": "https://testserver.cxjk.com/api/cxjk-article/interface/tArticle/flagUpdate",
     "msg": "通过正确id修改二级标签名字，修改成功",
     "url": "/interface/tArticle/flagUpdate",
     "mode": "post",
     "h": {"Content-Type": "application/json"},
     "d": {"flagName": "自动化接口修改后的二级标签", "updatedBy": "demoAdmin"},
     "code": "code",
     "expected_code": "200",
     "expected_key": ["code", "data", "id", "flagNo", "flagName", "flagType", "flagLevel", "updatedBy"],
     }
]

flagUpdate2 = [
    {
     "interface": "https://testserver.cxjk.com/api/cxjk-article/interface/tArticle/flagUpdate",
     "msg": "通过不存在id修改一级标签名字，修改失败",
     "url": "/interface/tArticle/flagUpdate",
     "mode": "post",
     "h": {"Content-Type": "application/json"},
     "d": {"flagName": "自动化接口修改后的一级标签", "updatedBy": "demoAdmin", "id": "9999"},
     "code": "code",
     "expected_code": "500",
     "expected_key": ["code", "data", "msg"],
     }
]

flagDelete = [
    {
     "interface": "https://testserver.cxjk.com/api/cxjk-article/interface/tArticle/flagDelete",
     "msg": "删除正确的一级标签，删除成功",
     "url": "/interface/tArticle/flagDelete",
     "mode": "post",
     "h": {"Content-Type": "application/x-www-form-urlencoded"},
     "d": {"updatedBy": "demoAdmin"},
     "code": "code",
     "expected_code": "200",
     "expected_key": ["code", "data", "id", "flagNo", "flagName", "flagType", "flagLevel", "updatedBy"],
     }
]

flagDelete2 = [
    {
     "interface": "https://testserver.cxjk.com/api/cxjk-article/interface/tArticle/flagDelete",
     "msg": "删除正确的二级标签，删除成功",
     "url": "/interface/tArticle/flagDelete",
     "mode": "post",
     "h": {"Content-Type": "application/x-www-form-urlencoded"},
     "d": {"updatedBy": "demoAdmin"},
     "code": "code",
     "expected_code": "200",
     "expected_key": ["code", "data", "id", "flagNo", "flagName", "flagType", "flagLevel", "updatedBy"],
     }
]

flagDelete3 = [
    {
     "interface": "https://testserver.cxjk.com/api/cxjk-article/interface/tArticle/flagDelete",
     "msg": "删除已经删除的标签，系统错误未找到指定对象",
     "url": "/interface/tArticle/flagDelete",
     "mode": "post",
     "h": {"Content-Type": "application/x-www-form-urlencoded"},
     "d": {"updatedBy": "demoAdmin"},
     "code": "code",
     "expected_code": "500",
     "expected_key": ["code", "data", "msg"],
     }
]

flagDelete4 = [
    {
     "interface": "https://testserver.cxjk.com/api/cxjk-article/interface/tArticle/flagDelete",
     "msg": "删除不存在的标签，系统错误未找到指定对象",
     "url": "/interface/tArticle/flagDelete",
     "mode": "post",
     "h": {"Content-Type": "application/x-www-form-urlencoded"},
     "d": {"updatedBy": "demoAdmin", "id": "9999"},
     "code": "code",
     "expected_code": "500",
     "expected_key": ["code", "data", "msg"],
     }
]

insert = [
    {
     "interface": "https://testserver.cxjk.com/api/cxjk-article/interface/tArticle/insert",
     "msg": "新增文章，成功",
     "url": "/interface/tArticle/insert",
     "mode": "post",
     "h": {"Content-Type": "application/json"},
     "d": {"authorName": "yuzhenxin", "categoryNoStr": "CATEGORY00000183", "content": "自动化接口新增的文章内容", "createdBy": "demoAdmin",
           "linkUrl": "https://cxjktest.oss-cn-shanghai.aliyuncs.com/article/2020/06/0ffc2c7c-6858-4036-9558-bdfc93ae1f9e.jpg",
           "putWay": "0", "title": "自动化接口新增的文章标题"},
     "code": "code",
     "expected_code": "200",
     "expected_key": ["code", "data", "id", "articleNo", "title", "authorName", "content", "putWay", "linkUrl", "createdBy"],
     }
]

update = [
    {
     "interface": "https://testserver.cxjk.com/api/cxjk-article/interface/tArticle/update",
     "msg": "通过正确的文章id，文章id关联，修改文章标题，内容，成功",
     "url": "/interface/tArticle/update",
     "mode": "post",
     "h": {"Content-Type": "application/json"},
     "d": {"authorName": "yuzhenxin", "categoryNoStr": "CATEGORY00000183", "content": "自动化接口修改的文章内容", "updatedBy": "demoAdmin",
           "linkUrl": "https://cxjktest.oss-cn-shanghai.aliyuncs.com/article/2020/06/0ffc2c7c-6858-4036-9558-bdfc93ae1f9e.jpg",
           "putWay": "0", "title": "自动化接口修改的文章标题"},
     "code": "code",
     "expected_code": "200",
     "expected_key": ["code", "data", "id", "articleNo", "title", "authorName", "content", "putWay", "linkUrl", "createdBy"],
     }
]
update2 = [
    {
     "interface": "https://testserver.cxjk.com/api/cxjk-article/interface/tArticle/update",
     "msg": "文章id为空，修改文章标题，内容，失败",
     "url": "/interface/tArticle/update",
     "mode": "post",
     "h": {"Content-Type": "application/json"},
     "d": {"authorName": "yuzhenxin", "categoryNoStr": "CATEGORY00000183", "content": "自动化接口修改的文章内容", "updatedBy": "demoAdmin",
           "linkUrl": "https://cxjktest.oss-cn-shanghai.aliyuncs.com/article/2020/06/0ffc2c7c-6858-4036-9558-bdfc93ae1f9e.jpg",
           "putWay": "0", "title": "自动化接口修改的文章标题", "id": ""},
     "code": "code",
     "expected_code": "500",
     "expected_key": ["code", "data", "msg"],
     }
]

delete = [
    {
     "interface": "https://testserver.cxjk.com/api/cxjk-article/interface/tArticle/delete",
     "msg": "删除正确的文章，关联文章id，删除成功",
     "url": "/interface/tArticle/delete",
     "mode": "post",
     "h": {"Content-Type": "application/x-www-form-urlencoded"},
     "d": {"updatedBy": "demoAdmin"},
     "code": "code",
     "expected_code": "200",
     "expected_key": ["code", "data", "id", "articleNo", "title", "authorName", "content", "putWay", "linkUrl", "createdBy"],
     }
]
delete2 = [
    {
     "interface": "https://testserver.cxjk.com/api/cxjk-article/interface/tArticle/delete",
     "msg": "删除不存在的文章，删除失败",
     "url": "/interface/tArticle/delete",
     "mode": "post",
     "h": {"Content-Type": "application/x-www-form-urlencoded"},
     "d": {"updatedBy": "demoAdmin", "id": "2262"},
     "code": "code",
     "expected_code": "500",
     "expected_key": ["code", "data", "id", "articleNo", "title", "authorName", "content", "putWay", "linkUrl", "createdBy"],
     }
]
delete3 = [
    {
     "interface": "https://testserver.cxjk.com/api/cxjk-article/interface/tArticle/delete",
     "msg": "删除已删除的文章，关联文章id，删除成功",
     "url": "/interface/tArticle/delete",
     "mode": "post",
     "h": {"Content-Type": "application/x-www-form-urlencoded"},
     "d": {"updatedBy": "demoAdmin"},
     "code": "code",
     "expected_code": "500",
     "expected_key": ["code", "data", "id", "articleNo", "title", "authorName", "content", "putWay", "linkUrl", "createdBy"],
     }
]

onshelf = [
    {
     "interface": "https://testserver.cxjk.com/api/cxjk-article/interface/tArticle/onshelf",
     "msg": "上架文章，关联文章id，成功",
     "url": "/interface/tArticle/onshelf",
     "mode": "post",
     "h": {"Content-Type": "application/json"},
     "d": {"updatedBy": "demoAdmin", "putWay": "1"},
     "code": "code",
     "expected_code": "200",
     "expected_key": ["code", "data"],
     }
]

onshelf2 = [
    {
     "interface": "https://testserver.cxjk.com/api/cxjk-article/interface/tArticle/onshelf",
     "msg": "下架文章，关联文章id，成功",
     "url": "/interface/tArticle/onshelf",
     "mode": "post",
     "h": {"Content-Type": "application/json"},
     "d": {"updatedBy": "demoAdmin", "putWay": "0"},
     "code": "code",
     "expected_code": "200",
     "expected_key": ["code", "data"],
     }
]

changePutWay = [
    {
     "interface": "https://testserver.cxjk.com/api/cxjk-article/interface/tArticle/changePutWay",
     "msg": "一键上架文章，关联文章id，一键上架成功",
     "url": "/interface/tArticle/changePutWay",
     "mode": "post",
     "h": {"Content-Type": "application/json"},
     "d": {"updatedBy": "demoAdmin", "putWayType": "1"},
     "code": "code",
     "expected_code": "200",
     "expected_key": ["code", "data", "putWayType", "articleIdStr", "articleIdArray", "putWay", "updatedBy"],
     }
]

changePutWay2 = [
    {
     "interface": "https://testserver.cxjk.com/api/cxjk-article/interface/tArticle/changePutWay",
     "msg": "一键下架文章，关联文章id，一键下架成功",
     "url": "/interface/tArticle/changePutWay",
     "mode": "post",
     "h": {"Content-Type": "application/json"},
     "d": {"updatedBy": "demoAdmin", "putWayType": "1"},
     "code": "code",
     "expected_code": "200",
     "expected_key": ["code", "data", "putWayType", "articleIdStr", "articleIdArray", "putWay", "updatedBy"],
     }
]

addCount = [
    {
     "interface": "https://testserver.cxjk.com/api/cxjk-article/interface/tArticle/addCount",
     "msg": "传入文章编号，新增阅读量成功",
     "url": "/interface/tArticle/addCount",
     "mode": "post",
     "h": {"Content-Type": "application/json"},
     "d": {},
     "code": "code",
     "expected_code": "200",
     "expected_key": ["code", "data", "msg"],
     }
]
