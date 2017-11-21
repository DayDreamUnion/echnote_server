#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Gu Xianxiong'

import time, uuid
from orm import Base
from sqlalchemy import Column, Integer, String


def next_id():
    return '%015d%s000' % (int(time.time() * 1000), uuid.uuid4().hex)

class User(Base):
    __tablename__ = 'user'
    # 表结构
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    password = Column(String(50))




