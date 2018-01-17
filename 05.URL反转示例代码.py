# encoding: utf-8

from flask import Flask,url_for

app = Flask(__name__)

@app.route('/')
def index():
    print(url_for('my_list'))
    print(url_for('article',id='123'))
    return 'Hello World!'
@app.route('/list/')
def my_list():
    print('list')

@app.route('/article/<id>')
def article(id):
    return('您请求的参数是：{0}'.format(id))

if __name__ == '__main__':
    app.run(debug = True)
