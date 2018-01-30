# Flask数据库的对接相关

## 1 数据库的安装：

1. Mysql为例
2. https://dev.mysql.com/downloads/mysql/
3. mac 设置初始化密码的命令是：

``` mysql
mysqladmin -uroot password [password]
```

## 02 MySQL-python 中间件的安装

1. windows可以通过anaconda 直接安装管理,conda升级方法。

``` anaconda
conda update conda
conda install -c anaconda navigator-updater
```

2. 如果是python3.X以上安装的插件就是‘pymysql’这个插件
3. 如果是在linux 或者 mac 直接进入虚拟环境，输入‘sudo pip install mysql-python’

## 03 Flask-SQLalchemy的介绍与安装：

1. ORM:Object Relationship Mapping(模型关系映射)
2. flask-sqlalchemy是一套ORM框架。
3. ORM的好处：可以让我们操作数据库跟操作对象一样，非常方便。因为一个表示抽象成一个类，一条数据就抽象成该类的一个对象。
4. anaconda安装方法

``` anaconda
conda install -c conda-forge flask-sqlalchemy
```

## 04 sqlalchemy的使用：

1. 初始化和设置数据库配置信息：

* 使用sqlalchemy中的功能进行初始化：

``` python
from flask import Flask
import sqlalchemy as orm
import config
app = Flask(__name__)
db = orm.create_engine(config.SQLALCHEMY_DATABASE_URI, echo=True)
metadata = orm.MetaData(db)
```

2. 设置配置信息：在‘config.py'文件中添加一下配置信息：

``` python
# dialect+driver://username:password@host:port/database
DIALECT = 'mysql'
DRIVER = 'pymysql'
USERNAME = 'root'
PASSWORD = 'root'
HOST = '127.0.0.1'
PORT = '3306'
DATABASE = 'db_demo1'
SQLALCHEMY_DATABASE_URI = "{}+{}://{}:{}@{}:{}/{}?charset=utf8".format(DIALECT, DRIVER, USERNAME,
                                             PASSWORD, HOST, PORT, DATABASE)
```

3. 在主‘app’文件中，添加配置文件：

``` python
metadata = orm.MetaData(db)
```

4. 做测试，看有没有问题：

``` python
metadata.create_all()
```

* 如果没有报错，说明配置没有问题，如果有错误，可以根据错误进行修改。

## 05 使用sqlalchemy创建模型与表的映射，增删改查：

1. 看代码。

## 06 sqlalchemy连接数据库

1. mysql 命令：

```mysql
drop database db_demo1;
mysql -uroot -p;
create database db_demo1 charset utf8;
```

2. 初始化和设置数据库配置信息

``` anaconda 安装MYSQL驱动
conda config --set ssl_verify false
conda update requests
conda install  mysql-connector-python
```

* 使用flask_sqlalchemy中的SQLALchemy 进行初始化：

```python
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config.from_object(config)
db = SQLAlchemy(app)
```

3. 设置配置信息：在‘config’文件中添加一下配置信息：

```python
#!/usr/bin/env python
# coding:utf-8

# dialect+driver://username:password@host:port/database

DIALECT = 'mysql'
DRIVER = 'mysqlconnector'
USERNAME = 'root'
PASSWORD = 'root'
HOST = '127.0.0.1'
PORT = '3306'
DATABASE = 'db_demo1'

SQLALCHEMY_DATABASE_URI = "{}+{}://{}:{}@{}:{}/{}?charset=utf8".format(DIALECT,DRIVER, USERNAME, PASSWORD, HOST, PORT, DATABASE)
SQLALCHEMY_TRACK_MODIFICATIONS = False
```

4. 在主APP文件中，添加配置文件：

```python
app = Flask(__name__)
app.config.from_object(config)
db = SQLAlchemy(app)
```

5. 做测试，看有没有问题：

```pyton
db.create_all()
```

如果没有报错，说明配置没有问题，如果有错误，可以根据错误进行修改。

## 07 使用Flask-SQLALchemy创建模型与表的映射。

1. 模型需要继承自‘db.Model’，然后需要映射到表中的属性，必须写成‘db.Column’的数据类型。
2. 数据类型
* ‘db.Integer’代表的是整形。
* ‘db.String’代表的是‘varchar’，需要指定最长的长度。
* ‘db.Text’代表的是‘text’

