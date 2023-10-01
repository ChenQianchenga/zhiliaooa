# -*- coding: utf-8 -*-#
# --------------------------------------------------------------------------
# ProjectName：zhiliaooa
# Name:config.py
# Description: 用来存常用的配置
# Author:ChenQiancheng
# Date:2023/9/10  20:20
# --------------------------------------------------------------------------
SECRET_KEY = "qiancheng"
# 数据库配置信息
HOSTNAME = "127.0.0.1"
PORT = "3306"
DATABASE = "zhiliaooa"
USERNAME = "root"
PASSWORD = "root"
DB_URI = f"mysql+pymysql://{USERNAME}:{PASSWORD}@{HOSTNAME}:{PORT}/{DATABASE}?charset=utf8mb4"
SQLALCHEMY_DATABASE_URI = DB_URI

# 邮箱配置
MAIL_SERVER = "smtp.qq.com"
MAIL_USE_SSL = True
MAIL_PORT = 465
MAIL_USERNAME = "980938541@qq.com"
MAIL_PASSWORD = "jqmssmqamwlfbdaj"
MAIL_DEFAULT_SENDER = "980938541@qq.com"
