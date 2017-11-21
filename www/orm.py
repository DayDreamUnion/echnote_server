#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Gu Xianxiong'
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from  sqlalchemy.orm import sessionmaker

global __SessionCls

#生成一个SqlORM 基类
Base = declarative_base()
#echo如果为True，那么当他执行整个代码的数据库的时候会显示过程
engine = create_engine("mysql+pymysql://root:Qwer4321@118.31.90.219:3306/echnote", max_overflow=5, echo=True)

def create_db():
    global __SessionCls
    Base.metadata.create_all(engine)  # 创建所有表结构
    __SessionCls = sessionmaker(bind=engine)

def getSessionCls():
    global __SessionCls

    if __SessionCls is None:
        create_db()
    return __SessionCls

