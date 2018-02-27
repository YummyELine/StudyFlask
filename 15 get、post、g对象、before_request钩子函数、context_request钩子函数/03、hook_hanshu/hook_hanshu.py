#!/usr/bin/env python
# encoding:utf-8

from flask import Flask, render_template, request, session, url_for, redirect, g
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)


@app.route('/')
def hello_world():
	return render_template('index.html')


@app.route('/login/', methods=['GET', 'POST'])
def login():
	print('login')
	if request.method == 'GET':
		return render_template('login.html')
	else:
		username = request.form.get('username')
		password = request.form.get('password')
		if username == 'z' and password == '1':
			session['username'] = 'z'
			return '登录成功'
		else:
			return '用户名或者密码错误！'


@app.route('/edit/')
def eidt():
	render_template('edit.html')


# if session.get('username'):
# 	return '修改成功'
# else:
# 	return redirect(url_for('login'))


# if hasattr(g, 'username'):
# 	return '修改成功'
# else:
# 	return redirect(url_for('login'))


# before_request: 在请求之前执行的。
# before_request: 是在试图函数执行之前执行的。
# before_request这个函数只是一个装饰器，他可以把需要设置为钩子函数的代码放到视图函数执行之前来执行

@app.before_request
def my_before_request():
	if session.get('username'):
		g.username = session.get('username')
	print('hello world')


@app.context_processor
def my_context_processor():
	# username = session.get('username')
	# if username:
	return {'username': 'z'}


if __name__ == '__main__':
	app.run()
