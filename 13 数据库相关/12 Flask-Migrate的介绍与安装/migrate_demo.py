from flask import Flask
from exts import db
import config
# from models import Article  # 没有用migrate的情况

app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)

# # 这边涉及到了上下文的知识，需要用with把app加载到app栈才能创建。 # 没有用migrate的情况。
# with app.app_context():
# 	db.create_all()

# 新建一个article模型，采用models分开的方式
# flask-scripts的方式


@app.route('/')
def hello_world():
	return 'Hello World!'


if __name__ == '__main__':
	app.run()
