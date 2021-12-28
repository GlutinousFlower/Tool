# -*- coding: utf-8 -*-
# @Time : 2021/12/20 6:05 下午
# @Author : xiaoluping
# @Email : xiaoluping@yuanfudao.com
# @File : run.py

import pytest
import urllib3
import logging
from common.Shell import *

try:
    urllib3.disable_warnings()

    shell = Shell()
    xml_report_path = '/Users/luping.xiao/work/gitResp/Tool/report/xml'
    html_report_path = '/Users/luping.xiao/work/gitResp/Tool/report/html'

    args = ['-s', '-q', '--alluredir', xml_report_path, '--clean-alluredir']
    pytest.main(args)

    cmd_generate = 'allure generate %s -o %s --clean' % (xml_report_path, html_report_path)
    cmd_open = 'allure open -h 127.0.0.1 -p 8083 %s' % html_report_path
    shell.invoke(cmd_generate)
    shell.invoke(cmd_open)



except Exception as e:
    logging.error('用例执行失败，请检查环境配置。失败原因：', e)
