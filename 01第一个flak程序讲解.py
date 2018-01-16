# 从Flask这个框架中导入Flask这个类
from flask import Flask
# 初始化一个Flask对象
# Flask（）
# 需要传递一个参数__name__
# 1.方便flask框架去寻找资源
# 2.方便flask插件比如Flask-Sqlalchemy出现错误的时候，好去寻找问题所在的位置
app = Flask(__name__)

# @app.route是一个装饰器
# @开头，并且在函数的上面，说明是装饰器
# 这个装饰器的作用，是做一个URL与视图函数的映射。
# 127.0.0.1:5000/  -> 去请求hello_world()这个函数，然后将结果返回给浏览器
@app.route('/')
def hello_world():
    return 'Hello World!'

# 如果当前这个文件是作为入口程序运行，那么就执行app.run()
if __name__ == '__main__':
    # app.run()
    # 启动一个应用服务器，来接受用户的请求
    # 一直在监听，相当于
    #  while Ture：
    #   listen()
    app.run()
