### 01 数据库的安装：
1. Mysql为例
2. https://dev.mysql.com/downloads/mysql/
3. mac 设置初始化密码的命令是：
```
mysqladmin -uroot password [password]
```

### MySQL-python 中间件的安装
1. windows可以通过anaconda 直接安装管理,conda升级方法。
```
conda update conda
conda install -c anaconda navigator-updater 
```
2. 如果是python3.X以上安装的插件就是‘pymysql’这个插件
3. 如果是在linux 或者 mac 直接进入虚拟环境，输入‘sudo pip install mysql-python’
