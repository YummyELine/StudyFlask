#!/usr/bin/env python
# encoding:utf-8

from flask_script import Manager
from migrate_demo import app
from flask_migrate import Migrate, MigrateCommand
from exts import db
from models import Article

# python manage.py db init  第一此执行
# python manage.py db migrate 都要执行
# python manage.py db upgrade 都要执行
# 模型 -> 迁移文件 -> 表
manager = Manager(app)

# 1.要使用flask_migrate，必须绑定app和db
migrate = Migrate(app, db)

# 2.把MigrateCommand命令添加到manager中
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
	manager.run()
