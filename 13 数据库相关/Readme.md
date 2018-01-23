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