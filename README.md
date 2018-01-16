# StudyFlask
自己学习Flask的一些笔记。

### 01第一个flask程序讲解：
1. 第一次创建项目的时候，要添加flask的虚拟环境的时候，一定要选择到Python这个执行文件，比如如的flask的虚拟环境目录在/user/virtualenv/flask-env/bin/python.
2. 其他具体代码看.py文件

### 02设置debug模式：
1. 在app.run()总传入一个关键字debug, app.run(debug = true),是设置当前项目为debug模式。
2. debug模式的两大功能：
* 当程序出现问题的时候，可以在页面中看到错误信息和出错的位置。
* 只要修改了项目中的'python'文件，程序会自动加载，不需要手动重新启动服务器。

### 03使用配置文件
1. 新建一个'config.py'文件,文件里面写 DEBUG = True
2. 在主APP文件中导入这个文件，并且配置到‘APP’中，示例代码如下：
``` 
improt config
app.config.from_object(config)
```
3. 还有许多的其他参数，都是放在这个配置文件中，比如'SECRET_KEY'和'SQLALCHEMY'这些配置，都是在这个文件中。
