#!/usr/bin/env python
# encoding:utf-8

from flask import g


def login_log():
	print('当前登录用户是{}'.format(g.username, ))


def login_ip_log():
	pass
