#!/usr/bin/env python
# coding:utf-8

# dialect+driver://username:password@host:port/database

DIALECT = 'mysql'
DRIVER = 'pymysql'
USERNAME = 'root'
PASSWORD = 'root'
HOST = '127.0.0.1'
PORT = '3306'
DATABASE = 'db_demo1'

SQLALCHEMY_DATABASE_URI = "{}+{}://{}:{}@{}:{}/{}?charset=utf8".format(DIALECT, DRIVER, USERNAME,
                                             PASSWORD, HOST, PORT, DATABASE)
