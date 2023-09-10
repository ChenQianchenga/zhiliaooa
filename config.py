# -*- coding: utf-8 -*-#
# --------------------------------------------------------------------------
# ProjectName：zhiliaooa
# Name:config.py
# Description: 用来存常用的配置
# Author:ChenQiancheng
# Date:2023/9/10  20:20
# --------------------------------------------------------------------------
# 数据库配置信息
HOSTNAME = "127.0.0.1"
PORT = "3306"
DATABASE = "zhiliaooa"
USERNAME = "root"
PASSWORD = "root"
DB_URI = f"mysql+pymysql://{USERNAME}:{PASSWORD}@{HOSTNAME}:{PORT}/{DATABASE}?charset=utf8mb4"
SQLALCHEMY_DATABASE_URI = DB_URI
