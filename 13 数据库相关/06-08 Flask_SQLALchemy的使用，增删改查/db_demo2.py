from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import config

app = Flask(__name__)
app.config.from_object(config)
db = SQLAlchemy(app)


# # 正常的SQL语句。
# article表：
# create table article(
#     id int primary key autoincrement,
#     title varchar(100) not null,
#     content text not null,
# )

# 创建orm 与表之间的关系模型。
class Article(db.Model):
    __tablename__ = 'article'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)


db.create_all()


@app.route('/')
def hello_world():
    # #  增加：
    # article1 = Article(title='aaa', content='bbb')
    # db.session.add(article1)
    # # 事物
    # db.session.commit()

    # # 查
    # # select * from article where title='aaa'
    # result = Article.query.filter(Article.title == 'aaa').all()
    # article1 = result[0]
    # print(article1.title)
    # print(article1.content)
    # Article.query.filter(Article.title == 'aaa').first()

    # # 改
    # # 1.先把你要改的数据查找出来
    # article1 = Article.query.filter(Article.title == 'aaa').first()
    # # 2.把这条数据，你需要修改的地方进行修改。
    # article1.title = 'new title'
    # # 3.做事物的提交。
    # db.session.commit()

    # 删
    # 1.把需要删除的数据查找出来。
    article1 = Article.query.filter(Article.content=='bbb').first()
    # 2.把这条数据删除掉
    db.session.delete(article1)
    # 3.做事物提交
    db.session.commit()

    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
