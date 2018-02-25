#!/usr/bin/env python
# encoding:utf-8

from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def hello_world():
	return render_template('index.html')


@app.route('/search/')
def search():
	print(request.args)  # 返回字典
	return 'search:{}'.format(request.args.get('q'), )


# 默认的视图函数，只能采用Get请求
# 如果你想采用POST请求，那么要写明
@app.route('/login/', methods=['GET', 'POST'])
def login():
	if request.method == 'GET':
		return render_template('login.html')
	else:
		username = request.form.get('username')
		password = request.form.get('password')
		return 'post request{},{}'.format(username, password)


if __name__ == '__main__':
	app.run(debug=True)
