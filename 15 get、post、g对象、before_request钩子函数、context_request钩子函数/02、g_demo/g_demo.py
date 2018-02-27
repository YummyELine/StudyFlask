#!/usr/bin/env python
# encoding:utf-8

from flask import Flask, g, render_template, request
from utils import login_log

app = Flask(__name__)


@app.route('/')
def hello_world():
	return 'Hello World!'


@app.route('/login/', methods=['GET', 'POST'])
def login():
	if request.method == 'GET':
		return render_template('login.html')
	else:
		g.useername = request.form.get('username')
		g.password = request.form.get('password')
		if g.useername == 'z' and g.password == '1':
			# 默认当前这个用户的用户名和密码正确
			login_log()
			return '恭喜登录成功！'
		else:
			return '你的用户名或密码错误！'


if __name__ == '__main__':
	app.run()
