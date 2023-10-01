# -*- coding: utf-8 -*-#
# --------------------------------------------------------------------------
# ProjectName：zhiliaooa
# Name:decorators.py
# Description:
# Author:ChenQiancheng
# Date:2023/9/30  22:04
# --------------------------------------------------------------------------
from functools import wraps
from flask import g, redirect, url_for


def login_required(func):
    # 保留func的信息
    @wraps(func)
    def inner(*args, **kwargs):
        if g.user:
            return func(*args, **kwargs)
        else:
            return redirect(url_for("auth.login"))

    return inner
