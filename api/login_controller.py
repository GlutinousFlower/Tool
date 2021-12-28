# -*- coding: utf-8 -*-
# @Time : 2021/12/20 6:11 下午
# @Author : xiaoluping
# @Email : xiaoluping@yuanfudao.com
# @File : login_controller.py

import requests


def login_by_password(phone, password):
    data = {
        'phone': phone,
        'password': password
    }
    url='https://api2.mubu.com/v3/api/user/phone_login'
    res=requests.post(url=url,data=data)
    return res

