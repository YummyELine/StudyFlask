#!/usr/bin/env python
# encoding:utf-8

from flask import Flask, session
import os
from datetime import timedelta

# import config  #方法一样用其中一种就可以了

app = Flask(__name__)
# app.config.from_object(config)
# app.config['SECRET_KEY']='24个字符的字符串'
app.config['SECRET_KEY'] = os.urandom(24)
# 设置过期的时间为7天，如果没有设置默认是31天。
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=7)


# 添加数据到session中
# 操作session的时候，跟操作字典是一样的。
# SECRET_KEY
@app.route('/')
def hello_world():
	session['username'] = 'Ee'
	# 如果没有指定session的过期时间，那么默认是浏览器关闭后就自动结束。
	# 如果设置了session的permanent属性为True,那么过期时间是31天。
	session.permanent = True

	return 'Hello World!'


@app.route('/get/')
def get():
	# session['username']
	# session.get['username']
	return session.get('username')


@app.route('/delete/')
def delete():
	print(session.get('username'))
	session.pop('username')
	print(session.get('username'))
	return 'success'


@app.route('/clear/')
def clear():
	print(session.get('username'))
	# 删除session中的所有数据。
	session.clear()
	print(session.get('username'))
	return 'success'


if __name__ == '__main__':
	app.run(debug=True)
