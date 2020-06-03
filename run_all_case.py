#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:余振新
@file: run_all_case.py
@time: 2020/1/14
"""
import unittest
# from HTMLTestRunner_cn import HTMLTestRunner
from common .HTMLTestRunner_cn import HTMLTestRunner
import time

test_dir = './test_case'
discover = unittest.defaultTestLoader.discover(start_dir=test_dir, pattern="test*.py")
# print(discover)

if __name__ == '__main__':
    report_dir = './test_report'
    # 时间戳会导致jenkins无法报告展示，去掉
    # now = time.strftime("%Y-%m-%d %H_%M_%S")
    # report_name = report_dir+'/'+now+'result.html'
    report_name = report_dir+'/'+'result.html'
    with open(report_name, 'wb') as f:
        runner = HTMLTestRunner(stream=f,
                                title="文章中台测试报告",
                                description="共28个接口：查询接口17个2个已停用，操作接口11个")   # retry=1  失败重跑次数
        runner.run(discover)
    f.close()
