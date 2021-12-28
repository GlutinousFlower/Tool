# -*- coding: utf-8 -*-
# @Time : 2021/12/20 6:17 下午
# @Author : xiaoluping
# @Email : xiaoluping@yuanfudao.com
# @File : test_login.py

from api.login_controller import *
import allure
import logging
import pytest


@allure.feature('登录case')
class TestLogin:
    @allure.story('测试密码登录')
    @pytest.mark.parametrize('phone', '18211172837')
    @pytest.mark.parametrize('password', 'xlp19961105')
    def test_login_by_password(self, phone, password,get_env_config):
        print(get_env_config)
        res = login_by_password(phone, password)
        logging.info(res.__dict__)
        res.status_code == 200
