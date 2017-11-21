#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Gu Xianxiong'

import orm
from models import User


if __name__ == '__main__':
#     orm.create_db()
#     Session = orm.getSessionCls()
#     session = Session()
#
#
# #定义一个字段
#     zengjia = User(id=2, name='sbliuyao')
# #添加字段
#     session.add(zengjia)
# #添加多个字段
#     session.add_all([
#         User(id=3, name='sbyao'),
#         User(id=4, name='liuyao')
#     ])
# #提交以上操作
#     session.commit()

    import time, uuid
    t = int(time.time() * 1000)
    id =  uuid.uuid4().hex
    ss = '%015d%s000' % (t, id)

    print(t)
    print(id)
    print(ss)