# -*- coding: utf-8 -*-
# @Time : 2021/12/24 2:40 下午
# @Author : xiaoluping
# @Email : xiaoluping@yuanfudao.com
# @File : config_parser.py

import configparser


class EnvConfigParser(object):
    """configparser对象"""

    def __init__(self, path):
        self.config = configparser.RawConfigParser()
        self.config.read(path, encoding='utf-8')
