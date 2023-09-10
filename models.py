#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   models.py
@Time    :   2023/09/10 20:33
@Author  :   O_qiancheng.chen
@Description :   数据库模型
"""
from datetime import datetime

from exts import db


class UserModel(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    join_time = db.Column(db.DateTime, default=datetime.now)
