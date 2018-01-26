from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import config

app = Flask(__name__)
app.config.from_object(config)
db = SQLAlchemy(app)


# 用户表
# create table users( id int primary key autoincrement, username varchar(100) not null)
# create table article( id int primary key  autoincrement, title varchar(100) not null
# content text not null , author_id int, foreign key 'author_id' refernces 'users.id')
class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(100), nullable=False)


class Article(db.Model):
    __tablename__ = 'article'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    # 关系 正向引用，与反向引用。
    author = db.relationship('User', backref=db.backref('articles'))


db.create_all()


@app.route('/')
def hello_world():
    # # 1想要添加一篇文章，因为文章必须依赖用户而存在，所以首相的话，先添加一个用户。
    # user1 = User(username='小E')
    # db.session.add(user1)
    # db.session.commit()
    # 2
    # article = Article(title= 'aaa', content= 'bbb', author_id=1)
    # db.session.add(article)
    # db.session.commit()
    # 3
    # # 我要找文章标题为aaa的这个作者
    # artile = Article.query.filter(Article.title=='aaa').first()
    # author_id = artile.author_id
    # user = User.query.filter(User.id == author_id).first()
    # print ('username:{}'.format(user.username))

    # # 4
    #     artile = Article(title='aaa',content='bbb')
    #     artile.author = User.query.filter(User.id==1).first()
    #     db.session.add(artile)
    #     db.session.commit()

    # 5
    # 我要找文件标题为aaa的 这个作者
    # article = Article.query.filter(Article.title == 'aaa').first()
    # print('UserName:{}'.format(article.author.username))

    # 6
    # # 我要找到这个用户写过的所有文章
    # article =Article(title='111',content='222',author_id=1)
    # db.session.add(article)
    # db.session.commit()
    user = User.query.filter(User.username == '小E').first()
    results = user.articles
    for result in results:
        print('-')
        print(result.title)

    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
