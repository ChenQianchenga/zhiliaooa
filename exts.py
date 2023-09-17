# -*- coding: utf-8 -*-#
# --------------------------------------------------------------------------
# ProjectName：zhiliaooa
# Name:exts.py
# Description:  扩展文件，避免循环引用
# Author:ChenQiancheng
# Date:2023/9/10  20:22
# --------------------------------------------------------------------------
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail

db = SQLAlchemy()
mail = Mail()