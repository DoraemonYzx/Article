#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:余振新
@file: interface_home.py
@time: 2020/04/22
"""

categorySelect = [
    {
     "interface": "https://testserver.cxjk.com/api/cxjk-article/interface/tArticle/categorySelect",
     "msg": "查询正确的id，查询成功",
     "url": "/interface/tArticle/categorySelect",
     "mode": "post",
     "h": {"Content-Type": "application/json"},
     "d": {"id": "36"},
     "code": "code",
     "expected_code": "200",
     "expected_key": ["code", "data", "id", "categoryNo", "categoryName", "parentCategory", "categoryType", "categoryLevel", "deleteFlag",
                      "createdBy", "createdDate", "updatedBy", "updatedDate"],
     },
    {
     "interface": "https://testserver.cxjk.com/api/cxjk-article/interface/tArticle/categorySelect",
     "msg": "查询一级分类，查询成功",
     "url": "/interface/tArticle/categorySelect",
     "mode": "post",
     "h": {"Content-Type": "application/json"},
     "d": {"categoryLevel": "1"},
     "code": "code",
     "expected_code": "200",
     "expected_key": ["code", "data", "id", "categoryNo", "categoryName", "parentCategory", "categoryType", "categoryLevel", "deleteFlag",
                      "createdBy", "createdDate", "updatedBy", "updatedDate"],
     },
    {
     "interface": "https://testserver.cxjk.com/api/cxjk-article/interface/tArticle/categorySelect",
     "msg": "查询二级分类，查询成功",
     "url": "/interface/tArticle/categorySelect",
     "mode": "post",
     "h": {"Content-Type": "application/json"},
     "d": {"categoryLevel": "2"},
     "code": "code",
     "expected_code": "200",
     "expected_key": ["code", "data", "id", "categoryNo", "categoryName", "parentCategory", "categoryType", "categoryLevel", "deleteFlag",
                      "createdBy", "createdDate", "updatedBy", "updatedDate"],
     },
    {
     "interface": "https://testserver.cxjk.com/api/cxjk-article/interface/tArticle/categorySelect",
     "msg": "查询名字为test的分类，查询成功",
     "url": "/interface/tArticle/categorySelect",
     "mode": "post",
     "h": {"Content-Type": "application/json"},
     "d": {"categoryName": "肿瘤科"},
     "code": "code",
     "expected_code": "200",
     "expected_key": ["code", "data", "id", "categoryNo", "categoryName", "parentCategory", "categoryType", "categoryLevel", "deleteFlag",
                      "createdBy", "createdDate", "updatedBy", "updatedDate"],
     },
    {
     "interface": "https://testserver.cxjk.com/api/cxjk-article/interface/tArticle/categorySelect",
     "msg": "查询no为FLAG00000179的分类，查询成功",
     "url": "/interface/tArticle/categorySelect",
     "mode": "post",
     "h": {"Content-Type": "application/json"},
     "d": {"categoryNo": "CATEGORY00000004"},
     "code": "code",
     "expected_code": "200",
     "expected_key": ["code", "data", "id", "categoryNo", "categoryName", "parentCategory", "categoryType", "categoryLevel", "deleteFlag",
                      "createdBy", "createdDate", "updatedBy", "updatedDate"],
     }

]

flagSelect = [
    {
     "interface": "https://testserver.cxjk.com/api/cxjk-article/interface/tArticle/flagSelect",
     "msg": "查询正确的id，查询成功",
     "url": "/interface/tArticle/flagSelect",
     "mode": "post",
     "h": {"Content-Type": "application/json"},
     "d": {"id": "182"},
     "code": "code",
     "expected_code": "200",
     "expected_key": ["code", "data", "id", "flagNo", "flagName", "parentFlag", "flagType", "flagLevel", "deleteFlag",
                      "createdBy", "createdDate", "updatedBy", "updatedDate"],
     },
    {
     "interface": "https://testserver.cxjk.com/api/cxjk-article/interface/tArticle/flagSelect",
     "msg": "查询一级标签，查询成功",
     "url": "/interface/tArticle/flagSelect",
     "mode": "post",
     "h": {"Content-Type": "application/json"},
     "d": {"flagLevel": "1", "flagType": "0"},
     "code": "code",
     "expected_code": "200",
     "expected_key": ["code", "data", "id", "flagNo", "flagName", "parentFlag", "flagType", "flagLevel", "deleteFlag",
                      "createdBy", "createdDate", "updatedBy", "updatedDate"],
     },
    {
     "interface": "https://testserver.cxjk.com/api/cxjk-article/interface/tArticle/flagSelect",
     "msg": "查询二级标签，查询成功",
     "url": "/interface/tArticle/flagSelect",
     "mode": "post",
     "h": {"Content-Type": "application/json"},
     "d": {"flagLevel": "2", "flagType": "0"},
     "code": "code",
     "expected_code": "200",
     "expected_key": ["code", "data", "id", "flagNo", "flagName", "parentFlag", "flagType", "flagLevel", "deleteFlag",
                      "createdBy", "createdDate", "updatedBy", "updatedDate"],
     },
    {
     "interface": "https://testserver.cxjk.com/api/cxjk-article/interface/tArticle/flagSelect",
     "msg": "查询名字为test的标签，查询成功",
     "url": "/interface/tArticle/flagSelect",
     "mode": "post",
     "h": {"Content-Type": "application/json"},
     "d": {"flagName": "test", "flagType": "0"},
     "code": "code",
     "expected_code": "200",
     "expected_key": ["code", "data", "id", "flagNo", "flagName", "parentFlag", "flagType", "flagLevel", "deleteFlag",
                      "createdBy", "createdDate", "updatedBy", "updatedDate"],
     },
    {
     "interface": "https://testserver.cxjk.com/api/cxjk-article/interface/tArticle/flagSelect",
     "msg": "查询no为FLAG00000179的标签，查询成功",
     "url": "/interface/tArticle/flagSelect",
     "mode": "post",
     "h": {"Content-Type": "application/json"},
     "d": {"flagNo": "FLAG00000179"},
     "code": "code",
     "expected_code": "200",
     "expected_key": ["code", "data", "id", "flagNo", "flagName", "parentFlag", "flagType", "flagLevel", "deleteFlag",
                      "createdBy", "createdDate", "updatedBy", "updatedDate"],
     },
]

query = [
    {
     "interface": "https://testserver.cxjk.com/api/cxjk-article/interface/tArticle/query",
     "msg": "不带参数查询文章，成功",
     "url": "/interface/tArticle/query",
     "mode": "post",
     "h": {"Content-Type": "application/json"},
     "d": {"currentPage": "1", "pageSize": "1"},
     "code": "code",
     "expected_code": "200",
     "expected_key": ["code", "data", "total", "list", "msg"]
     },
    {
     "interface": "https://testserver.cxjk.com/api/cxjk-article/interface/tArticle/query",
     "msg": "通过文章No查询文章，成功",
     "url": "/interface/tArticle/query",
     "mode": "post",
     "h": {"Content-Type": "application/json"},
     "d": {"currentPage": "1", "pageSize": "1", "articleNo": "ARTICLE00001906"},
     "code": "code",
     "expected_code": "200",
     "expected_key": ["code", "data", "total", "list", "msg"]
     },
    {
     "interface": "https://testserver.cxjk.com/api/cxjk-article/interface/tArticle/query",
     "msg": "通过文章name查询文章，成功",
     "url": "/interface/tArticle/query",
     "mode": "post",
     "h": {"Content-Type": "application/json"},
     "d": {"currentPage": "1", "pageSize": "1", "authorName": "阅读量统计"},
     "code": "code",
     "expected_code": "200",
     "expected_key": ["code", "data", "total", "list", "msg"]
     },
    {
     "interface": "https://testserver.cxjk.com/api/cxjk-article/interface/tArticle/query",
     "msg": "通过分类No查询文章，成功",
     "url": "/interface/tArticle/query",
     "mode": "post",
     "h": {"Content-Type": "application/json"},
     "d": {"currentPage": "1", "pageSize": "1", "categoryNo": "CATEGORY00000241"},
     "code": "code",
     "expected_code": "200",
     "expected_key": ["code", "data", "total", "list", "msg"]
     },
    {
     "interface": "https://testserver.cxjk.com/api/cxjk-article/interface/tArticle/query",
     "msg": "通过标签No查询文章，成功",
     "url": "/interface/tArticle/query",
     "mode": "post",
     "h": {"Content-Type": "application/json"},
     "d": {"currentPage": "1", "pageSize": "1", "flagNo": "FLAG00000007"},
     "code": "code",
     "expected_code": "200",
     "expected_key": ["code", "data", "total", "list", "msg"]
     },
    {
     "interface": "https://testserver.cxjk.com/api/cxjk-article/interface/tArticle/query",
     "msg": "通过文章id查询文章，成功",
     "url": "/interface/tArticle/query",
     "mode": "post",
     "h": {"Content-Type": "application/json"},
     "d": {"currentPage": "1", "pageSize": "1", "id": "2246"},
     "code": "code",
     "expected_code": "200",
     "expected_key": ["code", "data", "total", "list", "msg"]
     }
]

queryArtcleCategoryFlagByNo = [
    {
     "interface": "https://testserver.cxjk.com/api/cxjk-article/interface/tArticle/queryArtcleCategoryFlagByNo",
     "msg": "根据文章No查询文章分类标签，成功",
     "url": "/interface/tArticle/queryArtcleCategoryFlagByNo",
     "mode": "post",
     "h": {"Content-Type": "application/json"},
     "d": {"articleNos": ["ARTICLE00001903"]},
     "code": "code",
     "expected_code": "200",
     "expected_key": ["code", "data", "articleNo", "categoryList", "flagList"],
     }
]

queryArticleListByArticleNos = [
    {
     "interface": "https://testserver.cxjk.com/api/cxjk-article/interface/tArticle/queryArticleListByArticleNos",
     "msg": "根据文章No查询文章名称，成功",
     "url": "/interface/tArticle/queryArticleListByArticleNos",
     "mode": "post",
     "h": {"Content-Type": "application/x-www-form-urlencoded"},
     "d": {"articleNos": ["ARTICLE00001903"]},
     "code": "code",
     "expected_code": "200",
     "expected_key": ["code", "data", "msg", "title"]
     }
]

queryCategoryCount = [
    {
     "interface": "https://testserver.cxjk.com/api/cxjk-article/interface/tArticle/queryCategoryCount",
     "msg": "根据分类No查询分类中文章数量，成功",
     "url": "/interface/tArticle/queryCategoryCount",
     "mode": "post",
     "h": {"Content-Type": "application/json"},
     "d": {"categoryNoList": ["CATEGORY00000004"]},
     "code": "code",
     "expected_code": "200",
     "expected_key": ["code", "data", "msg"]
     }
]

queryHotArticleList = [
    {
     "interface": "https://testserver.cxjk.com/api/cxjk-article/interface/tArticle/queryHotArticleList",
     "msg": "查询(上架时间)一个月内的文章/ 阅读量前15 / 绑定医生的所有文章，成功",
     "url": "/interface/tArticle/queryHotArticleList",
     "mode": "post",
     "h": {"Content-Type": "application/json"},
     "d": {"articleNos": "ARTICLE00001903"},
     "code": "code",
     "expected_code": "200",
     "expected_key": ["code", "data", "msg"]
     }
]

queryByPlatformNo = [
    {
     "interface": "https://testserver.cxjk.com/api/cxjk-article/interface/tArticle/queryByPlatformNo",
     "msg": "\"articleNo\": \"ARTICLE00002713\"",
     "url": "/interface/tArticle/queryByPlatformNo",
     "mode": "post",
     "h": {"Content-Type": "application/json"},
     "d": {"articleNo": "ARTICLE00002713"},
     "code": "code",
     "expected_code": "200",
     "expected_key": ["code", "data", "articleNo", "categoryList", "categoryNo", "categoryName"],
     }
]  # 这个接口没有用到，没写用例

# queryCategoryAll = [
#     {
#      "interface": "查询分类列表接口",
#      "msg": "\"currentPage\": \"1\",\"pageSize\": \"1\"",
#      "url": "/interface/tArticle/queryCategoryAll",
#      "mode": "post",
#      "h": {"Content-Type": "application/json"},
#      "d": {"currentPage": "1", "pageSize": "1"},
#      "code": "code",
#      "expected_code": "200",
#      "expected_key": ["code", "data", "list", "categoryName", "id", "categoryNo"],
#      }
# ]

queryCategoryAll = [
    {
     "interface": "https://testserver.cxjk.com/api/cxjk-article/interface/tArticle/queryCategoryAll",
     "msg": "查询正确的id，查询成功",
     "url": "/interface/tArticle/queryCategoryAll",
     "mode": "post",
     "h": {"Content-Type": "application/json"},
     "d": {"id": "182", "currentPage": 1, "pageSize": 1},
     "code": "code",
     "expected_code": "200",
     "expected_key": ["code", "data", "id", "categoryNo", "categoryName", "parentCategory", "categoryType", "categoryLevel", "deleteFlag",
                      "createdBy", "createdDate", "updatedBy", "updatedDate"],
     },
    {
     "interface": "https://testserver.cxjk.com/api/cxjk-article/interface/tArticle/queryCategoryAll",
     "msg": "查询一级标签，查询成功",
     "url": "/interface/tArticle/queryCategoryAll",
     "mode": "post",
     "h": {"Content-Type": "application/json"},
     "d": {"categoryLevel": "1",  "currentPage": 1, "pageSize": 1},
     "code": "code",
     "expected_code": "200",
     "expected_key": ["code", "data", "id", "categoryNo", "categoryName", "parentCategory", "categoryType", "categoryLevel", "deleteFlag",
                      "createdBy", "createdDate", "updatedBy", "updatedDate"],
     },
    {
     "interface": "https://testserver.cxjk.com/api/cxjk-article/interface/tArticle/queryCategoryAll",
     "msg": "查询二级标签，查询成功",
     "url": "/interface/tArticle/queryCategoryAll",
     "mode": "post",
     "h": {"Content-Type": "application/json"},
     "d": {"categoryLevel": "2",  "currentPage": 1, "pageSize": 1},
     "code": "code",
     "expected_code": "200",
     "expected_key": ["code", "data", "id", "categoryNo", "categoryName", "parentCategory", "categoryType", "categoryLevel", "deleteFlag",
                      "createdBy", "createdDate", "updatedBy", "updatedDate"],
     },
    {
     "interface": "https://testserver.cxjk.com/api/cxjk-article/interface/tArticle/queryCategoryAll",
     "msg": "查询名字为test的标签，查询成功",
     "url": "/interface/tArticle/queryCategoryAll",
     "mode": "post",
     "h": {"Content-Type": "application/json"},
     "d": {"categoryName": "肿瘤科",  "currentPage": 1, "pageSize": 1},
     "code": "code",
     "expected_code": "200",
     "expected_key": ["code", "data", "id", "categoryNo", "categoryName", "parentCategory", "categoryType", "categoryLevel", "deleteFlag",
                      "createdBy", "createdDate", "updatedBy", "updatedDate"],
     },
    {
     "interface": "https://testserver.cxjk.com/api/cxjk-article/interface/tArticle/queryCategoryAll",
     "msg": "查询no为FLAG00000179的标签，查询成功",
     "url": "/interface/tArticle/queryCategoryAll",
     "mode": "post",
     "h": {"Content-Type": "application/json"},
     "d": {"categoryNo": "CATEGORY00000004", "currentPage": 1, "pageSize": 1},
     "code": "code",
     "expected_code": "200",
     "expected_key": ["code", "data", "id", "categoryNo", "categoryName", "parentCategory", "categoryType", "categoryLevel", "deleteFlag",
                      "createdBy", "createdDate", "updatedBy", "updatedDate"],
     },
]

# queryFlagAll = [
#     {
#      "interface": "查询标签列表接口",
#      "msg": "\"currentPage\": \"1\",\"pageSize\": \"1\"",
#      "url": "/interface/tArticle/queryFlagAll",
#      "mode": "post",
#      "h": {"Content-Type": "application/json"},
#      "d": {"currentPage": "1", "pageSize": "1"},
#      "code": "code",
#      "expected_code": "200",
#      "expected_key": ["code", "data", "list", "flagNo", "secondFlagNo", "id"],
#      }
# ]
queryFlagAll = [
    {
     "interface": "https://testserver.cxjk.com/api/cxjk-article/interface/tArticle/queryFlagAll",
     "msg": "查询正确的id，查询成功",
     "url": "/interface/tArticle/queryFlagAll",
     "mode": "post",
     "h": {"Content-Type": "application/json"},
     "d": {"id": "182", "currentPage": 1, "pageSize": 1},
     "code": "code",
     "expected_code": "200",
     "expected_key": ["code", "data", "id", "flagNo", "flagName", "parentFlag", "flagType", "flagLevel", "deleteFlag",
                      "createdBy", "createdDate", "updatedBy", "updatedDate"],
     },
    {
     "interface": "https://testserver.cxjk.com/api/cxjk-article/interface/tArticle/queryFlagAll",
     "msg": "查询一级标签，查询成功",
     "url": "/interface/tArticle/queryFlagAll",
     "mode": "post",
     "h": {"Content-Type": "application/json"},
     "d": {"flagLevel": "1", "flagType": "0", "currentPage": 1, "pageSize": 1},
     "code": "code",
     "expected_code": "200",
     "expected_key": ["code", "data", "id", "flagNo", "flagName", "parentFlag", "flagType", "flagLevel", "deleteFlag",
                      "createdBy", "createdDate", "updatedBy", "updatedDate"],
     },
    {
     "interface": "https://testserver.cxjk.com/api/cxjk-article/interface/tArticle/queryFlagAll",
     "msg": "查询二级标签，查询成功",
     "url": "/interface/tArticle/queryFlagAll",
     "mode": "post",
     "h": {"Content-Type": "application/json"},
     "d": {"flagLevel": "2", "flagType": "0", "currentPage": 1, "pageSize": 1},
     "code": "code",
     "expected_code": "200",
     "expected_key": ["code", "data", "id", "flagNo", "flagName", "parentFlag", "flagType", "flagLevel", "deleteFlag",
                      "createdBy", "createdDate", "updatedBy", "updatedDate"],
     },
    {
     "interface": "https://testserver.cxjk.com/api/cxjk-article/interface/tArticle/queryFlagAll",
     "msg": "查询名字为test的标签，查询成功",
     "url": "/interface/tArticle/queryFlagAll",
     "mode": "post",
     "h": {"Content-Type": "application/json"},
     "d": {"flagName": "test", "flagType": "0", "currentPage": 1, "pageSize": 1},
     "code": "code",
     "expected_code": "200",
     "expected_key": ["code", "data", "id", "flagNo", "flagName", "parentFlag", "flagType", "flagLevel", "deleteFlag",
                      "createdBy", "createdDate", "updatedBy", "updatedDate"],
     },
    {
     "interface": "https://testserver.cxjk.com/api/cxjk-article/interface/tArticle/queryFlagAll",
     "msg": "查询no为FLAG00000179的标签，查询成功",
     "url": "/interface/tArticle/queryFlagAll",
     "mode": "post",
     "h": {"Content-Type": "application/json"},
     "d": {"flagNo": "FLAG00000179", "currentPage": 1, "pageSize": 1},
     "code": "code",
     "expected_code": "200",
     "expected_key": ["code", "data", "id", "flagNo", "flagName", "parentFlag", "flagType", "flagLevel", "deleteFlag",
                      "createdBy", "createdDate", "updatedBy", "updatedDate"],
     },
]

# select = [
#     {
#      "interface": "https://testserver.cxjk.com/api/cxjk-article/interface/tArticle/select",
#      "msg": "\"currentPage\": \"1\",\"pageSize\": \"1\"",
#      "url": "/interface/tArticle/select",
#      "mode": "post",
#      "h": {"Content-Type": "application/json"},
#      "d": {"currentPage": "1", "pageSize": "1"},
#      "code": "code",
#      "expected_code": "200",
#      "expected_key": ["code", "data", "list", "title", "putWay", "id"],
#      }
# ]


select = [
    {
     "interface": "https://testserver.cxjk.com/api/cxjk-article/interface/tArticle/select",
     "msg": "不带参数查询文章，成功",
     "url": "/interface/tArticle/select",
     "mode": "post",
     "h": {"Content-Type": "application/json"},
     "d": {"currentPage": "1", "pageSize": "1"},
     "code": "code",
     "expected_code": "200",
     "expected_key": ["code", "data", "total", "list", "msg"]
     },
    {
     "interface": "https://testserver.cxjk.com/api/cxjk-article/interface/tArticle/select",
     "msg": "通过文章No查询文章，成功",
     "url": "/interface/tArticle/select",
     "mode": "post",
     "h": {"Content-Type": "application/json"},
     "d": {"currentPage": "1", "pageSize": "1", "articleNo": "ARTICLE00001906"},
     "code": "code",
     "expected_code": "200",
     "expected_key": ["code", "data", "total", "list", "msg"]
     },
    {
     "interface": "https://testserver.cxjk.com/api/cxjk-article/interface/tArticle/select",
     "msg": "通过文章name查询文章，成功",
     "url": "/interface/tArticle/select",
     "mode": "post",
     "h": {"Content-Type": "application/json"},
     "d": {"currentPage": "1", "pageSize": "1", "authorName": "阅读量统计"},
     "code": "code",
     "expected_code": "200",
     "expected_key": ["code", "data", "total", "list", "msg"]
     },
    {
     "interface": "https://testserver.cxjk.com/api/cxjk-article/interface/tArticle/select",
     "msg": "通过分类No查询文章，成功",
     "url": "/interface/tArticle/select",
     "mode": "post",
     "h": {"Content-Type": "application/json"},
     "d": {"currentPage": "1", "pageSize": "1", "categoryNo": "CATEGORY00000241"},
     "code": "code",
     "expected_code": "200",
     "expected_key": ["code", "data", "total", "list", "msg"]
     },
    {
     "interface": "https://testserver.cxjk.com/api/cxjk-article/interface/tArticle/select",
     "msg": "通过标签No查询文章，成功",
     "url": "/interface/tArticle/select",
     "mode": "post",
     "h": {"Content-Type": "application/json"},
     "d": {"currentPage": "1", "pageSize": "1", "flagNo": "FLAG00000007"},
     "code": "code",
     "expected_code": "200",
     "expected_key": ["code", "data", "total", "list", "msg"]
     },
    {
     "interface": "https://testserver.cxjk.com/api/cxjk-article/interface/tArticle/select",
     "msg": "通过文章id查询文章，成功",
     "url": "/interface/tArticle/select",
     "mode": "post",
     "h": {"Content-Type": "application/json"},
     "d": {"currentPage": "1", "pageSize": "1", "id": "2246"},
     "code": "code",
     "expected_code": "200",
     "expected_key": ["code", "data", "total", "list", "msg"]
     }
]

# select2 = [
#     {
#      "interface": "查询文章列表接口",
#      "msg": "\"currentPage\": \"1\",\"pageSize\": \"1\"",
#      "url": "/interface/tArticle/select2",
#      "mode": "post",
#      "h": {"Content-Type": "application/json"},
#      "d": {"currentPage": "1", "pageSize": "1"},
#      "code": "code",
#      "expected_code": "200",
#      "expected_key": ["code", "data", "list", "title", "putWay", "id"],
#      }
# ]
#
# select3 = [
#     {
#      "interface": "查询文章列表接口",
#      "msg": "\"currentPage\": \"1\",\"pageSize\": \"1\"",
#      "url": "/interface/tArticle/select3",
#      "mode": "post",
#      "h": {"Content-Type": "application/json"},
#      "d": {"currentPage": "1", "pageSize": "1"},
#      "code": "code",
#      "expected_code": "200",
#      "expected_key": ["code", "data", "list", "title", "putWay", "id"],
#      }
# ]  # 已经不用了

# selectAll = [
#     {
#      "interface": "查询文章列表接口",
#      "msg": "\"currentPage\": \"1\",\"pageSize\": \"1\"",
#      "url": "/interface/tArticle/selectAll",
#      "mode": "post",
#      "h": {"Content-Type": "application/json"},
#      "d": {"currentPage": "1", "pageSize": "1"},
#      "code": "code",
#      "expected_code": "200",
#      "expected_key": ["code", "data", "list", "title", "putWay", "id"],
#      }
# ]

selectAll = [
    {
     "interface": "https://testserver.cxjk.com/api/cxjk-article/interface/tArticle/selectAll",
     "msg": "不带参数查询文章，成功",
     "url": "/interface/tArticle/select",
     "mode": "post",
     "h": {"Content-Type": "application/json"},
     "d": {"currentPage": "1", "pageSize": "1"},
     "code": "code",
     "expected_code": "200",
     "expected_key": ["code", "data", "total", "list", "msg"]
     },
    {
     "interface": "https://testserver.cxjk.com/api/cxjk-article/interface/tArticle/selectAll",
     "msg": "通过文章No查询文章，成功",
     "url": "/interface/tArticle/selectAll",
     "mode": "post",
     "h": {"Content-Type": "application/json"},
     "d": {"currentPage": "1", "pageSize": "1", "articleNo": "ARTICLE00001906"},
     "code": "code",
     "expected_code": "200",
     "expected_key": ["code", "data", "total", "list", "msg"]
     },
    {
     "interface": "https://testserver.cxjk.com/api/cxjk-article/interface/tArticle/selectAll",
     "msg": "通过文章name查询文章，成功",
     "url": "/interface/tArticle/selectAll",
     "mode": "post",
     "h": {"Content-Type": "application/json"},
     "d": {"currentPage": "1", "pageSize": "1", "authorName": "阅读量统计"},
     "code": "code",
     "expected_code": "200",
     "expected_key": ["code", "data", "total", "list", "msg"]
     },
    {
     "interface": "https://testserver.cxjk.com/api/cxjk-article/interface/tArticle/selectAll",
     "msg": "通过分类No查询文章，成功",
     "url": "/interface/tArticle/selectAll",
     "mode": "post",
     "h": {"Content-Type": "application/json"},
     "d": {"currentPage": "1", "pageSize": "1", "categoryNo": "CATEGORY00000241"},
     "code": "code",
     "expected_code": "200",
     "expected_key": ["code", "data", "total", "list", "msg"]
     },
    {
     "interface": "https://testserver.cxjk.com/api/cxjk-article/interface/tArticle/selectAll",
     "msg": "通过标签No查询文章，成功",
     "url": "/interface/tArticle/selectAll",
     "mode": "post",
     "h": {"Content-Type": "application/json"},
     "d": {"currentPage": "1", "pageSize": "1", "flagNo": "FLAG00000007"},
     "code": "code",
     "expected_code": "200",
     "expected_key": ["code", "data", "total", "list", "msg"]
     },
    {
     "interface": "https://testserver.cxjk.com/api/cxjk-article/interface/tArticle/selectAll",
     "msg": "通过文章id查询文章，成功",
     "url": "/interface/tArticle/selectAll",
     "mode": "post",
     "h": {"Content-Type": "application/json"},
     "d": {"currentPage": "1", "pageSize": "1", "id": "2246"},
     "code": "code",
     "expected_code": "200",
     "expected_key": ["code", "data", "total", "list", "msg"]
     }
]

selectByArticleNo = [
    {
     "interface": "https://testserver.cxjk.com/api/cxjk-article/interface/tArticle/selectByArticleNo",
     "msg": "根据正确文章No查询文章，成功",
     "url": "/interface/tArticle/selectByArticleNo",
     "mode": "post",
     "h": {"Content-Type": "application/json"},
     "d": {"articleNo": "ARTICLE00001903"},
     "code": "code",
     "expected_code": "200",
     "expected_key": ["code", "data", "title", "articleNo", "authorName", "id"],
     },
    {
     "interface": "https://testserver.cxjk.com/api/cxjk-article/interface/tArticle/selectByArticleNo",
     "msg": "文章No为空，查询文章，失败",
     "url": "/interface/tArticle/selectByArticleNo",
     "mode": "post",
     "h": {"Content-Type": "application/json"},
     "d": {"articleNo": ""},
     "code": "code",
     "expected_code": "500",
     "expected_key": ["code", "data", "msg"],
     }
]

selectById = [
    {
     "interface": "https://testserver.cxjk.com/api/cxjk-article/interface/tArticle/selectById",
     "msg": "根据正确的文章id查询文章，成功",
     "url": "/interface/tArticle/selectById",
     "mode": "post",
     "h": {"Content-Type": "application/json"},
     "d": {"id": "1468"},
     "code": "code",
     "expected_code": "200",
     "expected_key": ["code", "data", "title", "articleNo", "authorName", "id"],
     },
    {
     "interface": "https://testserver.cxjk.com/api/cxjk-article/interface/tArticle/selectById",
     "msg": "文章id为空，查询文章，失败",
     "url": "/interface/tArticle/selectById",
     "mode": "post",
     "h": {"Content-Type": "application/json"},
     "d": {"id": ""},
     "code": "code",
     "expected_code": "500",
     "expected_key": ["code", "data", "msg"],
     }
]

# selectCategoryAll = [
#     {
#      "interface": "中心查询分类列表接口",
#      "msg": "\"currentPage\": \"1\",\"pageSize\": \"1\"",
#      "url": "/interface/tArticle/selectCategoryAll",
#      "mode": "post",
#      "h": {"Content-Type": "application/json"},
#      "d": {"currentPage": "1", "pageSize": "1"},
#      "code": "code",
#      "expected_code": "200",
#      "expected_key": ["code", "data", "list", "categoryLevel", "categoryNo", "id"],
#      }
# ]

selectCategoryAll = [
    {
     "interface": "https://testserver.cxjk.com/api/cxjk-article/interface/tArticle/selectCategoryAll",
     "msg": "查询正确的id，查询成功",
     "url": "/interface/tArticle/selectCategoryAll",
     "mode": "post",
     "h": {"Content-Type": "application/json"},
     "d": {"id": "182", "currentPage": 1, "pageSize": 1},
     "code": "code",
     "expected_code": "200",
     "expected_key": ["code", "data", "id", "categoryNo", "categoryName", "parentCategory", "categoryType", "categoryLevel", "deleteFlag",
                      "createdBy", "createdDate", "updatedBy", "updatedDate"],
     },
    {
     "interface": "https://testserver.cxjk.com/api/cxjk-article/interface/tArticle/selectCategoryAll",
     "msg": "查询一级标签，查询成功",
     "url": "/interface/tArticle/selectCategoryAll",
     "mode": "post",
     "h": {"Content-Type": "application/json"},
     "d": {"categoryLevel": "1",  "currentPage": 1, "pageSize": 1},
     "code": "code",
     "expected_code": "200",
     "expected_key": ["code", "data", "id", "categoryNo", "categoryName", "parentCategory", "categoryType", "categoryLevel", "deleteFlag",
                      "createdBy", "createdDate", "updatedBy", "updatedDate"],
     },
    {
     "interface": "https://testserver.cxjk.com/api/cxjk-article/interface/tArticle/selectCategoryAll",
     "msg": "查询二级标签，查询成功",
     "url": "/interface/tArticle/selectCategoryAll",
     "mode": "post",
     "h": {"Content-Type": "application/json"},
     "d": {"categoryLevel": "2",  "currentPage": 1, "pageSize": 1},
     "code": "code",
     "expected_code": "200",
     "expected_key": ["code", "data", "id", "categoryNo", "categoryName", "parentCategory", "categoryType", "categoryLevel", "deleteFlag",
                      "createdBy", "createdDate", "updatedBy", "updatedDate"],
     },
    {
     "interface": "https://testserver.cxjk.com/api/cxjk-article/interface/tArticle/selectCategoryAll",
     "msg": "查询名字为test的标签，查询成功",
     "url": "/interface/tArticle/selectCategoryAll",
     "mode": "post",
     "h": {"Content-Type": "application/json"},
     "d": {"categoryName": "肿瘤科",  "currentPage": 1, "pageSize": 1},
     "code": "code",
     "expected_code": "200",
     "expected_key": ["code", "data", "id", "categoryNo", "categoryName", "parentCategory", "categoryType", "categoryLevel", "deleteFlag",
                      "createdBy", "createdDate", "updatedBy", "updatedDate"],
     },
    {
     "interface": "https://testserver.cxjk.com/api/cxjk-article/interface/tArticle/selectCategoryAll",
     "msg": "查询no为FLAG00000179的标签，查询成功",
     "url": "/interface/tArticle/selectCategoryAll",
     "mode": "post",
     "h": {"Content-Type": "application/json"},
     "d": {"categoryNo": "CATEGORY00000004", "currentPage": 1, "pageSize": 1},
     "code": "code",
     "expected_code": "200",
     "expected_key": ["code", "data", "id", "categoryNo", "categoryName", "parentCategory", "categoryType", "categoryLevel", "deleteFlag",
                      "createdBy", "createdDate", "updatedBy", "updatedDate"],
     },
]

# selectCategoryAllChild = [
#     {
#      "interface": "中心查询分类列表接口",
#      "msg": "没有入参",
#      "url": "/interface/tArticle/selectCategoryAllChild",
#      "mode": "post",
#      "h": {"Content-Type": "application/json"},
#      "d": {},
#      "code": "code",
#      "expected_code": "200",
#      "expected_key": ["code", "data", "categoryName", "categoryLevel", "categoryNo", "id", "children"],
#      }
# ]

# selectFlagAll = [
#     {
#      "interface": "中心查询标签列表接口",
#      "msg": "\"currentPage\": \"1\",\"pageSize\": \"1\"",
#      "url": "/interface/tArticle/selectFlagAll",
#      "mode": "post",
#      "h": {"Content-Type": "application/json"},
#      "d": {"currentPage": "1", "pageSize": "1"},
#      "code": "code",
#      "expected_code": "200",
#      "expected_key": ["code", "data", "list", "flagNo", "total", "id"],
#      }
# ]

selectCategoryAllChild = [
    {
     "interface": "https://testserver.cxjk.com/api/cxjk-article/interface/tArticle/selectCategoryAllChild",
     "msg": "查询正确的id，查询成功",
     "url": "/interface/tArticle/selectCategoryAllChild",
     "mode": "post",
     "h": {"Content-Type": "application/json"},
     "d": {"id": "182", "currentPage": 1, "pageSize": 1},
     "code": "code",
     "expected_code": "200",
     "expected_key": ["code", "data", "id", "categoryNo", "categoryName", "parentCategory", "categoryType", "categoryLevel", "deleteFlag",
                      "createdBy", "createdDate", "updatedBy", "updatedDate"],
     },
    {
     "interface": "https://testserver.cxjk.com/api/cxjk-article/interface/tArticle/selectCategoryAllChild",
     "msg": "查询一级分类，查询成功",
     "url": "/interface/tArticle/selectCategoryAllChild",
     "mode": "post",
     "h": {"Content-Type": "application/json"},
     "d": {"categoryLevel": "1", "currentPage": 1, "pageSize": 1},
     "code": "code",
     "expected_code": "200",
     "expected_key": ["code", "data", "id", "categoryNo", "categoryName", "parentCategory", "categoryType", "categoryLevel", "deleteFlag",
                      "createdBy", "createdDate", "updatedBy", "updatedDate"],
     },
    {
     "interface": "https://testserver.cxjk.com/api/cxjk-article/interface/tArticle/selectCategoryAllChild",
     "msg": "查询二级分类，查询成功",
     "url": "/interface/tArticle/selectCategoryAllChild",
     "mode": "post",
     "h": {"Content-Type": "application/json"},
     "d": {"categoryLevel": "2", "currentPage": 1, "pageSize": 1},
     "code": "code",
     "expected_code": "200",
     "expected_key": ["code", "data", "id", "categoryNo", "categoryName", "parentCategory", "categoryType", "categoryLevel", "deleteFlag",
                      "createdBy", "createdDate", "updatedBy", "updatedDate"],
     },
    {
     "interface": "https://testserver.cxjk.com/api/cxjk-article/interface/tArticle/selectCategoryAllChild",
     "msg": "查询名字为肿瘤科的分类，查询成功",
     "url": "/interface/tArticle/selectCategoryAllChild",
     "mode": "post",
     "h": {"Content-Type": "application/json"},
     "d": {"categoryName": "肿瘤科", "currentPage": 1, "pageSize": 1},
     "code": "code",
     "expected_code": "200",
     "expected_key": ["code", "data", "id", "categoryNo", "categoryName", "parentCategory", "categoryType", "categoryLevel", "deleteFlag",
                      "createdBy", "createdDate", "updatedBy", "updatedDate"],
     },
    {
     "interface": "https://testserver.cxjk.com/api/cxjk-article/interface/tArticle/selectCategoryAllChild",
     "msg": "查询no为CATEGORY00000004的分类，查询成功",
     "url": "/interface/tArticle/selectCategoryAllChild",
     "mode": "post",
     "h": {"Content-Type": "application/json"},
     "d": {"categoryNo": "CATEGORY00000004", "currentPage": 1, "pageSize": 1},
     "code": "code",
     "expected_code": "200",
     "expected_key": ["code", "data", "id", "categoryNo", "categoryName", "parentCategory", "categoryType", "categoryLevel", "deleteFlag",
                      "createdBy", "createdDate", "updatedBy", "updatedDate"],
     },
    {
     "interface": "https://testserver.cxjk.com/api/cxjk-article/interface/tArticle/selectCategoryAllChild",
     "msg": "没有入参",
     "url": "/interface/tArticle/selectCategoryAllChild",
     "mode": "post",
     "h": {"Content-Type": "application/json"},
     "d": {},
     "code": "code",
     "expected_code": "200",
     "expected_key": ["code", "data", "id", "categoryNo", "categoryName", "parentCategory", "categoryType", "categoryLevel", "deleteFlag",
                      "createdBy", "createdDate", "updatedBy", "updatedDate"],
     },
]

selectFlagAll = [
    {
     "interface": "https://testserver.cxjk.com/api/cxjk-article/interface/tArticle/selectFlagAll",
     "msg": "查询正确的id，查询成功",
     "url": "/interface/tArticle/selectFlagAll",
     "mode": "post",
     "h": {"Content-Type": "application/json"},
     "d": {"id": "182", "currentPage": 1, "pageSize": 1},
     "code": "code",
     "expected_code": "200",
     "expected_key": ["code", "data", "id", "flagNo", "flagName", "parentFlag", "flagType", "flagLevel", "deleteFlag",
                      "createdBy", "createdDate", "updatedBy", "updatedDate"],
     },
    {
     "interface": "https://testserver.cxjk.com/api/cxjk-article/interface/tArticle/selectFlagAll",
     "msg": "查询一级标签，查询成功",
     "url": "/interface/tArticle/selectFlagAll",
     "mode": "post",
     "h": {"Content-Type": "application/json"},
     "d": {"flagLevel": "1", "flagType": "0", "currentPage": 1, "pageSize": 1},
     "code": "code",
     "expected_code": "200",
     "expected_key": ["code", "data", "id", "flagNo", "flagName", "parentFlag", "flagType", "flagLevel", "deleteFlag",
                      "createdBy", "createdDate", "updatedBy", "updatedDate"],
     },
    {
     "interface": "https://testserver.cxjk.com/api/cxjk-article/interface/tArticle/selectFlagAll",
     "msg": "查询二级标签，查询成功",
     "url": "/interface/tArticle/selectFlagAll",
     "mode": "post",
     "h": {"Content-Type": "application/json"},
     "d": {"flagLevel": "2", "flagType": "0", "currentPage": 1, "pageSize": 1},
     "code": "code",
     "expected_code": "200",
     "expected_key": ["code", "data", "id", "flagNo", "flagName", "parentFlag", "flagType", "flagLevel", "deleteFlag",
                      "createdBy", "createdDate", "updatedBy", "updatedDate"],
     },
    {
     "interface": "https://testserver.cxjk.com/api/cxjk-article/interface/tArticle/selectFlagAll",
     "msg": "查询名字为test的标签，查询成功",
     "url": "/interface/tArticle/selectFlagAll",
     "mode": "post",
     "h": {"Content-Type": "application/json"},
     "d": {"flagName": "test", "flagType": "0", "currentPage": 1, "pageSize": 1},
     "code": "code",
     "expected_code": "200",
     "expected_key": ["code", "data", "id", "flagNo", "flagName", "parentFlag", "flagType", "flagLevel", "deleteFlag",
                      "createdBy", "createdDate", "updatedBy", "updatedDate"],
     },
    {
     "interface": "https://testserver.cxjk.com/api/cxjk-article/interface/tArticle/selectFlagAll",
     "msg": "查询no为FLAG00000179的标签，查询成功",
     "url": "/interface/tArticle/selectFlagAll",
     "mode": "post",
     "h": {"Content-Type": "application/json"},
     "d": {"flagNo": "FLAG00000179", "currentPage": 1, "pageSize": 1},
     "code": "code",
     "expected_code": "200",
     "expected_key": ["code", "data", "id", "flagNo", "flagName", "parentFlag", "flagType", "flagLevel", "deleteFlag",
                      "createdBy", "createdDate", "updatedBy", "updatedDate"],
     },
]

# selectFlagAllChild = [
#     {
#      "interface": "中心查询标签列表接口",
#      "msg": "没有入参",
#      "url": "/interface/tArticle/selectFlagAllChild",
#      "mode": "post",
#      "h": {"Content-Type": "application/json"},
#      "d": {},
#      "code": "code",
#      "expected_code": "200",
#      "expected_key": ["code", "data", "flagLevel", "flagName", "id", "children", "flagNo"],
#      }
# ]

selectFlagAllChild = [
    {
     "interface": "https://testserver.cxjk.com/api/cxjk-article/interface/tArticle/selectFlagAllChild",
     "msg": "查询正确的id，查询成功",
     "url": "/interface/tArticle/selectFlagAllChild",
     "mode": "post",
     "h": {"Content-Type": "application/json"},
     "d": {"id": "182", "currentPage": 1, "pageSize": 1},
     "code": "code",
     "expected_code": "200",
     "expected_key": ["code", "data", "id", "flagNo", "flagName", "parentFlag", "flagType", "flagLevel", "deleteFlag",
                      "createdBy", "createdDate", "updatedBy", "updatedDate"],
     },
    {
     "interface": "https://testserver.cxjk.com/api/cxjk-article/interface/tArticle/selectFlagAllChild",
     "msg": "查询一级标签，查询成功",
     "url": "/interface/tArticle/selectFlagAllChild",
     "mode": "post",
     "h": {"Content-Type": "application/json"},
     "d": {"flagLevel": "1", "flagType": "0", "currentPage": 1, "pageSize": 1},
     "code": "code",
     "expected_code": "200",
     "expected_key": ["code", "data", "id", "flagNo", "flagName", "parentFlag", "flagType", "flagLevel", "deleteFlag",
                      "createdBy", "createdDate", "updatedBy", "updatedDate"],
     },
    {
     "interface": "https://testserver.cxjk.com/api/cxjk-article/interface/tArticle/selectFlagAllChild",
     "msg": "查询二级标签，查询成功",
     "url": "/interface/tArticle/selectFlagAllChild",
     "mode": "post",
     "h": {"Content-Type": "application/json"},
     "d": {"flagLevel": "2", "flagType": "0", "currentPage": 1, "pageSize": 1},
     "code": "code",
     "expected_code": "200",
     "expected_key": ["code", "data", "id", "flagNo", "flagName", "parentFlag", "flagType", "flagLevel", "deleteFlag",
                      "createdBy", "createdDate", "updatedBy", "updatedDate"],
     },
    {
     "interface": "https://testserver.cxjk.com/api/cxjk-article/interface/tArticle/selectFlagAllChild",
     "msg": "查询名字为test的标签，查询成功",
     "url": "/interface/tArticle/selectFlagAllChild",
     "mode": "post",
     "h": {"Content-Type": "application/json"},
     "d": {"flagName": "test", "flagType": "0", "currentPage": 1, "pageSize": 1},
     "code": "code",
     "expected_code": "200",
     "expected_key": ["code", "data", "id", "flagNo", "flagName", "parentFlag", "flagType", "flagLevel", "deleteFlag",
                      "createdBy", "createdDate", "updatedBy", "updatedDate"],
     },
    {
     "interface": "https://testserver.cxjk.com/api/cxjk-article/interface/tArticle/selectFlagAllChild",
     "msg": "查询no为FLAG00000179的标签，查询成功",
     "url": "/interface/tArticle/selectFlagAllChild",
     "mode": "post",
     "h": {"Content-Type": "application/json"},
     "d": {"flagNo": "FLAG00000179", "currentPage": 1, "pageSize": 1},
     "code": "code",
     "expected_code": "200",
     "expected_key": ["code", "data", "id", "flagNo", "flagName", "parentFlag", "flagType", "flagLevel", "deleteFlag",
                      "createdBy", "createdDate", "updatedBy", "updatedDate"],
     },
    {
     "interface": "https://testserver.cxjk.com/api/cxjk-article/interface/tArticle/selectFlagAllChild",
     "msg": "没有入参",
     "url": "/interface/tArticle/selectFlagAllChild",
     "mode": "post",
     "h": {"Content-Type": "application/json"},
     "d": {},
     "code": "code",
     "expected_code": "200",
     "expected_key": ["code", "data", "id", "flagNo", "flagName", "parentFlag", "flagType", "flagLevel", "deleteFlag",
                      "createdBy", "createdDate", "updatedBy", "updatedDate"],
     },
]

findArticleReadTimes = [
    {
     "interface": "https://testserver.cxjk.com/api/cxjk-article/interface/tArticle/findArticleReadTimes",
     "msg": "正确文章No查询阅读量，查询成功",
     "url": "/interface/tArticle/findArticleReadTimes",
     "mode": "post",
     "h": {"Content-Type": "application/json"},
     "d": {"articleNo": "ARTICLE00001903"},
     "code": "code",
     "expected_code": "200",
     "expected_key": ["code", "data", "msg"]
     }
]

findArticleReadTimes2 = [
    {
     "interface": "https://testserver.cxjk.com/api/cxjk-article/interface/tArticle/findArticleReadTimes",
     "msg": "错误文章No查询阅读量，查询失败",
     "url": "/interface/tArticle/findArticleReadTimes",
     "mode": "post",
     "h": {"Content-Type": "application/json"},
     "d": {"articleNo": "xxxx"},
     "code": "code",
     "expected_code": "200",
     "expected_key": ["code", "data", "msg"]
     },
    {
     "interface": "https://testserver.cxjk.com/api/cxjk-article/interface/tArticle/findArticleReadTimes",
     "msg": "文章No为空查询阅读量，查询失败",
     "url": "/interface/tArticle/findArticleReadTimes",
     "mode": "post",
     "h": {"Content-Type": "application/json"},
     "d": {"articleNo": ""},
     "code": "code",
     "expected_code": "500",
     "expected_key": ["code", "data", "msg"]
     }
]

getWxConfig = [
    {
     "interface": "https://testserver.cxjk.com/api/cxjk-article/interface/tArticle/getWxConfig",
     "msg": "正确文章No查询阅读量，查询成功",
     "url": "/interface/tArticle/getWxConfig",
     "mode": "post",
     "h": {"Content-Type": "application/json"},
     "d": {"articleNo": "ARTICLE00001903"},
     "code": "code",
     "expected_code": "200",
     "expected_key": ["code", "data", "msg"]
     }
]

selectAllListNew = [
    {
     "interface": "https://testserver.cxjk.com/api/cxjk-article/interface/tArticle/selectAllListNew",
     "msg": "查询文章列表_新，查询成功",
     "url": "/interface/tArticle/selectAllListNew",
     "mode": "post",
     "h": {"Content-Type": "application/json"},
     "d": {},
     "code": "code",
     "expected_code": "200",
     "expected_key": ["code", "data", "msg"]
     }
]

selectAllPageNew = [
    {
     "interface": "https://testserver.cxjk.com/api/cxjk-article/interface/tArticle/selectAllPageNew",
     "msg": "查询文章分页_新，查询成功",
     "url": "/interface/tArticle/selectAllPageNew",
     "mode": "post",
     "h": {"Content-Type": "application/json"},
     "d": {"currentPage": "1", "pageSize": "1"},
     "code": "code",
     "expected_code": "200",
     "expected_key": ["code", "data", "msg"]
     }
]

selectListNew = [
    {
     "interface": "https://testserver.cxjk.com/api/cxjk-article/interface/tArticle/selectListNew",
     "msg": "查询文章列表_新，查询成功",
     "url": "/interface/tArticle/selectListNew",
     "mode": "post",
     "h": {"Content-Type": "application/json"},
     "d": {},
     "code": "code",
     "expected_code": "200",
     "expected_key": ["code", "data", "msg"]
     }
]

selectPageNew = [
    {
     "interface": "https://testserver.cxjk.com/api/cxjk-article/interface/tArticle/selectPageNew",
     "msg": "查询文章分页_新，查询成功",
     "url": "/interface/tArticle/selectPageNew",
     "mode": "post",
     "h": {"Content-Type": "application/json"},
     "d": {"currentPage": "1", "pageSize": "1"},
     "code": "code",
     "expected_code": "200",
     "expected_key": ["code", "data", "msg"]
     }
]

selectArticleFlag = [
    {
     "interface": "https://testserver.cxjk.com/api/cxjk-article/interface/tArticle/selectArticleFlag",
     "msg": "查询文章的标签，查询成功",
     "url": "/interface/tArticle/selectArticleFlag",
     "mode": "post",
     "h": {"Content-Type": "application/json"},
     "d": {"articleNo": "ARTICLE00001903"},
     "code": "code",
     "expected_code": "200",
     "expected_key": ["code", "data", "msg"]
     }
]

selectArticleImage = [
    {
     "interface": "https://testserver.cxjk.com/api/cxjk-article/interface/tArticle/selectArticleImage",
     "msg": "查询文章img，查询成功",
     "url": "/interface/tArticle/selectArticleImage",
     "mode": "post",
     "h": {"Content-Type": "application/json"},
     "d": {"articleNo": "ARTICLE00001903"},
     "code": "code",
     "expected_code": "200",
     "expected_key": ["code", "data", "msg"]
     }
]
