#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:余振新
@file: ddd.py
@time: 2020/04/22
"""
import unittest
import ddt
from common.base_request import RequestInterface
from common.base_compare import CompareParm
import requests
from public import config
import json
import yaml
data_path = config.data_path+'111.yml'
print(data_path)
with open(data_path, "r+", encoding='utf-8') as file:
    y = yaml.load_all(file, Loader=yaml.FullLoader)
    print(y)
