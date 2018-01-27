#!/usr/bin/env python
# coding:utf-8
from flask_script import Manager

DBmanager = Manager()


@DBmanager.command
def init():
    print('数据库初始化完成')


@DBmanager.command
def migrate():
    print('数据表迁移成功')