3. 其他参数：
* ‘primary_key’：代表的是将这个字段设置为主键。
* ‘autoincrement’：代表的是这个主键为自增长的。
* ‘nullable’：代表的是这个字段是否可以为空，默认可以为空，可以将这个值设置为‘False’，在数据库中，这个值就不能为空了。

4. 最后需要调用‘db.create_all’来将模型真正的创建到数据库中。

## 08 Flask-SQLALchemy数据的增、删、改、查：

1. 增：

```python
    #  增加：
    article1 = Article(title='aaa', content='bbb')
    db.session.add(article1)
    # 事物
    db.session.commit()
```

2. 查：

```python
   # 查
    # select * from article where title='aaa'
    result = Article.query.filter(Article.title == 'aaa').all()
    article1 = result[0]
    print(article1.title)
    print(article1.content)
    Article.query.filter(Article.title == 'aaa').first()

```

3. 改：

```python
    # 改
    # 1.先把你要改的数据查找出来
    article1 = Article.query.filter(Article.title == 'aaa').first()
    # 2.把这条数据，你需要修改的地方进行修改。
    article1.title = 'new title'
    # 3.做事物的提交。
    db.session.commit()
```

4. 删：

```python
  # 删
    # 1.把需要删除的数据查找出来。
    article1 = Article.query.filter(Article.content=='bbb').first()
    # 2.把这条数据删除掉
    db.session.delete(article1)
    # 3.做事物提交
    db.session.commit()
```

## 09 Flask_SQLALchemy外键及其关系：

1. 外键：

``` python
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
```

2. "author = db.relationship('User', backref=db.backref('articles'))"解释：
* 给‘Article’这个模型添加一个‘author’属性，可以访问这篇文章作者的数据，像访问普通模型一样。
* ‘backref’是定义反向引用，可以通过‘User.articles’这个模型访问这个模型所写的所有文章。

3. 多对多：
* 多对多的关系，要通过一个中间表进行关联。
* 中间表，不能通过‘class’的方式实现，只能通过‘db.Table’的方式实现。
* 设置关联：‘tags = db.relationship('Tag', secondary=article_tag, backref=db.backref('articles'))’需要使用一个关键字参数‘secondary=中间表’来进行关联。
* 访问和数据添加可以通过一下方式进行操作：

添加数据：

```python
    article1 = Article(title='aaa')
    article2 = Article(title='bbb')

    tag1 = Tag(name='111')
    tag2 = Tag(name='222')

    article1.tags.append(tag1)
    article1.tags.append(tag2)

    article2.tags.append(tag2)
    article2.tags.append(tag1)

    db.session.add(article1)
    db.session.add(article2)
    db.session.add(tag1)
    db.session.add(tag2)
    db.session.commit()

```

访问数据：

```python
    article1 = Article.query.filter(Article.title=='aaa').first()
    tags = article1.tags
    for tag in tags:
        print(tag.name)

```

## 10 Flask-Script的介绍与安装：

1. Flask-Script: Flask-Script的作用是可以通过命令的形式来操作Flask.例如通过命令跑一个开发版本的服务器、设置数据库，定时任务等。
2. 安装：进入到虚拟环境中，然后'pip install flask-script'来进行安装，anaconda使用命令‘conda install -c conda-forge flask-script’。
3. 如果直接在主‘manage.py’中写命令，那么在终端就只要‘pyton manage.py command_name’就可以了。
4. 如果把一些命令集中在一个文件中，那么在终端就需要输入一个父命令，比如‘python manage.py db init’。
5. 例子：

```python
#!/usr/bin/env python
# encoding:utf-8

from flask_script import Manager
from flask_script_demo import app
from db_scripys import DBmanager

manager = Manager(app)


# 和数据库相关的操作，我都放在一起。
@manager.command
def runserver():
    print('服务器跑起来了。')


manager.add_command('db', DBmanager)

if __name__ == '__main__':
    manager.run()
```

6. 有子命令的列子:

```python
#!/usr/bin/env python
# coding:utf-8
from flask_script import Manager

DBmanager = Manager()


@DBmanager.command
def init():
    print('数据库初始化完成')


@DBmanager.command
def migrate():
    print('数据表迁移成功')
```

## 11 分开‘models’已经解决循环引用：

1. 分开models的目的：为了让代码更加方便的管理。
2. 如何解决循环引用：把‘db’放在一个单独的文件中，切断循环引用的线条就可以了。

## 12 Flask-Migrate的介绍与安装：
