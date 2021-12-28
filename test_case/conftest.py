# -*- coding: utf-8 -*-
# @Time : 2021/12/20 6:18 下午
# @Author : xiaoluping
# @Email : xiaoluping@yuanfudao.com
# @File : conftest.py
import sys
import pytest
from constants.constants import ENV_ONLINE, ENV_TEST, DEFAULT_ENV


@pytest.fixture(scope="session")
def get_env_config():
    env = DEFAULT_ENV
    try:
        if sys.argv[1] in ['test', 'online']:
            env = sys.argv[1]
    except IndexError:
        print('请指定运行环境')

    if env == ENV_ONLINE:
        return "online"
    elif env == ENV_TEST:
        return "test"
