# encoding: utf-8

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    context = {'username': '小E',
              'gender': '男',
              'age': '18'}
    return  render_template('index.html', **context)
    # 参数少可用这个方式 return render_template('index.html', username='小E', gender='男', age='18')


if __name__ == '__main__':
    app.run(debug=True)
