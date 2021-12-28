# -*- coding: utf-8 -*-
# @Time : 2021/12/28 3:15 下午
# @Author : xiaoluping
# @Email : xiaoluping@yuanfudao.com
# @File : Shell.py

import subprocess


class Shell:
    @staticmethod
    def invoke(cmd):
        output, errors = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
        o = output.decode("utf-8")
        return o
